import csv

courses_list = []
with open('courses.csv', 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        courses_list.append(row)