#!/bin/bash

export ENVIRON=local
export PYTHONPATH=./
cd scratch
pipenv run python -m run
