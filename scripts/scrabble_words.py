from pathlib import Path

def _open_and_read_file(path: Path):
    raw = ''
    with open(path, 'r') as f:
        raw = f.read()
    return raw.split('\n')


def get_scrabble_words():
    words = _open_and_read_file(
        Path('files', 'collins_scrabble_words_2019.txt')
    )
    return words[3:]


def get_5_letter_words():
    p = Path('files', 'scrabble_5_letter_words.txt')
    if not p.exists():
        words = [word for word in get_scrabble_words() if len(word) == 5]
        with open(p, 'w+'):
            w = '\n'.join(words)
            p.write_text(w)
    return _open_and_read_file(p)