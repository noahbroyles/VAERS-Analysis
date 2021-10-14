-- auto-generated definition
create table tInjuryData
(
    VAERS_ID          int         not null,
    ReceiveDate       date        null,
    State             varchar(2)  null,
    PatientAgeYEARS   float       null,
    CageYEARS         int         null,
    CageMONTHS        float       null,
    Sex               varchar(1)  null,
    ReportDate        date        null,
    Symptoms          longtext    null,
    DIED              bit         null,
    DiedDate          date        null,
    L_THREAT          bit         null,
    ER_VISIT          bit         null,
    HOSPITAL          bit         null,
    HospitalDays      int         null,
    X_STAY            bit         null,
    DISABLED          bit         null,
    Recovered         varchar(1)  null,
    VaccinationDate   date        null,
    OnsetDate         date        null,
    NumberOfDays      int         null,
    LabData           longtext    null,
    AdministeredBy    varchar(3)  null,
    FundedBy          varchar(3)  null,
    OtherMedication   longtext    null,
    CurrentIllness    longtext    null,
    MedicalHistory    longtext    null,
    PriorVaccinations text        null,
    SplitType         varchar(50) null,
    BIRTH_DEFECT      bit         null,
    OFFICIAL_VISIT    bit         null,
    ER_ED_VISIT       bit         null,
    Allergies         longtext    null,
    constraint tInjuryData_VAERS_ID_uindex
        unique (VAERS_ID)
);

alter table tInjuryData
    add primary key (VAERS_ID);


-- auto-generated definition
create table tSymptom
(
    VAERS_ID        int         not null,
    Symptom1        text        null,
    SymptomVersion1 varchar(10) null,
    Symptom2        text        null,
    SymptomVersion2 varchar(10) null,
    Symptom3        text        null,
    SymptomVersion3 varchar(10) null,
    Symptom4        text        null,
    SymptomVersion4 varchar(10) null,
    Symptom5        text        null,
    SymptomVersion5 varchar(10) null,
    constraint tSymptom_VAERS_ID_uindex
        unique (VAERS_ID)
);

alter table tSymptom
    add primary key (VAERS_ID);

-- auto-generated definition
create table tVaccine
(
    VAERS_ID     int          not null,
    VaccineType  varchar(30)  null,
    Manufacturer text         null,
    VaccineLot   varchar(100) null,
    DoseSeries   varchar(4)   null,
    VaxRoute     varchar(4)   null,
    VaxSite      varchar(3)   null,
    VaccineName  text         null,
    constraint tVaccine_VAERS_ID_uindex
        unique (VAERS_ID)
);

alter table tVaccine
    add primary key (VAERS_ID);

