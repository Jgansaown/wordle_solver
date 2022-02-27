import json
from pathlib import Path
from typing import Optional, List
from multiprocessing import Pool
import os

from wordle import match_guess_to_answer
from solver import Solver

def read_words_list(path: Path, sep: str = '\n'):
    with open(path) as f:
        return f.read().split(sep)

def compute_effectiveness(answers: List[str], test_set: List[str], ranking_algorithm: str):
    solver = Solver(word_list=test_set)    
    with Pool(os.cpu_count()) as p:
        ret = p.map(solver.solve, answers)
    
    print(ret)
    with open('output.txt', 'w+') as file:
        txt = '\n'.join([json.dumps(r) for r in ret])    
        file.write(txt)

if __name__ == '__main__':
    answers = read_words_list(Path('files', 'wordle_list_of_answers.txt'))
    test_set = read_words_list(Path('files', 'scrabble_5_letter_words.txt'))

    compute_effectiveness(
        answers = answers[:10],
        test_set = test_set,
        ranking_algorithm = 'naive' #
    )

    # import numpy as np
    # with open('output.txt') as f:
    #     txt = f.read()

    # result = np.array([ line.split('=') for line in txt.split('\n') ])

    # nums = np.array([ int(n) for n in result[:, 1] ])
    # print(nums)
    # print(f'Minimum guesses: {nums.min()}, Maximum guesses: {nums.max()}, Average guesses: {nums.mean()}')

