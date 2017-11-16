#!/bin/bash
brew services start postgres

set -e
set -u

OPEN_HOSP="psql -d hospital -U doctor"

# need to add in all of the constraints and primary keys and foriegn keys

$OPEN_HOSP<<SQL

CREATE TYPE file_type AS ENUM ('P', 'T');
CREATE TYPE gender_code AS ENUM ('M', 'F', 'U');

CREATE TYPE reporting_status AS ENUM ('00', '01', '02');
CREATE TYPE qualifer_code AS ENUM ('01', '02', '03', '04', '05', '06');
CREATE TYPE partial_fill_code AS ENUM ('01', '02');
CREATE TYPE payment_code AS ENUM ('01', '02', '03', '04', '05', '06', '07', '99');

DROP TABLE IF EXISTS Transaction;
CREATE TABLE Transaction (
  controlNumber integer,
  creationDate date,
  creationTime time,
  fileType file_type,
  terminator_char char
);

DROP TABLE IF EXISTS InformationSource;
CREATE TABLE InformationSource (
  id integer,
  sourceName varchar(40)
);

DROP TABLE IF EXISTS Pharmacy;
CREATE TABLE Pharmacy (
  deaNumber integer
);

DROP TABLE IF EXISTS Patient;
CREATE TABLE Patient (
  id integer,
  lastName varchar(40),
  firstName varchar(40),
  address varchar(100),
  city varchar(50),
  state varchar(40),
  zipcode integer,
  birthdate date,
  gender gender_code
);

DROP TABLE IF EXISTS DispensingInfo;
CREATE TABLE DispensingInfo (
  reportingStatus reporting_status,
  prescriptionNum integer,
  dateWritten date,
  refillsAllowed integer,
  dateFilled date,
  refillNumber integer,
  qualifer qualifer_code,
  id integer,
  daySupply integer,
  prtialFill partial_fill_code,
  payment payment_code
);

DROP TABLE IF EXISTS Prescriber;
CREATE TABLE Prescriber (
  deaNumber integer
);

DROP TABLE IF EXISTS PharmacyTrailer;
CREATE TABLE PharmacyTrailer (
  segmentCount integer
);

DROP TABLE IF EXISTS TransactionTrailer;
CREATE TABLE TransactionTrailer (
  transactionNumber integer,
  segmentCount integer
);
SQL
