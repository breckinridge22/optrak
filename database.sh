#!/bin/bash

#brew install postgres
#brew start services postgres

set -e
set -u

INIT_DB="psql postgres"

$INIT_DB <<SQL

drop database if exists optrak;

create database optrak;
create role doctor with login password 'optrak';
grant all PRIVILEGES on database optrak to doctor;
commit;
SQL
