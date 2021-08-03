from convertor.convertor import LeetConvertor


class Decoder(LeetConvertor):
    def _create_map(self, file: str, **kwargs) -> dict[str, str]:
        encode_dict = self._file_to_dict(file)
        decode_dict = {value: key for key, value in encode_dict.items()}
        assert len(decode_dict) == len(encode_dict)
        # sorted on a key len
        return dict(
            sorted(
                decode_dict.items(),
                key=lambda item: len(item[0]) + ord(item[0][0]),
                reverse=True
            )
        )
