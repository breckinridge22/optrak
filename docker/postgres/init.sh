#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	create role doctor with login password 'optrak';
	create database optrak;
	grant all PRIVILEGES on database optrak to doctor;
	create database hospital;
	grant all PRIVILEGES on database hospital to doctor;
EOSQL

psql -v ON_ERROR_STOP=1 -d hospital -U doctor <<-EOSQL
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
EOSQL
