from typing import List

import numpy as np

from analyzer import Analyzer, Plotter

class Solver:
    def __init__(self, word_list: List[str]):
        self.word_list = word_list
        self.analyzer = Analyzer(
            np.array([list(word) for word in self.word_list])
        )

    def first_guess(self) -> str:
        """Picks the optimal first guess
        """
        ...

    def subsequent_guess(self, prev_hint: str) -> str:
        """Picks optimal guess with hints from previous guesses
        """
        ...

    """Private Methods"""
    def _analyze_words(self):
        ...

if __name__ == '__main__':
    import main
    s = Solver(word_list=main.get_scrabble_5_letter_words())
    print(f'Number of words: {len(s.word_list)}')

    a = s.analyzer

    p = Plotter()
    p.save_frequency_analysis_plot(analyzer=a, filename='./out/frequency_analysis.jpg')
    p.save_freq_bar_plot(analyzer=a, filename='./out/frequency.jpg')
    