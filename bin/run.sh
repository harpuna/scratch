#!/bin/bash

export ENVIRON=dev
export PYTHONPATH=./
cd scratch
pipenv run python -m run
