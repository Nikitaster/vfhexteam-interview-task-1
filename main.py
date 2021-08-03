#!/usr/bin/env python3
import os
from pathlib import Path

import convertor
from convertor.encode_convertor import Encoder
from convertor.decode_convertor import Decoder
from convertor.trash_generator import Trasher

ROOT_PATH = Path(__file__).parent
KEY_FILE = Path(os.path.join(os.path.dirname(convertor.__file__), 'key'))
SOURCE_DIR = Path(os.path.join(ROOT_PATH, 'source'))
DECODED_DIR = Path(os.path.join(ROOT_PATH, 'decoded_sources'))
ENCODED_DIR = Path(os.path.join(ROOT_PATH, 'encoded_sources'))


def assert_source_files():
    assert SOURCE_DIR.exists() and os.listdir(SOURCE_DIR)


def decode_source():
    decoder = Decoder(KEY_FILE)
    return decoder.convert_files(input_dir=SOURCE_DIR,
                                 input_mask='source*',
                                 output_dir=DECODED_DIR,
                                 input_prefix='source',
                                 output_prefix='decoded')


def generate_trash_files():
    trasher = Trasher()
    return trasher.convert_files(input_dir=DECODED_DIR,
                                 input_mask='decoded*',
                                 output_dir=DECODED_DIR,
                                 input_prefix='decoded',
                                 output_prefix='')


def encode_decoded_source():
    encoder = Encoder(KEY_FILE)
    return encoder.convert_files(input_dir=DECODED_DIR,
                                 input_mask='decoded*',
                                 output_dir=ENCODED_DIR,
                                 input_prefix='decoded',
                                 output_prefix='encoded')


def main():
    assert_source_files()
    decode_source()
    generate_trash_files()
    encode_decoded_source()


if __name__ == '__main__':
    main()
