-- Worst COVID19 Vaccine Manufacturers
SELECT
       tV.VaccineType as `Vaccine Type`,
       tV.Manufacturer,
       SUM(DIED) as `Number of Deaths`
FROM tInjuryData D
    INNER JOIN tVaccine tV on D.VAERS_ID = tV.VAERS_ID
WHERE D.DIED = 1
    AND tV.VaccineType = 'COVID19'
GROUP BY tV.VaccineType, tV.Manufacturer
ORDER BY `Number of Deaths` DESC;
SELECT
       tV.VaccineType as `Vaccine Type`,
       tV.Manufacturer,
       COUNT(D.VAERS_ID) as `Number of Cases`
FROM tInjuryData D
    INNER JOIN tVaccine tV on D.VAERS_ID = tV.VAERS_ID
WHERE tV.VaccineType = 'COVID19'
GROUP BY tV.VaccineType, tV.Manufacturer
ORDER BY `Number of Cases` DESC;

-- Top Thrombosis Vaccines and Manufacturers
SELECT tV.VaccineType, tV.Manufacturer, COUNT(S.VAERS_ID) as `Thrombosis Cases`
FROM tSymptom S
    INNER JOIN tVaccine tV on S.VAERS_ID = tV.VAERS_ID
WHERE (
    Symptom1 = 'Thrombosis'
    OR Symptom2 = 'Thrombosis'
    OR Symptom3 = 'Thrombosis'
    OR Symptom4 = 'Thrombosis'
    OR Symptom5 = 'Thrombosis'
)
GROUP BY tV.VaccineType, tV.Manufacturer
HAVING `Thrombosis Cases` >= 5
ORDER BY `Thrombosis Cases` DESC;
