
# ---------------------------- CONSTANTS ------------------------------- #
import tkinter

import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0

start = None



# ---------------------------- TIMER RESET ------------------------------- #
def restart():
    global REPS
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50), highlightthickness=0)
    right_label.config(text="")
    window.after_cancel(start)
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        title_label.config(text="BREAK", fg = PINK, font=(FONT_NAME, 50), highlightthickness=0)
        long_count = LONG_BREAK_MIN * 60
        count_down(long_count)

    elif REPS % 2 == 0:
        title_label.config(text="BREAK", fg = RED, font=(FONT_NAME, 50), highlightthickness=0)
        break_count = SHORT_BREAK_MIN * 60
        count_down(break_count)

    else:
        title_label.config(text="WORK", fg = GREEN, font=(FONT_NAME, 50), highlightthickness=0)
        work_count = WORK_MIN * 60
        count_down(work_count)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

import time

def count_down(count):

    count_min = math.floor(count / 60)

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global start
        start = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        session = math.floor(REPS/2)
        pomodoro = ""
        for i in range(session):
            pomodoro += "✔"
        right_label.config(text=pomodoro)


# ---------------------------- UI SETUP ------------------------------- #


from tkinter import *

window = Tk()
window.title("Pomodoro App ")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas()
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, highlightthickness=0)
title_label.config(bg=YELLOW)
title_label.grid(row=1, column=2)

start_button = Button(text="Start", bg="white", command=start_timer, highlightthickness=0)
start_button.grid(row=3, column=1)


reset_button = Button(text="Reset", bg="white", command=restart, highlightthickness=0)
reset_button.grid(row=3, column=3)


right_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "bold"), highlightthickness=0)
right_label.grid(row=4, column=2)









window.mainloop()