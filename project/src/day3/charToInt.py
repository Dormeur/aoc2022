CODE_CONVERTER_LOWERCASE = 96
CODE_CONVERTER_UPPERCASE = 38


def char_to_int(char: str):
    if char.islower():
        return ord(char) - CODE_CONVERTER_LOWERCASE
    else:
        return ord(char) - CODE_CONVERTER_UPPERCASE
