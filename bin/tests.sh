#!/bin/bash

# To run all tests: ./bin/tests.sh
# To run unit tests: ./bin/tests.sh unit

if [ -z "$1" ]
then
    DIR="tests/unit"
else
    DIR="$1"
fi

export ENVIRON=test
export PYTHONPATH=./scratch
pytest -s -W ignore::DeprecationWarning --cov=scratch --cov-report=term $DIR
