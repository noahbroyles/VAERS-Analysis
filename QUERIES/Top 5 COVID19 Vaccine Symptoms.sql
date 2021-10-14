SELECT DISTINCT S.Symptom1 as Symptom, COUNT(D.VAERS_ID) as NumberOfCases
FROM tInjuryData D
    INNER JOIN tVaccine V on D.VAERS_ID = V.VAERS_ID
    INNER JOIN tSymptom S on D.VAERS_ID = S.VAERS_ID
WHERE V.VaccineType = 'COVID19'
GROUP BY S.Symptom1
ORDER BY NumberOfCases DESC
LIMIT 5;

/*
Most common Covid Vaccine Symptoms
+----------------+-------------+
|Symptom         |NumberOfCases|
+----------------+-------------+
|Arthralgia      |12176        |
|Body temperature|7142         |
|Asthenia        |6625         |
|COVID-19        |6537         |
|Chills          |6123         |
+----------------+-------------+
 
*/
