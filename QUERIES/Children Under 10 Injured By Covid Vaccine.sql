-- Children Under 10 Injured by COVID Vaccine
SELECT COUNT(*) as `Children Under 10 Injured by COVID Vaccine`
FROM tInjuryData D
    INNER JOIN tVaccine tV on D.VAERS_ID = tV.VAERS_ID
WHERE tV.VaccineType = 'COVID19'
    AND PatientAgeYEARS IS NOT NULL
    AND PatientAgeYEARS < 10
ORDER BY D.PatientAgeYEARS;

/*
Children Injured by COVID Vaccine
+------------------------------------------+
|Children Under 10 Injured by COVID Vaccine|
+------------------------------------------+
|105                                       |
+------------------------------------------+

 */