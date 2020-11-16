"""
we need to hash some data .we have a database called users_db.csv .
after hashing data from this database ,  data is saved in new database called hash_users_db.csv .
changed data are read from new database and saved in a list called users.
this list is used for generating objects,later.
"""

import csv

rows_list = []
with open('users_db.csv', 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        rows_list.append(row)

with open('hash_users_db.csv', 'w', newline='') as csv_file:
    fieldnames = ['username', 'password', 'firstname', 'lastname', 'user_id', 'user_type', 'field_name', 'field_code']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    for row in rows_list:
        csv_writer.writerow({'username': str(hash(row['username'])), 'password': str(hash(row['password'])),
                             'firstname': row['firstname'], 'lastname': row['lastname'], 'user_id': row['user_id'],
                             'user_type': row['user_type'], 'field_name': row['field_name'],
                             'field_code': row['field_code']})
users = []
with open('hash_users_db.csv', 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        users.append(row)


