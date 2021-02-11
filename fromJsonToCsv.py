# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import csv

fnames = ['questions.json', 'users.json']

def getJasonVariable():
    fname = fnames[int(input("Выберите файл для перевода: \n1 вопросы\n2 пользователи\n")) - 1]
    print("был выбран файл: {0:s} \n".format(fname))
    f = open(fname, encoding='utf-8')
    ff = json.load(f)
    return ff

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # загрузка JSON файла
    ff = getJasonVariable() #здесь можно заменить на результат запроса от mongoDB

    # работа с JSON
    fff = []

    # создание заголовка файла
    dataKeys = []
    dataKeys = ff[0].keys()
    dataHeader = []
    for j in dataKeys:
        dataHeader.append(str(j))
    with open("translated.csv", mode="w", encoding='utf-8') as for_head:
        head_writer = csv.DictWriter(for_head, fieldnames=dataHeader, delimiter="\t", lineterminator="\n")
        head_writer.writeheader()

    # преобразование структуры в строку
    timing = 0
    for i in ff:
        for j in dataHeader:
            if (isinstance(i[j], list)):
                i[j] = ', '.join(i[j])
        fff.append(i)

        timing += 1
        print("line: {0:d}".format(timing))

    # сохранеие таблицы в csv-файл
    timing = 0
    for k in fff:
        with open("translated.csv", mode="a", encoding='utf-8') as fsv:
            file_writer = csv.writer(fsv, delimiter="\t", lineterminator="\n")
            file_writer.writerow(k.values())
        timing += 1
        print("file: {0:d}".format(timing))
    None
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
