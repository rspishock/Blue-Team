#! /usr/bin/python3
"""
This script will parse .eml files extracting common indicators used in phishing emails.
"""

import argparse
import re
import sys

from os import path
from time import sleep

def get_arguments():
    """Get user supplied arguments from terminal"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input', help='The .eml file to analyze.')
    parser.add_argument('-o', '--output', dest='output', help='File to write parsed strings to.')
    parser.add_argument('-h', '--help', )
    options = parser.parse_args()

    return options

# argument variables
options = get_arguments()
input_file = options.input
output_file = options.output

print('\n\t\t\t\t***DISCLAIMER***')
print('''\nAll information returned from this script should be considered at face value and as a potential starting 
point for further analysis.''')
print('''\nUpon completion of the script, a deeper analysis should be performed to determine whether the suspected 
email is in fact a phishing attempt.\n''')
# script will pause for 15 seconds to give the user a chance to read the disclaimer
sleep(15)

# try:
if path.exists(input_file):
    print(f'Parsing {input_file}...')
    with open(input_file) as file_object:
        for line in file_object:
            # recipient regex
            email_regex = re.compile(f'[a-z0-9]@[a-z0-9].[a-z]')
            email = email_regex.search(line)

            # subject regex
            subject_regex = re.compile(f'Subject [a-zA-Z0-9_\s]+')
            subject = subject_regex.search(line)

            # sender regex
            sender_regex = re.compile(f'From [a-zA-Z0-9_\s]+]')
            sender = sender_regex.search(line)

            # x-sender regex
            xsender_regex = re.compile(f'xsender [a-zA-Z0-9_\s]+')
            
            # reply regex

            # date/time regex

            return[email, subject, sender,]

            
    # file output
    with open(output_file, 'w') as f:



else:
    print(f'File {input_file} not found.\nMake sure file exists and run script again.')
    sys.exit(0)
#except
