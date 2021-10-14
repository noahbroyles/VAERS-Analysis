import csv
import json
from io import StringIO


def csv2tsv(filepath, writeToPath: str = None) -> str:
    with open(filepath, 'r') as csvR:
        tsvData = csvR.read().replace(',', '\t')
    if writeToPath:
        with open(writeToPath, 'w') as t:
            t.write(tsvData)
    return tsvData


def csv2json(filepath, writeToPath: str = None):
    with open(filepath, 'r', errors='ignore') as csvFile:
        reader = csv.DictReader(csvFile)
        data = [record for record in reader]
    if writeToPath:
        with open(writeToPath, 'w') as jf:
            json.dump(data, jf, indent=4)
    return data


def tsv2csv(filepath, writeToPath: str = None) -> str:
    with open(filepath, 'r') as tsvR:
        csvData = tsvR.read().replace('\t', ',')
    if writeToPath:
        with open(writeToPath, 'w') as c:
            c.write(csvData)
    return csvData


def tsv2json(filepath, writeToPath: str = None):
    with open(filepath, 'r') as tsvFile:
        reader = csv.DictReader(tsvFile, delimiter="\t")
        data = [record for record in reader]
    if writeToPath:
        with open(writeToPath, 'w') as jf:
            json.dump(data, jf, indent=4)
    return data


def json2tsv(filepath, writeToPath: str = None) -> str:
    with open(filepath, 'r') as jf:
        data = json.load(jf)
    tsvData = StringIO()
    tsvWriter = csv.writer(tsvData, delimiter='\t')
    tsvWriter.writerow(data[0].keys())

    for row in data:
        tsvWriter.writerow(row.values())

    if writeToPath:
        with open(writeToPath, 'w') as c:
            c.write(tsvData.getvalue())

    return tsvData.getvalue()


def json2csv(filepath, writeToPath: str = None) -> str:
    with open(filepath, 'r') as jf:
        data = json.load(jf)
    csvData = StringIO()
    csvWriter = csv.writer(csvData)
    csvWriter.writerow(data[0].keys())

    for row in data:
        csvWriter.writerow(row.values())

    if writeToPath:
        with open(writeToPath, 'w') as c:
            c.write(csvData.getvalue())

    return csvData.getvalue()
