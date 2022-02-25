from collections import Counter
import string
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

    def letter_freq_in_all(self) -> Counter:
        t = self.letter_count_in_all()
        return Counter({
            c: v/(sum(t.values()))
            for c, v in zip(t.keys(), t.values())
        })


class Plotter:
    def __init__(self) -> None:
        pass

    ### Plots ###
    def save_frequency_analysis_plot(self, analyzer: Analyzer, filename: str):
        fig, axs = plt.subplots(3, 2)
        pos_freq = analyzer.letter_freq_in_pos()
        all_freq = analyzer.letter_freq_in_all()
        X = list(string.ascii_uppercase)
        for i, ax in enumerate([a for tmp in axs for a in tmp]):
            if i == 0:
                ax.bar(X, [all_freq[c] for c in X])
            else:
                ax.bar(X, [pos_freq[i-1][c] for c in X])
        fig.savefig(filename)

    def save_freq_bar_plot(self, analyzer: Analyzer, filename: str):
        pos_freq = analyzer.letter_freq_in_pos()
        all_freq = analyzer.letter_freq_in_all()
        X = list(string.ascii_uppercase)
        x = np.arange(len(string.ascii_uppercase))
        width = 0.1
        fig, ax = plt.subplots(figsize=(20,5))
        rects = []
        rects.append(ax.bar(x - 5*width/2, [all_freq[c] for c in X],    width, label='all'))
        rects.append(ax.bar(x - 3*width/2, [pos_freq[0][c] for c in X], width, label='first'))
        rects.append(ax.bar(x - 1*width/2, [pos_freq[1][c] for c in X], width, label='second'))
        rects.append(ax.bar(x + 1*width/2, [pos_freq[2][c] for c in X], width, label='third'))
        rects.append(ax.bar(x + 3*width/2, [pos_freq[3][c] for c in X], width, label='fourth'))
        rects.append(ax.bar(x + 5*width/2, [pos_freq[4][c] for c in X], width, label='fifth'))
        
        ax.set_ylabel('frequency')
        ax.set_title('Frequency')
        ax.set_xticks(x, string.ascii_uppercase)
        ax.legend()
        fig.savefig(filename, dpi=500)

if __name__ == '__main__':
    import main
    s = Solver(word_list=main.get_scrabble_5_letter_words())
    print(f'Number of words: {len(s.word_list)}')

    a = s.analyzer

    p = Plotter()
    p.save_frequency_analysis_plot(analyzer=a, filename='./out/frequency_analysis.jpg')
    p.save_freq_bar_plot(analyzer=a, filename='./out/frequency.jpg')
    