from collections import Counter

def match_guess_to_answer(answer: str, guess: str, lower: bool = False) -> str:
    """Match the guess to answer and returns the result.

    The result is a combination of `C`, `P`, `A`,
    where `C` means the letter is in the `correct` position,
    `P` means the letter is `present` in the answer but in the wrong position,
    and `A` means the letter is `absent` in the answer.

    [`guess`] and [`answer`] must be the same length.

    Args:
        answer (str): The answer
        guess (str): The guess

    Returns:
        str: The result
    """
    assert len(answer) == len(guess), "guess and answer must be the same length"

    answer = answer.lower() if lower else answer.upper()
    guess = guess.lower() if lower else guess.upper()

    # A count of number of present letters
    present = Counter(answer) & Counter(guess)

    ret = ['A' for _ in range(len(answer))]

    # Check for correct letters
    for i, c in enumerate(guess):
        if c == answer[i]:
            ret[i] = 'C'
            present[c] -= 1

    # Check for present letters
    for i, c in enumerate(guess):
        if present[c] > 0:
            ret[i] = 'P'
            present[c] -= 1

    return ''.join(ret).lower() if lower else ''.join(ret).upper()
