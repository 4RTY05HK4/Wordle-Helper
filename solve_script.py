import sys
arg_dict = {
    "positions": None,
    "anti_pos": None,
    "pattern": None,
    "letters_in": None,
    "letters_not_in": None,
}

for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    arg = arg.split("=")
    arg_dict[arg[0]] = arg[1]

print(arg_dict)
path = sys.path[0]
file_path = path + "\complete_wordle.txt"
file_tmp_path = path + "\\tmp_file.txt"
file = open(file_path)
file_tmp = open(file_tmp_path, "w")

flag_not_in = False
pos_correct = True
counter_in = 0

if arg_dict["pattern"]:
    for word in file:
        if arg_dict["pattern"] in word:
            for letter in arg_dict["letters_not_in"]:
                if letter in word:
                    flag_not_in = True

            if flag_not_in == False:
                for letter in arg_dict["letters_in"]:
                    if letter in word:
                        counter_in += 1

            for i in range(0, len(arg_dict["positions"])):
                pos = arg_dict["positions"]
                anti_pos = arg_dict["anti_pos"]
                if pos[i] != "-" and pos[i] != word[i] or anti_pos[i] == word[i]:
                    pos_correct = False

            if flag_not_in is True or pos_correct is False:
                flag_not_in = False
                pos_correct = True
            elif counter_in == len(arg_dict["letters_in"]):
                file_tmp.write(str(counter_in) + " : " + word + "")
            counter_in = 0
            flag_not_in = False
            pos_correct = True

else:
    for word in file:
        for letter in arg_dict["letters_not_in"]:
            if letter in word:
                flag_not_in = True

        for letter in arg_dict["letters_in"]:
            if letter in word:
                counter_in += 1

        for i in range(0, len(arg_dict["positions"])):
            pos = arg_dict["positions"]
            anti_pos = arg_dict["anti_pos"]
            if pos[i] != "-" and pos[i] != word[i] or anti_pos[i] == word[i]:
                pos_correct = False

        if flag_not_in is True or pos_correct is False:
            flag_not_in = False
            pos_correct = True
        elif counter_in == len(arg_dict["letters_in"]):
            file_tmp.write(str(counter_in) + " : " + word + "")
        counter_in = 0
        flag_not_in = False
        pos_correct = True

file.close()
file_tmp.close()
