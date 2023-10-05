from unittest import TestCase, main
from whiteboard import solution



class MatchTestCase(TestCase):
    def test_first_example(self):
        self.assertEqual(solution("a","b"),False)
    def test_second_example(self):
        self.assertEqual(solution("aa","ab"),False)
    def test_third(self):
        self.assertEqual(solution("aa","aab"),True)
    def test_backwards(self):
        self.assertEqual(solution("baa","aab"),True)
    def test_word(self):
        self.assertEqual(solution("leet","leetcode"),True)
    def test_gimmie(self):
        self.assertEqual(solution("Pay me!","sse eeea.aaa! yy?yPmm mmnn nn"),True)