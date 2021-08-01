import argparse
import re
import string
import os
from pathlib import Path

import convertor
from convertor.decode_convertor import Decoder
from convertor.encode_convertor import Encoder


KEY_FILE = Path(os.path.join(os.path.dirname(convertor.__file__)), 'key')


def prepare_text_source(text: str):
    pattern = re.compile('[' + re.escape(string.punctuation) + ']')
    return pattern.sub('', text.lower())


def parse_args(func):
    def wrapper():
        parser = argparse.ArgumentParser()
        parser.add_argument('source_text',
                            type=str,
                            help='Returns encoded or decode text')
        return func(parser.parse_args())
    return wrapper


@parse_args
def decode(args):
    print(Decoder(KEY_FILE).convert_text(args.source_text))


@parse_args
def encode(args):
    ambient_text_without_punctuation = prepare_text_source(args.source_text)
    print(Encoder(KEY_FILE).convert_text(ambient_text_without_punctuation))
