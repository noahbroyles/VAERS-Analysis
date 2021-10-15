-- These queries are not optimized for speed

-- 2021 Cases Percentage
SELECT
    ((SELECT COUNT(*) as CasesIn2021 FROM tInjuryData WHERE YEAR(ReceiveDate) = 2021)
    / (SELECT COUNT(*) as AllCasesSince1990 FROM tInjuryData)
    * 100)
AS `2021 Cases Percentage`;

-- 2021 Deaths Percentage
SELECT ((SELECT COUNT(*) as DeathsIn2021 FROM tInjuryData WHERE DIED = 1 AND YEAR(ReceiveDate) = 2021)
     / (SELECT COUNT(*) as AllDeathsSince1990 FROM tInjuryData WHERE DIED = 1)
     * 100)
AS `2021 Deaths Percentage`;

/*

+---------------------+
|2021 Cases Percentage|
+---------------------+
|48.8508              |
+---------------------+

+----------------------+
|2021 Deaths Percentage|
+----------------------+
|65.4831               |
+----------------------+

48.9% of all cases occurred in 2021
65.5% of all deaths occurred in 2021

*/



