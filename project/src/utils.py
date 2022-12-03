def read_file(file: str):
    return map(lambda line: line.rstrip(), open(file, "r"))
