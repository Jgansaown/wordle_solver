from collections import Counter
from typing import Dict, List, Counter, Tuple

import numpy as np
import matplotlib.pyplot as plt

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

class Analyzer:
    def __init__(self, words: np.ndarray) -> None:
        self.words = words

    def letter_count_in_pos(self) -> List[Counter]:
        """finds the number of appearance of letters in each position

        Returns:
            List[Counter]: 
        """
        return [
            Counter(self.words[:, i])
            for i in range(self.words.shape[1])
        ]

    def letter_count_in_all(self) -> Counter:
        """finds the number of appearance of letter in all words

        Returns:
            Counter: count of appearance of letters
        """
        return sum(self.letter_count_in_pos(), Counter())

    def letter_freq_in_pos(self) -> List[Counter]:
        return [
            Counter({
                c: v/(sum(counts.values()))
                for c, v in zip(counts.keys(), counts.values())
            })
            for counts in self.letter_count_in_pos()
        ]

    def letter_freq_in_all(self):
        t = self.letter_count_in_all()
        return Counter({
            c: v/(sum(t.values()))
            for c, v in zip(t.keys(), t.values())
        })

    # def save_plots(self):
    #     y = self.letter_count_in_all()
    #     print(y)
    #     print(y.keys())
    #     print(y.values())
        
    #     fig, ax= plt.subplots()
    #     ax.bar(y.keys(), y.values())
    #     fig.savefig('test.jpg')
    #     fig.show()

    def save_frequency_analysis_plot(self, filename):
        fig, axs = plt.subplots(3, 2)
        # print([(idx1, idx2, j) for idx1, i in enumerate(axs) for idx2, j in enumerate(i)])
        pos_freq = a.letter_freq_in_pos()
        all_freq = a.letter_freq_in_all()
        print(all_freq)
        for i, ax in enumerate([a for tmp in axs for a in tmp]):
            print(i)
            print(ax)
            if i == 0:
                ax.bar(all_freq.keys(), all_freq.values())
            else:
                ax.bar(pos_freq[i-1].keys(), pos_freq[i-1].values())
        
        fig.savefig(filename)
        fig.show()
    
    def save_plot(self, x, y, filename):
        fig, ax= plt.subplots()
        ax.bar(x, y)
        fig.savefig(filename)
        fig.show()

if __name__ == '__main__':
    import main
    s = Solver(word_list=main.get_scrabble_5_letter_words())
    a = s.analyzer
    
    print(f'Number of words: {len(s.word_list)}')

    # for i, counts in enumerate(a.letter_freq_in_pos()):
    #     a.save_plot(counts.keys(), counts.values(), f'frequency_{i}.jpg')

    a.save_frequency_analysis_plot('frequency_analysis.jpg')