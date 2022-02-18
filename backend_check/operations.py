import os
import datetime
import csv
from backend_check.constants import Constants as cts
# import pandas as pd


def save_info_db(name, lastname, email, movil):
    validate_file()
    _date = datetime.datetime.now().strftime('%d-%b-%Y')
    _time = datetime.datetime.now().strftime('%H:%M:%S')
    register = [name, lastname, email, movil, _date, _time]

    with open(cts.FILENAME, 'a+', newline='') as csv_file:
        new_register = csv.writer(csv_file)
        new_register.writerow(register)


def validate_file():
    # Create a csv file if this do not exist.
    if 'clients.csv' not in os.listdir(cts.PATH_DB):
        # print("Creating new client file")
        register = ['nombre', 'apellido', 'email', 'mobil', 'fecha', 'hora']
        with open(cts.FILENAME, 'w') as csv_file:
            new_register = csv.writer(csv_file)
            new_register.writerow(register)


save_info_db("Sammy", "Bastidas", "samy@gatito.com", '0912345678')

# File Verification
# df = pd.read_csv(cts.FILENAME)
# print(df)


