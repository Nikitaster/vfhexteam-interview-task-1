import os


class AbstractFileGenerator():
    """Abstract base class for file generators"""
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def output_name_generator(input_file_name: str, input_prefix: str,
                              output_prefix: str, output_dir: str):
        """A method for getting output file name based on input one and prefix
        :return: output name
        """
        _, name = os.path.split(input_file_name)
        name, ext = os.path.splitext(name)
        common_suffix = name.removeprefix(input_prefix)
        return os.path.join(output_dir, f'{output_prefix}{common_suffix}{ext}')

    def convert_files(self, *, input_dir: str, input_mask: str,
                      output_dir: str, input_prefix: str,
                      output_prefix: str) -> list[str]:
        """A method for converting all files
        :param input_dir: the path to an input dir
        :param input_mask: the input file pattern name
        :param output_dir: the path to an output dir
        :param input_prefix: the input prefix for _output_name_generator
        :param output_prefix: the output prefix for _output_name_generator
        :return: the list of converted strings
        """
        raise NotImplementedError
