from pathlib import Path
from typing import Optional

from wordle import match_guess_to_answer
from solver import Solver

def read_word_list(path: Path, sep: str = '\n'):
    with open(path) as f:
        return f.read().split(sep)

def get_scrabble_5_letter_words():
    p = Path('files', 'scrabble_5_letter_words.txt')
    return read_word_list(p)

def get_words_list(path: Optional[Path] = None, sep: str = '\n'):
    return read_word_list(path, sep) if path else get_scrabble_5_letter_words()

def solve_wordle(answer: str) -> int:
    # Initialize solver
    solver = Solver(word_list=get_scrabble_5_letter_words())

    # Guess
    hint = ''
    for i in range(0, 6):
        if i == 0:
            guess = solver.first_guess()
        else:
            guess = solver.subsequent_guess(hint)
        hint = match_guess_to_answer(answer, guess)
        if hint == 'CCCCC':
            return i
    return -1


if __name__ == '__main__':
    # print(get_words_list()[:10])
    solve_wordle('JASON')
