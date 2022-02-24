import unittest
from src.wordle import match_guess_to_answer as match

class TestWordleMatch(unittest.TestCase):

    def test_answer_and_guess_same_length(self):
        with self.assertRaises(AssertionError) as e:
            match('JASON', 'A')
        self.assertEqual(e.exception.args, ('guess and answer must be the same length',))

    def test_guess_is_all_correct(self):
        self.assertEqual(match('ABCDE', 'ABCDE'),'CCCCC')
        self.assertEqual(match('AAAAA', 'AAAAA'),'CCCCC')

    def test_guess_is_all_absent(self):
        self.assertEqual(match('ABCDE', 'FGHIJ'),'AAAAA')
        self.assertEqual(match('AAAAA', 'BBBBB'),'AAAAA')

    def test_guess_have_present_letters(self):
        self.assertEqual(match('BABBB', 'AAAAA'), 'ACAAA')
        self.assertEqual(match('BABAB', 'AAAAA'), 'ACACA')
        self.assertEqual(match('BABBB', 'ABAAA'), 'PPAAA')
        
        self.assertEqual(match('JASON', 'ABAAA'), 'PAAAA')
        self.assertEqual(match('JASON', 'AABBB'), 'ACAAA')
        self.assertEqual(match('ABCDD', 'DDDDD'), 'AAACC')
        self.assertEqual(match('ABCDD', 'DDDAA'), 'PPAPA')
    
    ### Using result from actual wordle to test
    def test_wordle_246(self):
        self.assertEqual(match('tacit', 'horse'), 'AAAAA')
        self.assertEqual(match('tacit', 'plans'), 'AAPAA')
        self.assertEqual(match('tacit', 'crane'), 'PAPAA')
        self.assertEqual(match('tacit', 'soare'), 'AAPAA')
        self.assertEqual(match('tacit', 'three'), 'CAAAA')
        self.assertEqual(match('tacit', 'trace'), 'CAPPA')
        self.assertEqual(match('tacit', 'tacit'), 'CCCCC')

    def test_wordle_250(self):
        self.assertEqual(match('bloke', 'tacit'), 'AAAAA')
        self.assertEqual(match('bloke', 'doner'), 'APAPA')
        self.assertEqual(match('bloke', 'bowie'), 'CPAAC')
        self.assertEqual(match('bloke', 'bloke'), 'CCCCC')
        