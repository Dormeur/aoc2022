import tkinter as tk
from tkinter import CENTER


class Screen:

    def __init__(self, gui, data):
        self.data = data

        self.grid_frame = tk.Frame(gui, bd='2')
        self.grid_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.fill_grid_frame()
        self.prettify_grid_frame()

    def fill_grid_frame(self):
        for row_index, row_value in enumerate(self.data):
            for col_index, col_value in enumerate(row_value):
                tk.Label(self.grid_frame, text=col_value).grid(row=row_index, column=col_index + 1)

    def prettify_grid_frame(self):
        tk.Label(self.grid_frame, text='Cycle   1 ->').grid(row=0, column=0)
        tk.Label(self.grid_frame, text='Cycle  41 ->').grid(row=1, column=0)
        tk.Label(self.grid_frame, text='Cycle  81 ->').grid(row=2, column=0)
        tk.Label(self.grid_frame, text='Cycle 121 ->').grid(row=3, column=0)
        tk.Label(self.grid_frame, text='Cycle 161 ->').grid(row=4, column=0)
        tk.Label(self.grid_frame, text='Cycle 201 ->').grid(row=5, column=0)

        tk.Label(self.grid_frame, text='<- Cycle  40').grid(row=0, column=41)
        tk.Label(self.grid_frame, text='<- Cycle  80').grid(row=1, column=41)
        tk.Label(self.grid_frame, text='<- Cycle 120').grid(row=2, column=41)
        tk.Label(self.grid_frame, text='<- Cycle 160').grid(row=3, column=41)
        tk.Label(self.grid_frame, text='<- Cycle 200').grid(row=4, column=41)
        tk.Label(self.grid_frame, text='<- Cycle 240').grid(row=5, column=41)
