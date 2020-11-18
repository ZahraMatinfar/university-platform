"""
We need to hash some data .
Hashed data is saved in new database called hash_users_db.csv .
This module is written to show how to hashed data.(just for more information my girls in the group)
Notice that hash_users_db.csv is our main database ,we don't have users_db.csv in reality.
"""

import csv
from hashlib import sha256

# hashing data from users_db.csv file
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
        csv_writer.writerow({'username': row['username'], 'password': sha256(row['password'].encode()).hexdigest(),
                             'firstname': row['firstname'], 'lastname': row['lastname'], 'user_id': row['user_id'],
                             'user_type': row['user_type'], 'field_name': row['field_name'],
                             'field_code': row['field_code']})

# checking hashed data (The idea will used later)
users = []
with open('hash_users_db.csv', 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        users.append(row)
# you can try 4210z (or any passwords in users_db.csv)  then compare files (users_db.csv & hash_users_db.csv).
pass_input = input('password:').encode()
for item in users:
    if item['password'] == sha256(pass_input).hexdigest():
        print('t')
