################################File Function
import error


def file_add_line_fun(fileName, text):
    with open(fileName, 'a') as file:
        file.write(f'{text}\n')


def file_read_line_fun(fileName, line):
    with open(fileName, 'r') as file:
        file = file.readlines()
        return file[line.strip()]


def file_read_fun(fileName):
    with open(fileName, 'r') as file:
        FileText = [line.strip() for line in file]
    return FileText


def spliter_fun(fullArray, index):
    result = []
    for element in fullArray:
        parts = element.split()
        if len(parts) > index:
            result.append(parts[index])
    return result


def error_fun(info):
    printError = error.Error(info)


# WINDOW FUNCTION

def window_clear_fun(window):
    for widget in window.winfo_children():
        widget.destroy()

