import os
import re

from convertor.abstract_base_convertor import AbstractFileConvertor
import glob


class Decoder(AbstractFileConvertor):
    @staticmethod
    def _file_to_dict(filename) -> dict[str, str]:
        with open(filename) as file:
            tuple_list = [
                tuple(line.split(':', 1)) for line in file.readlines()
            ]
        return {
            original.strip().lower(): variable.strip().split(',')[0]
            for original, variable in tuple_list
        }

    def convert_text(self, input_text: str) -> str:
        for replace, original in self._latter_mapper.items():
            input_text = input_text.replace(original, replace, -1)
        return input_text

    def _create_map(self, file: str, **kwargs) -> dict[str, str]:
        assert file
        encode_dict = self._file_to_dict(file)
        decode_dict = {value: key for key, value in encode_dict.items()}
        assert len(decode_dict) == len(encode_dict)
        # sorted on a key len
        decode_dict = dict(
            sorted(encode_dict.items(),
                    key=lambda item: len(item[1]) + ord(item[1][0]),
                    reverse=True))
        return decode_dict

    def convert_files(self, *, input_dir: str, input_mask: str,
                      output_dir: str, input_prefix: str,
                      output_prefix: str):
        os.makedirs(output_dir, exist_ok=True)
        for filename in glob.glob(os.path.join(input_dir, input_mask)):
            output_name = self.output_name_generator(
                filename,
                input_prefix,
                output_prefix,
                output_dir,
            )
            with open(filename) as file:
                with open(output_name, 'w') as outfile:
                    converted_text = self.convert_text(file.read())
                    outfile.write(converted_text)
