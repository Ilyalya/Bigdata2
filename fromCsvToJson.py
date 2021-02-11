# This is a sample Python script.

import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

fnames = ['questions.csv', 'users.csv']

timing = 1

def ListGenerator(z):
    if z.find(', ') != -1:
        x = z.split(', ')
        return x
    else:
        return z

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first = True
    fname = fnames[int(input("Выберите файл для перевода: \n1 вопросы\n2 пользователи\n"))-1]
    print("был выбран файл: {0:s} \n".format(fname))
    headerData = []

    f = open(fname, encoding='utf-8')
    if f is not None:
        import csv
        readForHead = csv.reader(f, delimiter="\t", lineterminator="\n")
        headerData = next(readForHead)
    f.close()

    f = open(fname, encoding='utf-8')
    if f is not None:
        reader = csv.reader(f, delimiter="\t", lineterminator="\n")
        with open('translated.json', mode="a", encoding='utf-8') as fj:
            z = next(reader)
            z = next(reader)
            x = {headerData[0]: ListGenerator(z[0])}
            y = {headerData[1]: ListGenerator(z[1])}
            x.update(y)
            for i in range(len(headerData) - 2):
                y = {headerData[i + 2]: ListGenerator(z[i + 2])}
                x.update(y)
            fj.write('[')
            json.dump(x, fj, indent=4, ensure_ascii=False, separators=(',', ':'))
    f.close()

    f = open(fname, encoding='utf-8')
    if f is not None:
        reader = csv.DictReader(f, delimiter="\t", lineterminator="\n")
        for rows in reader:
            if first:
                first = False
                continue
            # http://coders.ask-ru.net/python-объединить-два-словаря/
            x = {headerData[0]: ListGenerator(rows[headerData[0]])}
            y = {headerData[1]: ListGenerator(rows[headerData[1]])}
            x.update(y)
            for i in range(len(headerData) - 2):
                y = {headerData[i+2]: ListGenerator(rows[headerData[i+2]])}
                x.update(y)
            with open('translated.json', mode="a", encoding='utf-8') as fj:
                fj.write(',')
                json.dump(x, fj, indent=4, ensure_ascii=False, separators=(',', ':'))

            print(timing)
            timing += 1
    f.close()

    with open('translated.json', mode="a", encoding='utf-8') as fj:
        fj.write(']')





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
