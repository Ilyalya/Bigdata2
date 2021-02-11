import csv
import columns


def createHeader(fileName):
    with open(fileName, mode="w", encoding='utf-8') as for_head:
        head_writer = csv.DictWriter(for_head, fieldnames=columns.quest_field, delimiter="\t", lineterminator="\n")
        head_writer.writeheader()


def writeToFile(fileName, question):
    with open(fileName, mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter="\t", lineterminator="\n")
        file_writer.writerow(question.values())


def collectInformation(filename, filetocollect):
    with open(filename, mode="a", encoding='utf-8') as collect_file:
        with open(filetocollect+"1.csv", mode="r", encoding='utf-8') as first_file:
            reader = csv.reader(first_file, delimiter="\t")
            writer = csv.writer(collect_file, delimiter="\t")
            writer.writerows(reader)
        for i in range(3):
            with open(filetocollect + "{0:d}.csv".format(i+2), mode="r", encoding='utf-8') as current_file:
                reader = csv.reader(current_file, delimiter="\t")
                writer = csv.writer(collect_file, delimiter="\t")
                writer.writerows(reader)
#reference: https://stackoverflow.com/questions/2512386/how-to-merge-200-csv-files-in-python

