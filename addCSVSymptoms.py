import os
import creds

from addict import Dict
from svFileConvertor import csv2json
from database import Database, PreparedStatement


db = Database()

data_filenames = [f for f in os.listdir("data") if f.endswith('SYMPTOMS.csv')]

for csv in data_filenames:
    print(f'ADDING SYMPTOM RECORDS FROM {csv[:4]}...')
    records = [Dict(r) for r in csv2json(f"data/{csv}")]

    for record in records:
        print(f"\tAdding record {record.VAERS_ID}")
        pstmt = PreparedStatement("""INSERT IGNORE INTO tSymptom (
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
            (?,?,?,?,?,?,?,?,?,?,?)""",
            params=[
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
            ], convert_blanks_to_nulls=True)
        db.execute_stmt(pstmt.get_finished_sql(), commit=True)
    print()

db.close()