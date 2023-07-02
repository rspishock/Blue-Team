#! /usr/bin/python3
"""
This script will parse .eml files extracting common indicators used in phishing emails.
"""

import argparse
import re

from os import path
from time import sleep

def get_arguments():
    """Get user supplied arguements from terminal"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='file', help='The .eml file to examine.')
    # parser.add_argument('-h', '--help', )
    options = parser.parse_args()

    return options


print('\n\t\t\t\t***DISCLAIMER***')
print('\nAll infomration returned from this script should be considered at face value and as a potential jump point for analysis.')
print('\nMalware authors will often put code into their malware in an attempt to steer analysts away from the actual intent of their code.py.')
print('\nUpon completion of the script, a deeper analysis should be performed to determine whether the suspected code is in fact malware.\n')
# script will pause for 15 seconds to give the user a chance to read the disclaimer
sleep(15)

try:
