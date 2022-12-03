class Rucksack:

    def __init__(self, compartment):
        self.compartment = compartment
        compartment_length = compartment.__len__()
        self.first_compartment = compartment[:(compartment_length // 2)]
        self.second_compartment = compartment[(compartment_length // 2):]

    def get_shared_item(self):
        for char in self.first_compartment:
            if self.second_compartment.__contains__(char):
                return char
