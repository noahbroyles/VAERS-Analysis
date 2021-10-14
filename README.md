# VAERS-WTF
### Analyzing [VAERS (Vaccine Adverse Event Reporting System)](https://vaers.hhs.gov/) Data

This repo was created to analyze the data which can be downloaded from [the VAERS download page](https://vaers.hhs.gov/data/datasets.html?). When I saw that the file sizes from 2021 were 12 times the files from 2020, I decided to look into this. WTF happened?

To use this on your own, take the following steps:
1. Run `schema.sql` in a MySQL database.
2. Set up a `creds.py` file as follows:
  ```python
import os

os.environ['DBHOST'] = 'your database host'
os.environ['DBUSER'] = 'your database user'
os.environ['DBPASSWD'] = 'Your database password'
  ```
3. Run `addCSVData.py`, `addCSVSymptoms.py`, and `addCSVVax.py`.
