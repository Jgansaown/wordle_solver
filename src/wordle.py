
def match_guess_to_answer(answer: str, guess: str, lower: bool = False) -> str:
    """Match the guess to answer and returns the result.

    The result is a combination of `C`, `P`, `A`,
    where `C` means the letter is in the `correct` position,
    `P` means the letter is `present` in the answer but in the wrong position,
    and `A` means the letter is `absent` in the answer.

    For example,

    Throws error when length of [`guess`] is not equal to [`answer`].

    Args:
        answer (str): The answer
        guess (str): The guess

    Returns:
        str: The result
    """

    # TODO: error when len of guess less than answer
    assert(len(answer) == len(guess))

    answer = answer.upper() if not lower else answer.lower()
    guess = guess.upper() if not lower else answer.lower()

    ret = ['A' for _ in range(len(answer))]

    # match letters in correct position
    for i in range(len(answer)):
        if answer[i] == guess[i]:
            ret[i] = 'C'
    
    # match letters present in answer but wrong position
    for i in range(len(answer)):
        # if ret is not correct, check if it is in the answer
        if ret[i] != 'C':
            # list of indexes present in answer
            for i0 in range(len(answer)):
                if answer[i0] == guess[i]:
                    if ret[i0] != 'C':
                        ret[i] = 'P'
    return ''.join(ret)

class DefinitelyNotWordle():
    """A mock wordle game
    """
    
    def __init__(self, answer: str) -> None:
        self.answer = answer.upper()

    def guess(self, guess: str) -> str:
        """Returns the result to a guess.

        Args:
            guess (str): 

        Returns:
            str: A string in the format of: C = Correct, P = Present, A = Absent
        """
        return match_guess_to_answer(self.answer, guess)
    
if __name__ == '__main__':
    game = DefinitelyNotWordle(answer='JASON')

    # answer='JASON', guess='JOHNN', ret='CPAAC'
    res = game.guess('JOHNN')
    print(f'{res} { "==" if res == "CPAAC" else "!=" } \'CPAAC\'')
