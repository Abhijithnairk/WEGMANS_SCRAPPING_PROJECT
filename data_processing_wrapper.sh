#!/bin/bash

FILE="/home/abhijith/AI_ROTECH/wegmans/data.json"

if [ -f "$FILE" ]; then
    echo "$FILE found."
    /usr/bin/python3 /home/abhijith/AI_ROTECH/wegmans/data_processing.py
else
    echo "Error: File '$FILE' not found."
fi
