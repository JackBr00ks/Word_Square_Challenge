#!/usr/bin/env python3
"""
Word Square Solver - Finds all possible word squares from a given set of letters.
"""

import os
import sys
import urllib.request
from collections import Counter, defaultdict
from typing import List


DEFAULT_WORDLIST_URL = "http://norvig.com/ngrams/enable1.txt"
DEFAULT_WORDLIST_LOCAL = "enable1.txt"


class WordSquareSolver:
    def __init__(self, wordlist_path: str = DEFAULT_WORDLIST_LOCAL, wordlist_url: str = DEFAULT_WORDLIST_URL):
        self.wordlist_path = wordlist_path
        self.wordlist_url = wordlist_url
        self.words = self.load_wordlist()

    def load_wordlist(self) -> List[str]:
        """Load wordlist from local file or download from URL."""
        if os.path.exists(self.wordlist_path):
            with open(self.wordlist_path, encoding="utf8") as f:
                return [w.strip().lower() for w in f if w.strip()]
        print(f"Downloading wordlist from {self.wordlist_url} ...")
        try:
            with urllib.request.urlopen(self.wordlist_url, timeout=30) as r:
                data = r.read().decode("utf8")
            words = [w.strip().lower() for w in data.splitlines() if w.strip()]
            with open(self.wordlist_path, "w", encoding="utf8") as f:
                f.write("\n".join(words))
            return words
        except Exception as e:
            print("Failed to download wordlist:", e)
            sys.exit(1)

    def find_candidates(self, letters: str, n: int) -> List[str]:
        """Return all words of length n that can be made from the given letters."""
        letters_count = Counter(letters.lower())
        candidates = []
        for w in self.words:
            if len(w) != n or not w.isalpha():
                continue
            if not Counter(w) - letters_count:
                candidates.append(w)
        return candidates

    def build_prefix_map(self, candidates: List[str]) -> dict:
        """Build a prefix -> list-of-words map for pruning."""
        pm = defaultdict(list)
        for word in candidates:
            for i in range(len(word)+1):
                pm[word[:i]].append(word)
        return pm

    def solve(self, letters: str, n: int) -> List[List[str]]:
        """Solve the word square using backtracking and prefix map optimization."""
        letters_count = Counter(letters.lower())
        candidates = self.find_candidates(letters, n)
        solutions: List[List[str]] = []
        square: List[str] = []

        if not candidates:
            return []

        prefix_map = self.build_prefix_map(candidates)

        def backtrack(row: int, remaining: Counter):
            if row == n:
                if remaining.total() == 0:
                    solutions.append(square.copy())
                return

            # Determine prefix for current row
            prefix = ''.join(square[i][row] for i in range(row)) if row > 0 else ''
            for w in prefix_map.get(prefix, []):
                wc = Counter(w)
                if any(wc[ch] > remaining.get(ch, 0) for ch in wc):
                    continue

                square.append(w)
                for ch in wc:
                    remaining[ch] -= wc[ch]

                backtrack(row + 1, remaining)

                square.pop()
                for ch in wc:
                    remaining[ch] += wc[ch]

        backtrack(0, letters_count.copy())
        return solutions


def main():
    # Challenge inputs
    challenge_inputs = [
        "4 aaccdeeeemmnnnoo",
        "5 aaaeeeefhhmoonssrrrrttttw",
        "5 aabbeeeeeeeehmosrrrruttvv",
        "7 aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy"
    ]

    solver = WordSquareSolver()

    for inp in challenge_inputs:
        n, letters = inp.split(maxsplit=1)
        n = int(n)
        print(f"\nInput: {inp}")
        sols = solver.solve(letters, n)
        if not sols:
            print("No solution found.")
        else:
            for idx, sol in enumerate(sols, 1):
                print(f"\nSolution {idx}:")
                for row in sol:
                    print(row)


if __name__ == "__main__":
    main()
