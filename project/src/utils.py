from typing import List


def read_file(file: str) -> List[str]:
    return list(map(lambda line: line.rstrip(), open(file, "r")))
