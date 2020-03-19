import unittest
import wordwrap

class TestWordwrap(unittest.TestCase):

    def setUp(self):
        self.wordwrap = wordwrap.Wordwrap()

    def test_empty_string(self):
        self.assertEqual("",self.wordwrap.wrap("",5))
    
    def test_zero_column(self):
        self.assertEqual("",self.wordwrap.wrap("test string",0))

    def test_string_less_than_column_number(self):
        self.assertEqual("test string",self.wordwrap.wrap("test string",15))

    def test_string_same_length_as_column_number(self):
        self.assertEqual("some words",self.wordwrap.wrap("some words",10))

    def test_string_wrapped_once(self):
        self.assertEqual("random\ntext",self.wordwrap.wrap("random text",6))
    
    def test_string_wrapped_multi_line_column_aligns_with_word_boundaries(self):
        self.assertEqual("the\nthe\nthe\nthe\nthe\nthe",self.wordwrap.wrap("the the the the the the",3))

    def test_string_wrapped_multi_line_no_word_boundary_alignment(self):
        print(self.wordwrap.wrap("a random sentence that will test multiple line word wrapping",20))
        self.assertEqual("a random sentence\nthat will test\nmultiple line word\nwrapping",self.wordwrap.wrap("a random sentence that will test multiple line word wrapping",20))
