# VAERS-Analysis
### Analyzing [VAERS (Vaccine Adverse Event Reporting System)](https://vaers.hhs.gov/) Data

This repo was created to analyze the reports of vaccine injuries since 1990, which can be downloaded from [the VAERS download page](https://vaers.hhs.gov/data/datasets.html?). When I saw that the files from 2021 were *12 times* the size of the files from 2020, I decided to look into this. WTF happened!? The year isn't even over yet!

![Image showing the difference in file sizes between 2020 and 2021](https://raw.githubusercontent.com/noahbroyles/VAERS-WTF/master/images/filesizes.png)

To use this on your own, take the following steps:
1. Run `schema.sql` in a MySQL database.
2. Install requirements: `pip3 install -r requirements.txt` 
3. Set up a `creds.py` file inside `addData` as follows:
  ```python
import os

os.environ['DBHOST'] = 'your database host'
os.environ['DBUSER'] = 'your database user'
os.environ['DBPASSWD'] = 'Your database password'
  ```
4. `cd addData`
5. Run `addCSVData.py`, `addCSVSymptoms.py`, and `addCSVVax.py`.

You are now able to run queries on the VAERS data in your database.

<small>VAERS Data ([`vaers-data`](https://github.com/noahbroyles/VAERS-WTF/tree/master/vaers-data)) Last Update: 10/13/2021</small>
