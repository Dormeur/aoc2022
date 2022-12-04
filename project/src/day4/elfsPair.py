from typing import List


class ElfsPair:

    def __init__(self, first_elf_sections: List[int], second_elf_sections: List[int]):
        self.first_elf_sections: List[int] = first_elf_sections
        self.second_elf_sections: List[int] = second_elf_sections

    def is_section_fully_containing_other(self) -> bool:
        if self.first_elf_sections.__len__() > self.second_elf_sections.__len__():
            return all(section_id in self.first_elf_sections for section_id in self.second_elf_sections)
        else:
            return all(section_id in self.second_elf_sections for section_id in self.first_elf_sections)

    def is_section_overlaps_other(self) -> bool:
        if self.first_elf_sections.__len__() > self.second_elf_sections.__len__():
            return any(section_id in self.first_elf_sections for section_id in self.second_elf_sections)
        else:
            return any(section_id in self.second_elf_sections for section_id in self.first_elf_sections)
