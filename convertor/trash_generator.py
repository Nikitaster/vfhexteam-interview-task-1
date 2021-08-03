import glob
import os
from pathlib import Path

from convertor.abstract_base_file_generator import AbstractFileGenerator


class Trasher(AbstractFileGenerator):
    def convert_files(self, *, input_dir: str, input_mask: str,
                      output_dir: str, input_prefix: str,
                      output_prefix: str) -> list[str]:
        os.makedirs(output_dir, exist_ok=True)
        result = []
        for filename in glob.glob(os.path.join(input_dir, input_mask)):
            output_name = self.output_name_generator(filename, input_prefix,
                                                     output_prefix, output_dir)
            Path(output_name).touch(exist_ok=True)
            result.append('')
        return result
