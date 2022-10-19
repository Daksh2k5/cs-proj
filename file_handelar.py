from converter import *
from pickle import dump, load
from csv import reader, writer


def file_convert_txt(filename):
    file_bin = open("temp.dat", "wb")
    with open(filename) as file_txt:
        while True:
            line = file_txt.readline()
            if line == "":
                break
            details = [get_roll_no(line), get_name(line), get_marks(line)]
            dump(details, file_bin)


def csv_file_writer(filename):
    file_bin = open("temp.dat", "rb"):




