import csv
with open("demo2.csv",newline="")as csvfile:
    d = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for i in d:
        print(','.join(i))