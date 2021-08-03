import os
import glob

from convertor.abstract_base_convertor import AbstractTextConvertor
from convertor.abstract_base_file_generator import AbstractFileGenerator


class LeetConvertor(AbstractTextConvertor, AbstractFileGenerator):
    def __init__(self, key_file: [str, ...] = None, **_):
        assert key_file is None or os.path.isfile(key_file)
        self._latter_mapper = self._create_map(key_file)

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

    def _create_map(self, file: [str, ...], **kwargs) -> dict[str, str]:
        raise NotImplementedError

    def convert_text(self, input_text: str) -> str:
        for original, replace in self._latter_mapper.items():
            input_text = input_text.replace(original, replace, -1)
        return input_text

    def convert_files(self, *, input_dir: str, input_mask: str,
                      output_dir: str, input_prefix: str,
                      output_prefix: str) -> list[str]:
        result = []
        os.makedirs(output_dir, exist_ok=True)
        for filename in glob.glob(os.path.join(input_dir, input_mask)):
            output_name = self.output_name_generator(filename, input_prefix,
                                                     output_prefix, output_dir)
            with open(filename) as file:
                with open(output_name, 'w') as outfile:
                    converted_text = self.convert_text(file.read())
                    outfile.write(converted_text)
                result.append(converted_text)
        return result
