from pathlib import Path
from typing import Optional

def read_word_list(path: Path, sep: str = '\n'):
    with open(path) as f:
        return f.read().split(sep)

def get_5_letter_words():
    p = Path('files', 'scrabble_5_letter_words.txt')
    return read_word_list(p)

def get_words_list(path: Optional[Path] = None, sep: str = '\n'):
    return read_word_list(path, sep) if path else get_5_letter_words()

if __name__ == '__main__':
    print(get_words_list()[:10])