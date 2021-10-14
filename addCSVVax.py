#!/usr/bin/python3

import os
import json
import creds


from addict import Dict
from datetime import datetime
from database import Database
from svFileConvertor import csv2json
from pymysql.err import ProgrammingError


def get_date(date_string):
    if date_string != '':
        return datetime.strftime(datetime.strptime(date_string, '%m/%d/%Y'), '%Y-%m-%d')
    return ''

def determine_bool(string):
    if string == "Y":
        return 1
    elif string == "U" or string == "":
        return ''
    return 0


db = Database()

data_filenames = [f for f in os.listdir("data") if f.endswith('VAX.csv')]

for csv in data_filenames:
    print(f'ADDING RECORDS FROM {csv[:4]}...')
    records = [Dict(r) for r in csv2json(f"data/{csv}")]

    params = []
    record_count = len(records)
    for record in records:
        print(f"\tPreparing record {record.VAERS_ID}")
        c_params = [
            record.VAERS_ID,
            record.VAX_TYPE,
            record.VAX_MANU,
            record.VAX_LOT,
            record.VAX_DOSE_SERIES,
            record.VAX_ROUTE,
            record.VAX_SITE,
            record.VAX_NAME
        ]
        params += c_params

    print('Executing statement in database...')
    try:
        db.execute_stmt(f"""INSERT IGNORE INTO tVaccine (
            VAERS_ID,
            VaccineType,
            Manufacturer,
            VaccineLot,
            DoseSeries,
            VaxRoute,
            VaxSite,
            VaccineName
            )
            VALUES
            {",".join('(?,?,?,?,?,?,?,?)' for _ in range(record_count))}""",
            params=params, convert_blanks_to_nulls=True, commit=True)
    except ProgrammingError:
        with open('errors.json', 'r') as rf:
            errors = json.load(rf)
        errors.append(csv)
        with open('errors.json', 'w') as wf:
            json.dump(errors, wf, indent=4)

    print('Done.')

                
    os.system(f"mv data/{csv} data/processed/{csv}")
    print()

db.close()
