def get_roll_no(line):  # Gives the roll number of student
    s = line.split()
    return int(s[0])


def get_name(line):  # Gives name of the student
    s = line.split()
    s.pop(0)
    name = ""
    for i in s:
        if i.isdigit():
            break
        else:
            name += i +" "
    return str(name)


def get_marks(line):  # Gives a dictionary of marks

    def sub_code(code):
        if code == "301":
            return "English core"
        elif code == "302":
            return "Hindi core"
        elif code == "041":
            return "Maths"
        elif code == "042":
            return "Physics"
        elif code == "043":
            return "Chemistry"
        elif code == "044":
            return "Biology"
        elif code == "048":
            return "Physical education"
        elif code == "049":
            return "Painting"
        elif code == "054":
            return "Business studies"
        elif code == "055":
            return "Accountancy"
        elif code == "066":
            return "Entrepreneurship"
        elif code == "074":
            return "Legal studies"
        elif code == "083":
            return "Computer science"
        elif code == "241":
            return "Applied maths"
        else:
            return "Some subject"

    dict_marks = {}
    index_num = 0
    s = line.split()
    s.pop(0)
    for i in s:
        if i.isdigit():
            index_num = s.index(i)
            break
    for i in range(index_num, len(s), 3):
        if s[i].isdigit():
            lst = [s[i + 1], s[i + 2]]
            dict_marks[sub_code(str(s[i]))]=lst

        else:
            break
    return dict_marks