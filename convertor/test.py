import unittest

import os
import convertor

from pathlib import Path
from .encode_convertor import Encoder

KEY_FILE = Path(os.path.join(os.path.dirname(convertor.__file__)), 'key')


class EncoderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.encoder = Encoder(KEY_FILE)
        
    def test_alphabet(self):
        self.assertEqual(
            self.encoder.convert_text('abcdefghijklmnopqrstuvwxyz'),
            '48<|)3|=[#!_||<1|\/||\|0|oO_|257|_|\/\^/><¥2', 
            'Alphabet test has been failed'
        )
    
    def test_by_example_line(self):
        self.assertEqual(
            self.encoder.convert_text('this is a test task'),
            '7#!5 !5 4 7357 745|<', 
            'The encryption of the test line has been failed'
        )