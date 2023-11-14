import csv
with open("demo.csv", newline='') as csvfile:
  d = csv.DictReader(csvfile)
  print("ROLL NO |  STUDENT NAME")
  print("--------------------")
  for i in d:
     print(i['Rollno'], i['student_name'])