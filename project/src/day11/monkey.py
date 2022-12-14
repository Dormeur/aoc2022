class Monkey:
    def __init__(self, items, operation, divisible_test, correct_monkey_id, wrong_monkey_id):
        self.inspection = 0
        self.items = items
        self.operation = operation
        self.divisible_test = divisible_test
        self.correct_monkey_id = correct_monkey_id
        self.wrong_monkey_id = wrong_monkey_id

    def play_turn(self, monkeys, mod):
        self.inspection += len(self.items)
        for item in self.items:
            boring_item = self.operation(item)
            boring_item %= mod
            if boring_item % self.divisible_test == 0:
                monkeys[self.correct_monkey_id].items.append(boring_item)
            else:
                monkeys[self.wrong_monkey_id].items.append(boring_item)
        self.items = []
