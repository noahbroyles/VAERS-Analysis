SELECT ((SELECT COUNT(*) as DeathsIn2021
FROM tInjuryData
WHERE DIED = 1 AND YEAR(ReceiveDate) = 2021) / (SELECT COUNT(*) as AllDeathsSince1990
FROM tInjuryData
WHERE DIED = 1) * 100) as `2021 Deaths Percentage`

/*
+----------------------+
|2021 Deaths Percentage|
+----------------------+
|65.4831               |
+----------------------+

*/