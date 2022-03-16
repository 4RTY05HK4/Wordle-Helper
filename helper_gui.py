from ast import arg
from tkinter import *


def reset_list():
    var.set("Reset")
    right_list.delete(0, END)
    letters_in.delete(0, END)
    letters_not_in.delete(0, END)
    pattern.delete(0, END)
    pattern.insert(0, "-----")
    antipattern.delete(0, END)
    antipattern.insert(0, "-----")
    for word in words:
        right_list.insert(END, word)
    var.set("WORDLE!!!")


def on_validate(P):
    if len(P) <= 5:
        return True
    else:
        return False


def list_remove(word):
    try:
        idx = right_list.get(0, END).index(word)
        right_list.delete(idx)
    except ValueError:
        var.set("Not in wordlist!")


def filter_list():
    arg_dict = {
        "letters_not_in": letters_not_in.get(),
        "letters_in": letters_in.get(),
        "antipattern": antipattern.get(),
        "pattern": pattern.get(),
    }
    counter_in = 0
    flag_not_in = False
    pos_correct = True
    word_list = right_list.get(0, END)

    for word in word_list:
        for letter in arg_dict["letters_not_in"]:
            if letter in word:
                flag_not_in = True

        for letter in arg_dict["letters_in"]:
            if letter in word:
                counter_in += 1

        for i in range(0, len(arg_dict["pattern"])):
            pos = arg_dict["pattern"]
            anti_pos = arg_dict["antipattern"]
            if pos[i] != "-" and pos[i] != word[i] or anti_pos[i] == word[i]:
                pos_correct = False

        if flag_not_in is True or pos_correct is False:
            flag_not_in = False
            pos_correct = True
            list_remove(word)
        elif counter_in < len(arg_dict["letters_in"]):
            list_remove(word)
        counter_in = 0
        flag_not_in = False
        pos_correct = True

try:
    file = open("complete_wordle.txt")
except FileNotFoundError:
    print("File not found!")
    exit()
words = []
for word in file:
    words.append(word.replace("\n", ""))
file.close()

main_frame = Tk()
main_frame.geometry("400x400")

var = StringVar()
var.set("WORDLE!!!")

frame_left = Frame(main_frame)
frame_left.pack(side=LEFT)

frame_left_2 = Frame(main_frame)
frame_left_2.pack(side=LEFT)

rightframe = Frame(main_frame)
rightframe.pack(side=RIGHT)

right_list = Listbox(rightframe, bg="white", height="200")
right_list.pack(side=RIGHT, fill=BOTH)

scrollbar = Scrollbar(main_frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

for word in words:
    right_list.insert(END, word)

right_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=right_list.yview)

label_lni = Label(frame_left, text="Letters not in word")
label_lni.pack()
letters_not_in = Entry(frame_left, width=20)
letters_not_in.insert(0, "")
letters_not_in.pack(padx=5, pady=5)

label_li = Label(frame_left, text="Letters in word")
label_li.pack()
letters_in = Entry(frame_left, width=20)
letters_in.insert(0, "")
letters_in.pack(padx=5, pady=5)

label_ap = Label(frame_left, text="Wrong positions")
label_ap.pack()
antipattern = Entry(frame_left, width=20)
antipattern.insert(0, "-----")
antipattern.pack(padx=5, pady=5)

label_p = Label(frame_left, text="Correct positions")
label_p.pack()
pattern = Entry(frame_left, width=20)
pattern.insert(0, "-----")
pattern.pack(padx=5, pady=5)

validate_callback = main_frame.register(on_validate)
antipattern.configure(validate="key", validatecommand=(validate_callback, "%P"))
pattern.configure(validate="key", validatecommand=(validate_callback, "%P"))

label = Label(frame_left_2, textvariable=var)
label.pack()

Button2 = Button(frame_left, text="FILTER", command=filter_list)
Button2.pack(padx=5, pady=5)

Button_reset = Button(frame_left, text="RESET", command=reset_list)
Button_reset.pack(padx=5, pady=5)

main_frame.title("Wordle helper")
main_frame.mainloop()
