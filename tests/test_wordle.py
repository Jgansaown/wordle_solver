import unittest
import src.wordle as wordle

class TestStringMethods(unittest.TestCase):

    def test_answer_are_auto_capitalized(self):
        game = wordle.DefinitelyNotWordle(answer='jason')
        self.assertEqual(game.answer, 'JASON')

    def test_guess(self):
        game = wordle.DefinitelyNotWordle(answer='JASON')
        self.assertEqual(game.guess('JOHNN'), 'CPAAC')

    def test_guess_is_all_correct(self):
        game = wordle.DefinitelyNotWordle(answer='JASON')
        self.assertEqual(game.guess('JASON'), 'CCCCC')

    def test_guess_is_all_correct_except_one(self):
        game = wordle.DefinitelyNotWordle(answer='JASON')
        self.assertEqual(game.guess('AASON'), 'ACCCC')

    def test_guess_is_all_incorrect(self):
        game = wordle.DefinitelyNotWordle(answer='JASON')
        self.assertEqual(game.guess('THREE'), 'AAAAA')

    def test_wordle_246(self):
        game = wordle.DefinitelyNotWordle(answer='tacit')
        self.assertEqual(game.guess('horse'), 'AAAAA')
        self.assertEqual(game.guess('plans'), 'AAPAA')
        self.assertEqual(game.guess('crane'), 'PAPAA')
        self.assertEqual(game.guess('soare'), 'AAPAA')
        self.assertEqual(game.guess('three'), 'CAAAA')
        self.assertEqual(game.guess('trace'), 'CAPPA')

    def test_wordle_246_fn(self):
        self.assertEqual(wordle.match_guess_to_answer('tacit', 'horse'), 'AAAAA')
        self.assertEqual(wordle.match_guess_to_answer('tacit', 'plans'), 'AAPAA')
        self.assertEqual(wordle.match_guess_to_answer('tacit', 'crane'), 'PAPAA')
        self.assertEqual(wordle.match_guess_to_answer('tacit', 'soare'), 'AAPAA')
        self.assertEqual(wordle.match_guess_to_answer('tacit', 'three'), 'CAAAA')
        self.assertEqual(wordle.match_guess_to_answer('tacit', 'trace'), 'CAPPA')
        

if __name__ == '__main__':
    unittest.main()