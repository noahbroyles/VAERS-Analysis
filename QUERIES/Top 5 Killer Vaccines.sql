-- Top 5 Deadly Vaccines
SELECT
       tV.VaccineType as `Vaccine Type`,
       SUM(DIED) as `Number of Deaths`
FROM tInjuryData D
    INNER JOIN tVaccine tV on D.VAERS_ID = tV.VAERS_ID
WHERE D.DIED = 1
GROUP BY (tV.VaccineType)
ORDER BY `Number of Deaths` DESC
LIMIT 5;

-- Top 5 Harmful Vaccines
SELECT
       tV.VaccineType as `Vaccine Type`,
       COUNT(D.VAERS_ID) as `Number of Cases`
FROM tInjuryData D
    INNER JOIN tVaccine tV on D.VAERS_ID = tV.VAERS_ID
GROUP BY (tV.VaccineType)
ORDER BY `Number of Cases` DESC
LIMIT 5;

/*
Top 5 Deadly Vaccines
+------------+----------------+
|Vaccine Type|Number of Deaths|
+------------+----------------+
|COVID19     |8889            |
|DTAP        |881             |
|DTP         |862             |
|FLU3        |848             |
|FLUX        |643             |
+------------+----------------+

Top 5 Harmful Vaccines
+------------+---------------+
|Vaccine Type|Number of Cases|
+------------+---------------+
|COVID19     |195841         |
|FLU3        |93202          |
|VARZOS      |79179          |
|DTAP        |61242          |
|HEP         |51656          |
+------------+---------------+

*/