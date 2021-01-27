#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "root" --dbname "root" <<-EOSQL
    CREATE DATABASE transferio;
    GRANT ALL PRIVILEGES ON DATABASE transferio TO root;
EOSQL
