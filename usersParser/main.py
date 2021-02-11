import user_parser
import json_writer
import csv_writer
import math

from multiprocessing import Process
import time

userBlock1 = 'users1.csv'
userBlock2 = 'users2.csv'
userBlock3 = 'users3.csv'
userBlock4 = 'users4.csv'
mrsJason1 = 'users1.json'
mrsJason2 = 'users2.json'
mrsJason3 = 'users3.json'
mrsJason4 = 'users4.json'


def usersQnaParserPepare1(firstPage, lastPage):
    for numberPage in range(firstPage, lastPage):
        success = False
        while (success == False):
            try:
                parsedUsers = user_parser.getNickUsers(numberPage)
                if (parsedUsers != None):
                    csv_writer.writeToFile(userBlock1, parsedUsers)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 1\tпарсинг страницы пользователей: {0:d}".format(numberPage))
                time.sleep(7)


def usersQnaParserPepare2(firstPage, lastPage):
    for numberPage in range(firstPage, lastPage):
        success = False
        while (success == False):
            try:
                parsedUsers = user_parser.getNickUsers(numberPage)
                if (parsedUsers != None):
                    csv_writer.writeToFile(userBlock2, parsedUsers)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 2\tпарсинг страницы пользователей: {0:d}".format(numberPage))
                time.sleep(7)


def usersQnaParserPepare3(firstPage, lastPage):
    for numberPage in range(firstPage, lastPage):
        success = False
        while (success == False):
            try:
                parsedUsers = user_parser.getNickUsers(numberPage)
                if (parsedUsers != None):
                    csv_writer.writeToFile(userBlock3, parsedUsers)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 3\tпарсинг страницы пользователей: {0:d}".format(numberPage))
                time.sleep(7)


def usersQnaParserPepare4(firstPage, lastPage):
    for numberPage in range(firstPage, lastPage):
        success = False
        while (success == False):
            try:
                parsedUsers = user_parser.getNickUsers(numberPage)
                if (parsedUsers != None):
                    csv_writer.writeToFile(userBlock4, parsedUsers)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 4\tпарсинг страницы пользователей: {0:d}".format(numberPage))
                time.sleep(7)


def usersQnaParser1():
    import csv
    with open(userBlock1, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for i in reader:
            success = False
            while (success == False):
                try:
                    parsedUsers = user_parser.getUserInfo(i)
                    if (parsedUsers != None):
                        json_writer.writeJSONtoFile(mrsJason1, parsedUsers)
                    success = True
                except:
                    print("Упс ошибочка\tпроцесс: 1\tпарсинг пользователя:{0:s}".format(i[0]))
                    time.sleep(7)


def usersQnaParser2():
    import csv
    with open(userBlock2, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for i in reader:
            success = False
            while (success == False):
                try:
                    parsedUsers = user_parser.getUserInfo(i)
                    if (parsedUsers != None):
                        json_writer.writeJSONtoFile(mrsJason2, parsedUsers)
                    success = True
                except:
                    print("Упс ошибочка\tпроцесс: 1\tпарсинг пользователя:{0:s}".format(i[0]))
                    time.sleep(7)


def usersQnaParser3():
    import csv
    with open(userBlock3, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for i in reader:
            success = False
            while (success == False):
                try:
                    parsedUsers = user_parser.getUserInfo(i)
                    if (parsedUsers != None):
                        json_writer.writeJSONtoFile(mrsJason3, parsedUsers)
                    success = True
                except:
                    print("Упс ошибочка\tпроцесс: 1\tпарсинг пользователя:{0:s}".format(i[0]))
                    time.sleep(7)


def usersQnaParser4():
    import csv
    with open(userBlock4, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for i in reader:
            success = False
            while (success == False):
                try:
                    parsedUsers = user_parser.getUserInfo(i)
                    if (parsedUsers != None):
                        json_writer.writeJSONtoFile(mrsJason4, parsedUsers)
                    success = True
                except:
                    print("Упс ошибочка\tпроцесс: 1\tпарсинг пользователя:{0:s}".format(i[0]))
                    time.sleep(7)


if __name__ == "__main__":
    ################################################################
    # ДИАПАЗОН ВОПРОСОВ ПАРСИНГА
    firstPage = int(input("\nвведите номер первой страницы: "))
    lastPage = int(input("\nвведите номер последней страницы: "))
    print("введённый интервал: с {0:d} по {1:d}\n".format(firstPage, lastPage))
    ################################################################

    countGoes = 2
    countLess = lastPage - firstPage + 1
    countLoop = math.ceil((countLess / 4) / countGoes)
    actualLength = countLoop * countGoes
    lastPage = firstPage + actualLength - 1
    print("фактический интервал: с {0:d} по {1:d}".format(firstPage, lastPage + actualLength * 3))

    # ПАРСИНГ ПОЛЬЗОВАТЕЛЕЙ
    for j in range(countLoop):
        t5 = Process(target=usersQnaParserPepare1, args=(firstPage + j * countGoes, firstPage + j * countGoes + countGoes,))
        t6 = Process(target=usersQnaParserPepare2, args=(firstPage + j * countGoes + countGoes * countLoop, firstPage + j * countGoes + countGoes + countGoes * countLoop,))
        t7 = Process(target=usersQnaParserPepare3, args=(firstPage + j * countGoes + countGoes * countLoop * 2, firstPage + j * countGoes + countGoes + countGoes * countLoop * 2,))
        t8 = Process(target=usersQnaParserPepare4, args=(firstPage + j * countGoes + countGoes * countLoop * 3, firstPage + j * countGoes + countGoes + countGoes * countLoop * 3,))
        t5.start(); t6.start(); t7.start(); t8.start()
        t5.join(); t6.join(); t7.join(); t8.join()
        t5.close(); t6.close(); t7.close(); t8.close()
        # в общей сложности парсилось 648 страниц
        # отпарсил за 61.7507860660553 секунд
        # файлы users.csv нет необходимости объединять, потому что функция в каждом процессе будет обращаться к своему файлу

        t9 = Process(target=usersQnaParser1)
        t10 = Process(target=usersQnaParser2)
        t11 = Process(target=usersQnaParser3)
        t12 = Process(target=usersQnaParser4)
        t9.start(); t10.start(); t11.start(); t12.start()
        t9.join(); t10.join(); t11.join(); t12.join()
        t9.close(); t10.close(); t11.close(); t12.close()
        # убийство процесса это плохо
        # t9.kill()
        # t10.kill()
        # t11.kill()
        # t12.kill()

        csv_writer.collectInformation('allusers.csv', 'users')
        for i in range(1, 5):
            f = open('users' + "{0:d}.csv".format(i), 'w+')
            f.seek(0)
            f.close()

        print("load {0:d} part".format(j+1) + " of {0:d}".format(countLoop))

    # отпарсил по 9 страниц с пользователями (в общей сложности 36) за 405.69443702697754 секунд!


