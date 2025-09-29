import pytest
from collections import Counter
import sys, os
import sys
import os

# Add parent directory to Python path so tests can import the solver module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from word_square_solver import WordSquareSolver


def test_load_wordlist():
    solver = WordSquareSolver()
    words = solver.load_wordlist()
    assert isinstance(words, list)
    assert all(isinstance(w, str) for w in words)
    assert all(w.islower() for w in words)

def test_find_candidates():
    solver = WordSquareSolver()
    letters = "aabc"
    n = 2
    candidates = solver.find_candidates(letters, n)
    # Only 2-letter words that use letters from "aabc"
    assert all(len(w) == n for w in candidates)
    assert all(set(w).issubset(set(letters)) for w in candidates)
    
def test_build_prefix_map():
    solver = WordSquareSolver()
    candidates = ["cat", "car", "dog"]
    pm = solver.build_prefix_map(candidates)
    # Every prefix should be a key
    expected_prefixes = ["", "c", "ca", "cat", "car", "d", "do", "dog"]
    for prefix in expected_prefixes:
        assert prefix in pm
    
def test_find_candidates_filters_length():
    solver = WordSquareSolver()
    solver.words = ["abc", "de", "fgh"]
    cands = solver.find_candidates("abcdefgh", 2)
    assert cands == ["de"]
    


