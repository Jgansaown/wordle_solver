from collections import Counter
import string
from typing import List, Counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Analyzer:
    def __init__(self, words: np.ndarray) -> None:
        self.words = words

    def get_ranked_words(self):
        ret = pd.DataFrame(
            data = {
                'rank': self.get_ranking_with_naive_method()
            },
            index = [
                ''.join([chr(c+ord('A')) for c in w])
                for w in self.words
            ],
        )
        ret.sort_values('rank', axis='index', ascending=False, inplace=True)
        return ret

    def get_ranking_with_naive_method(self):
        """Naive method to analyze words.

        Using only the frequency of letters in the whole word list to generate the ranking of each words
        """
        freq = self.letter_freq_in_all()
        return [ 
            sum( freq[c] for c in set(w) ) # set so the ranking is weighted less to words with duplicated letters
            for w in self.words
        ]

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
        X = list(range(26))
        for i, ax in enumerate([a for tmp in axs for a in tmp]):
            if i == 0:
                ax.bar(X, [all_freq[c] for c in X])
            else:
                ax.bar(X, [pos_freq[i-1][c] for c in X])
            ax.set_xticks(X, string.ascii_uppercase)
        fig.savefig(filename)

    def save_freq_bar_plot(self, analyzer: Analyzer, filename: str):
        pos_freq = analyzer.letter_freq_in_pos()
        all_freq = analyzer.letter_freq_in_all()
        X = list(range(26))
        x = np.arange(26)
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
    from pathlib import Path
    from main import read_words_list

    word_array = read_words_list(Path('files', 'scrabble_5_letter_words.txt'))
    a = Analyzer(
        words = np.array([ [ ord(c)-ord('A') for c in word ] for word in word_array])
    )

    p = Plotter()
    p.save_frequency_analysis_plot(analyzer=a, filename='./out/frequency_analysis.jpg')
    p.save_freq_bar_plot(analyzer=a, filename='./out/frequency.jpg')