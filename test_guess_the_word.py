
# Jaxon Johnson
# CIS256 Fall 2026
# Programming Assignment 4

import pytest

import guess_the_word


def test_selected_word_is_from_word_list():
    # The selected word should be in the available word list.
    selected_word = guess_the_word.choose_word()

    assert selected_word in guess_the_word.WORDS


def test_choose_word_uses_random_choice(monkeypatch):
    # Make the random selection predictable for this test.
    monkeypatch.setattr(
        guess_the_word.random,
        "choice",
        lambda words: words[0]
    )

    assert guess_the_word.choose_word(["apple", "orange"]) == "apple"


def test_correct_guess():
    # A letter in the word should be accepted.
    assert guess_the_word.check_guess("python", "p") is True


def test_incorrect_guess():
    # A letter not in the word should be rejected.
    assert guess_the_word.check_guess("python", "z") is False


def test_display_reveals_repeated_letters():
    # Guessing a letter reveals every time it appears.
    result = guess_the_word.display_word("letter", {"t"})

    assert result == "_ _ t t _ _"


def test_empty_word_list_raises_error():
    # An empty word list should raise an error.
    with pytest.raises(ValueError):
        guess_the_word.choose_word([])
