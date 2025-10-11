import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import random

def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("gui")
    frm_main.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)
    setup_main(frm_main)
    frm_main.mainloop()

def setup_main(frm):
    lbl_sides = Label(frm, text="Enter the number of sides on the dice (2-20): ")
    lbl_sides.grid(row=0, column=0)
    ent_sides = IntEntry(frm, width = 2, lower_bound=2, upper_bound=20)
    ent_sides.grid(row=0, column=1)

    lbl_count = Label(frm, text="Enter the amount of dice to roll (1-10): ")
    lbl_count.grid(row=1, column=0)
    ent_count = IntEntry(frm, width = 2, lower_bound= 1, upper_bound= 10)
    ent_count.grid(row=1, column=1)

    btn_roll = Button(frm, text="Roll!")
    btn_roll.grid(row=2)
    lbl_roll = Label(frm, text="")
    lbl_roll.grid(row=3)

    def roll_dice(sides, count):
        sum = 0
        rolltext = ""
        for roll in range(count):
            die_roll = random.randint(1, sides)
            sum += die_roll
            rolltext += f" {die_roll} "
        rolltext += f"Total: {sum}"
        return rolltext

    def roll_action():
        try:
            sides = ent_sides.get()
        except ValueError:
            lbl_roll.config(text="You must enter a valid number of sides.")
        try:
            count = ent_count.get()
        except ValueError:
            lbl_roll.config(text="You must enter a valid number of dice.")
        lbl_text = roll_dice(sides, count)
        lbl_roll.config(text=lbl_text)

    btn_roll.config(command=roll_action)

if __name__ == "__main__":
    main()