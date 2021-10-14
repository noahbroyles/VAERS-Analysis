SELECT ((SELECT COUNT(*) as DeathsIn2021
FROM tInjuryData
WHERE DIED = 1 AND YEAR(ReceiveDate) = 2021) / (SELECT COUNT(*) as AllDeathsSince1990
FROM tInjuryData
WHERE DIED = 1) * 100) as `Pecentage of 2021 Deaths per All Deaths`