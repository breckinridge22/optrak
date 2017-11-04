#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	CREATE DATABASE optrak;
	CREATE ROLE doctor WITH LOGIN PASSWORD 'optrak';
	GRANT ALL PRIVILEGES ON DATABASE optrak TO doctor;
EOSQL

