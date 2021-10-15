-- Cases by Gender
SELECT Sex, COUNT(*) as NumberOfCases
FROM tInjuryData
WHERE Sex <> 'U'
GROUP BY Sex

/*
 Cases by Gender
 +---+-------------+
|Sex|NumberOfCases|
+---+-------------+
|F  |976308       |
|M  |491012       |
+---+-------------+

 */
