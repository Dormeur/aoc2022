class ElfsGroup:

    def __init__(self, rucksacks):
        self.rucksacks = rucksacks

    def get_badge(self):
        for item in self.rucksacks[0].compartment:
            if self.rucksacks[1].compartment.__contains__(item) and self.rucksacks[2].compartment.__contains__(item):
                return item
