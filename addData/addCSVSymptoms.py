#!/usr/bin/python3

import os
import creds

from addict import Dict
from database import Database
from svFileConvertor import csv2json


db = Database()

data_filenames = [f for f in os.listdir("../data") if f.endswith('SYMPTOMS.csv')]

for csv in data_filenames:
    print(f'ADDING SYMPTOM RECORDS FROM {csv[:4]}...')
    records = [Dict(r) for r in csv2json(f"../data/{csv}")]
    record_count = len(records)

    params = []
    for record in records:
        print(f"\tPreparing record {record.VAERS_ID}")
        c_params = [
            record.VAERS_ID,
            record.SYMPTOM1,
            record.SYMPTOMVERSION1,
            record.SYMPTOM2,
            record.SYMPTOMVERSION2,
            record.SYMPTOM3,
            record.SYMPTOMVERSION3,
            record.SYMPTOM4,
            record.SYMPTOMVERSION4,
            record.SYMPTOM5,
            record.SYMPTOMVERSION5
        ]
        params += c_params
    print("Executing statement in database...")
    db.execute_stmt(f"""INSERT IGNORE INTO tSymptom (
        VAERS_ID,
        Symptom1,
        SymptomVersion1,
        Symptom2,
        SymptomVersion2,
        Symptom3,
        SymptomVersion3,
        Symptom4,
        SymptomVersion4,
        Symptom5,
        SymptomVersion5
        )
        VALUES
        {",".join('(?,?,?,?,?,?,?,?,?,?,?)' for _ in range(record_count))}""",
        params=params, convert_blanks_to_nulls=True)

    os.system(f"mv ../data/{csv} ../data/processed/{csv}")
    print('Done.')

db.close()
