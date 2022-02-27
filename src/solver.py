from random import randint
from typing import Iterable, List

import numpy as np
from numpy.typing import NDArray

from analyzer import Analyzer
from wordle import match_guess_to_answer as match

def match_correct(word: str, correct: Iterable[str]):
    for w, c in zip(word, correct):
        if w != c and c != '':
            return False
    return True

def match_incorrect(word: str, incorrects: Iterable[Iterable[str]]):
    for incorrect in incorrects:
        for w, i in zip(word, incorrect):
            if w == i and i != '':
                return False
    return True

def filter_word_list(
    word_array: NDArray, 
    correct: Iterable[str],
    incorrect: Iterable[Iterable[str]],
    present: Iterable[str],
    absent: Iterable[str]
) -> NDArray:
    """filter the word list based on 'Present' letters and 'Absent' letters

    Args:
        word_list (List[str]): list of words
        present (Iterable[str]): list of letters present in the answer
        absent (Iterable[str]): list of letters absent from the answer

    Returns:
        List[str]: filtered word list
    """
    return np.array([
        w
        for w in word_array
        if set(w).issuperset(present) # True if every element in 'present' is in the word
        and set(w).isdisjoint(absent) # True if every element in 'absent is NOT in the word
        and match_correct(w, correct)
        and match_incorrect(w, incorrect)
    ])

class Solver:
    def __init__(self, word_list: List[str], isupper: bool = True):
        self.word_list = word_list
        self.isupper = isupper

        # Initializations
        self.word_array = np.array(self.word_list)
        self.filter = self._initialize_filter()

    """
        Public Methods
    """
    def guess(self, prev_guess: str, hint: str) -> str:
        """Picks optimal guess with hints from previous guesses

            Initial previous guess and hint are empty strings
        """
        if prev_guess == '' and hint == '':
            word_array = self.word_array
        else:
            word_array = self._filtered_word_list(prev_guess, hint)

        # Get new rankings
        ranking = Analyzer(words=self._get_ord_array(word_array)).get_ranked_words()

        # FIXME: this is so dumb
        if ranking.iloc[0].name == prev_guess:
            return ranking.iloc[ randint(1, len(ranking))-1 ].name 
        return ranking.iloc[0].name

    def solve(self, answer: str):
        """
        """
        self.reset()
        guesses, hints, rounds = [''], [''], 1
        correct = 'C' * len(answer)
        while hints[-1] != correct:
            try:
                guesses.append(self.guess(prev_guess=guesses[-1], hint=hints[-1]))
            except Exception: # TODO: Better error handling
                return {
                    'answer': answer,
                    'guesses': guesses[1:],
                    'hints': hints[1:],
                    'rounds': -1
                }
            hints.append(match(answer, guesses[-1]))
            rounds += 1
        #     print(f'Answer: {answer}, Guess: {guesses}, Hint: {hints}')
        # print(f'Number of guesses for \'{answer}\': {rounds}')
        return {
            'answer': answer,
            'guesses': guesses[1:],
            'hints': hints[1:],
            'rounds': rounds
        }

    def reset(self):
        """Resets solver to initial state
        """
        self.filter = self._initialize_filter()
    
    """
        Private Methods
    """
    def _initialize_filter(self):
        return {
            'present': [],
            'absent': [],
            'correct': ['' for _ in self.word_array[0]],
            'incorrect': []
        }

    def _get_ord_array(self, word_array: np.ndarray):
        diff = ord('A') if self.isupper else ord('a')
        return np.array([ [ ord(c)-diff for c in word ] for word in word_array])

    def _update_filter(self, prev_guess, hint):
        # TODO: check if this can be simplified
        self.filter['incorrect'].append(['' for _ in self.word_array[0]])
        for i, (g, c) in enumerate(zip(prev_guess, hint)):
            if (
                g not in self.filter['correct'] 
                and g not in self.filter['present'] 
                and c == 'A' or c == 'a'
            ):
                self.filter['absent'].append(g)
            elif c == 'P' or c == 'p':
                self.filter['present'].append(g)
                self.filter['incorrect'][-1][i] = g
            elif c == 'C' or c == 'c':
                self.filter['correct'][i] = g
                if g in self.filter['absent']:
                    self.filter['absent'].remove(g)
            else:
                ...
    
    def _filtered_word_list(self, prev_guess, hint) -> NDArray:
        """filter the word list based on 'Present' letters and 'Absent' letters
        """
        self._update_filter(prev_guess, hint)
        return np.array([
            w
            for w in self.word_array
            if set(w).issuperset(self.filter['present']) # True if every element in 'present' is in the word
            and set(w).isdisjoint(self.filter['absent']) # True if every element in 'absent is NOT in the word
            and match_correct(w, self.filter['correct'])
            and match_incorrect(w, self.filter['incorrect'])
        ])

if __name__ == '__main__':
    pass
