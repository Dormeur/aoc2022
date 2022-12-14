from day11.monkey import Monkey


def to_items_list(sentence):
    return list(map(int, sentence.lstrip().removeprefix('Starting items: ').split(',')))


def to_operation_function(sentence):
    return eval("lambda old:" + sentence.lstrip().removeprefix('Operation: new ='))


def to_divisible_test(sentence) -> int:
    return int(sentence.lstrip().removeprefix('Test: divisible by '))


def to_monkey_id(sentence) -> int:
    return int(sentence.split(' ')[-1])


def to_monkey(paragraph: list[str]):
    return Monkey(to_items_list(paragraph[1]),
                  to_operation_function(paragraph[2]),
                  to_divisible_test(paragraph[3]),
                  to_monkey_id(paragraph[4]),
                  to_monkey_id(paragraph[5]))
