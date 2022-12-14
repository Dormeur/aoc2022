from typing import List


def read_file(file: str) -> List[str]:
    return open(file).read().strip().splitlines()
