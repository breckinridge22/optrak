#!/bin/bash

#brew install postgres
brew services start postgres

set -e
set -u

INIT_DB="psql postgres"

$INIT_DB <<SQL
create role doctor with login password 'optrak';
create database optrak;
grant all PRIVILEGES on database optrak to doctor;
create database hospital;
grant all PRIVILEGES on database hospital to doctor;
commit;
SQL
