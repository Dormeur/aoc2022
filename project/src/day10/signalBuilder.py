import tkinter as tk

import numpy as np

from day10.screen import Screen
from utils import read_file

monitored_cycles: dict = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}

f = read_file('../resources/input_day_10.txt')
screen_data = np.full((6, 40), '.')


def get_instruction():
    return f.pop(0) if len(f) > 0 else None


def draw_pixel(cycle, x):
    col = (cycle - 1) % 40
    if col in [x - 1, x, x + 1]:
        row = (cycle - 1) // 40
        screen_data[row][col] = '#'


def build_signal():
    buffer, cycle, x = None, 0, 1
    instruction = get_instruction()
    while instruction:
        cycle += 1
        draw_pixel(cycle, x)

        if cycle in monitored_cycles.keys():
            monitored_cycles[cycle] = x

        if instruction == 'noop':
            instruction = get_instruction()
        elif buffer is None:
            buffer = int(instruction.split()[1])
        else:
            x += buffer
            buffer = None
            instruction = get_instruction()


def print_sum_of_monitored_cycles():
    print(sum(signal * value for signal, value in monitored_cycles.items()))


def print_screen():
    gui = tk.Tk()
    gui.title('Message :')
    gui.geometry('800x200')
    gui.configure(bg='lightgray')
    Screen(gui, screen_data)
    gui.mainloop()
