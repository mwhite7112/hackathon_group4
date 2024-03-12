#!/bin/bash

set -e

pip install -r requirements.txt > /dev/null

python3 main.py data/reddit_COLLEGE_2017.csv data/reddit_COLLEGE_2018.csv data/reddit_COLLEGE_2019.csv