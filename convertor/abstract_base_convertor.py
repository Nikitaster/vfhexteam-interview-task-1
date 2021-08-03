import os
from abc import ABC


class AbstractTextConvertor(ABC):
    """Abstract base - interface for 1337 encoder / decoder
    """
    def __init__(self, key_file: [str, ...] = None, **_):
        assert key_file is None or os.path.isfile(key_file)
        self._latter_mapper = self._create_map(key_file)

    def _create_map(self, file: [str, ...], **kwargs) -> dict[str, str]:
        """A method for generating map (dict) for encode/decode text
        :param file: the optional path to a file with text
        :return: encode/decode dict, return empty dict if file is None
        """
        raise NotImplementedError

    def convert_text(self, input_text: str) -> str:
        """A method for the convert the text
        (encode -> decode | decode -> encode)
        :param input_text: the text to convert
        :return: converted text
        """
        raise NotImplementedError

