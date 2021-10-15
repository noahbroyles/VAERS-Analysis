-- Autism Cases
SELECT COUNT(D.VAERS_ID) as AustismCases, tV.VaccineType, tV.Manufacturer
FROM tInjuryData D
    INNER JOIN tSymptom tS on D.VAERS_ID = tS.VAERS_ID
    INNER JOIN tVaccine tV on D.VAERS_ID = tV.VAERS_ID
WHERE
    'Autism' IN (Symptom1, Symptom2, Symptom3, Symptom4, Symptom5)
GROUP BY tV.VaccineType, tV.Manufacturer
ORDER BY AustismCases DESC, tV.VaccineType
LIMIT 5;

/*
Autism Cases, Vaccines, and Manufacturer
+------------+-----------+--------------------+
|AustismCases|VaccineType|Manufacturer        |
+------------+-----------+--------------------+
|1150        |MMR        |MERCK & CO. INC.    |
|99          |HEP        |MERCK & CO. INC.    |
|96          |DTAP       |UNKNOWN MANUFACTURER|
|83          |DTP        |UNKNOWN MANUFACTURER|
|77          |DTAP       |SANOFI PASTEUR      |
+------------+-----------+--------------------+

*/
