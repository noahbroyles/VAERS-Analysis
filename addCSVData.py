import os
import json
import creds


from addict import Dict
from datetime import datetime
from svFileConvertor import csv2json
from pymysql.err import ProgrammingError
from database import Database, PreparedStatement



def get_date(date_string):
    if date_string != '':
        return datetime.strftime(datetime.strptime(date_string, '%m/%d/%Y'), '%Y-%m-%d')
    return ''

def determine_bool(string):
    if string == "Y":
        return 1
    elif string == "":
        return ''
    return 0


db = Database()

data_filenames = [f for f in os.listdir("data") if f.endswith('DATA.csv')]

for csv in data_filenames:
    print(f'ADDING RECORDS FROM {csv[:4]}...')
    records = [Dict(r) for r in csv2json(f"data/{csv}")]

    for record in records:
        print(f"\tAdding record {record.VAERS_ID}")
        pstmt = PreparedStatement("""INSERT IGNORE INTO tInjuryData (
            VAERS_ID,
            ReceiveDate,
            State,
            PatientAgeYEARS,
            CageYEARS,
            CageMONTHS,
            Sex,
            ReportDate,
            Symptoms,
            DIED,
            DiedDate,
            L_THREAT,
            ER_VISIT,
            HOSPITAL,
            HospitalDays,
            X_STAY,
            DISABLED,
            Recovered,
            VaccinationDate,
            OnsetDate,
            NumberOfDays,
            LabData,
            AdministeredBy,
            FundedBy,
            OtherMedication,
            CurrentIllness,
            MedicalHistory,
            PriorVaccinations,
            SplitType,
            BIRTH_DEFECT,
            OFFICIAL_VISIT,
            ER_ED_VISIT,
            Allergies
            ) 
            VALUES
            (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            params=[
                record.VAERS_ID, 
                get_date(record.RECVDATE),
                record.STATE,
                record.AGE_YRS,
                record.CAGE_YR,
                record.CAGE_MO,
                record.SEX,
                get_date(record.RPT_DATE),
                record.SYMPTOM_TEXT,
                determine_bool(record.DIED),
                get_date(record.DATEDIED),
                determine_bool(record.L_THREAT),
                determine_bool(record.ER_VISIT), 
                determine_bool(record.HOSPITAL),
                record.HOSPDAYS,
                determine_bool(record.X_STAY),
                determine_bool(record.DISABLE),
                determine_bool(record.RECOVD),
                get_date(record.VAX_DATE),
                get_date(record.ONSET_DATE),
                record.NUMDAYS,
                record.LAB_DATA,
                record.V_ADMINBY,
                record.V_FUNDBY,
                record.OTHER_MEDS,
                record.CUR_ILL,
                record.HISTORY,
                record.PRIOR_VAX,
                record.SPLTTYPE,
                determine_bool(record.BIRTH_DEFECT),
                determine_bool(record.OFC_VISIT),
                determine_bool(record.ER_ED_VISIT),
                record.ALLERGIES
            ], convert_blanks_to_nulls=True)

        try:
            db.execute_stmt(pstmt.get_finished_sql(), commit=True)
        except ProgrammingError:
            with open('errors.json', 'r') as rf:
                errors = json.load(rf)
            errors[record.VAERS_ID] = record
            with open('errors.json', 'w') as wf:
                json.dump(errors, wf, indent=4)
                
    os.system(f"mv data/{csv} processed/{csv}")
    print()

db.close()
