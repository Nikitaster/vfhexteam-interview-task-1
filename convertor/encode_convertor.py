from convertor.convertor import LeetConvertor


class Encoder(LeetConvertor):
    def _create_map(self, file: str, **kwargs) -> dict[str, str]:
        return self._file_to_dict(file)
