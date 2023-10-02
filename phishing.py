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
    parser.add_argument('-i', '--input', dest='input', help='The .eml file to analyze.')
    parser.add_argument('-o', '--output', dest='output', help='File to write parsed strings to.')
    # parser.add_argument('-h', '--help', )
    options = parser.parse_args()

    return options

# argument variables
options = get_arguments()
input_file = options.input
output_file = options.output

print('\n\t\t\t\t***DISCLAIMER***')
print('\nAll information returned from this script should be considered at face value and as a potential jump point for further analysis.')
print('\nUpon completion of the script, a deeper analysis should be performed to determine whether the suspected code is in fact malware.\n')
# script will pause for 15 seconds to give the user a chance to read the disclaimer
sleep(15)

try:
    if path.exists(input_file):
        with open(input_file) as file_object:
            for line in file_object:
                #recipient regex
                email_regex = re.compile(f'[a-z0-9]@[a-z0-9].[a-z]')
                file = email_regex.search(line)
                #subject regex
                subject_regex = re.compile(f'Subject [a-z0-9]@[a-z0-9].[a-z]')
                file = subject_regex.search(line)
                #sender regex

                #x-sender regex

                #reply regex

                #date/time regex
