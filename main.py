from tkinter import *
import math
from typing_text import *

# Constants
PINK = "#e2979c"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TEST_LENGTH = 60
time = None


# Timer Reset

def reset_timer():
    window.after_cancel(time)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(wpm_text, text="0")
    canvas.itemconfig(accuracy_text, text="0%")


# Timer Mechanism

def start_timer():
    timer.config(text="Start", fg=PINK)
    count_down(TEST_LENGTH)


# Calculate WPM

def calculate_wpm(input_text):
    original_text_split = original_text.split(" ")
    count = 0
    count_wrong = 0
    total_words = len(input_text)
    for word in input_text:
        if word == original_text_split[input_text.index(word)]:
            count += 1

        if word != original_text_split[input_text.index(word)]:
            count_wrong += 1

    accuracy_percentage = round(count / total_words, 2)

    canvas.itemconfig(wpm_text, text=count)
    canvas.itemconfig(accuracy_text, text=f"{accuracy_percentage}%")


# Countdown Mechanism

def count_down(count):
    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")

    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        calculate_wpm(typing_input.get().split())


# UI Setup
window = Tk()
window.title("Typing Test")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=1000, height=600, bg=YELLOW, highlightthickness=0)
keyboard_img = PhotoImage(file="keyboard.png")
canvas.create_image(500, 500, image=keyboard_img)

blank_text = canvas.create_text(0, 0, text="label", fill=YELLOW)
canvas.grid(row=1, column=1)

timer_text = canvas.create_text(500, 100, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))

wpm_label = Label(text="WPM", font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
wpm_label.place(x=350, y=10)
wpm_text = canvas.create_text(270, 100, text="0", fill="black", font=(FONT_NAME, 35, "bold"))

accuracy_label = Label(text="Accuracy", font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
accuracy_label.place(x=800, y=10)
accuracy_text = canvas.create_text(800, 100, text="0%", fill="black", font=(FONT_NAME, 35, "bold"))

timer = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
timer.place(x=550, y=10)

typing_input = Entry(width=25)
typing_input.place(x=550, y=350)

start_button = Button(text="Start", highlightthickness=0, padx=50, pady=10, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, padx=50, pady=10, command=reset_timer)
reset_button.grid(row=2, column=2)

# All text for typing phrase
typing_text_1 = Label(text=broken_text_1, font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg='black')
typing_text_1.place(x=0, y=150)

typing_text_2 = Label(text=broken_text_2, font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg='black')
typing_text_2.place(x=0, y=170)

typing_text_3 = Label(text=broken_text_3, font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg='black')
typing_text_3.place(x=0, y=190)

typing_text_4 = Label(text=broken_text_4, font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg='black')
typing_text_4.place(x=0, y=210)

typing_text_5 = Label(text=broken_text_5, font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg='black')
typing_text_5.place(x=0, y=230)

typing_text_6 = Label(text=broken_text_6, font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg='black')
typing_text_6.place(x=0, y=250)

window.mainloop()
