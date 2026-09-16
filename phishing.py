#! /usr/bin/python3

#This script will parse .eml files extracting common IOCs used in phishing emails.

import argparse
import re
import sys

from os import path
from time import sleep


# Set up parsers
parser = argparse.ArgumentParser(description="Specifies the input and output files for the script..")

# Set required=True to prevent omission
parser.add_argument('-i', '--input', required=True, dest='input', help='The .eml file to analyze.')
parser.add_argument('-o', '--output', required=True, dest='output', help='File to write parsed strings to.')

args = parser.parse_args()

# Assign values to variables
input_file = args.input
output_file = args.output


print('\n\t\t\t\t***DISCLAIMER***')
print('''\nAll information returned from this script should be considered at face value and as a potential starting 
point for further analysis.''')
print('''\nUpon completion of the script, a deeper analysis should be performed to determine whether the suspected 
email is in fact a phishing attempt.\n''')
# script will pause for 8 seconds to give the user a chance to read the disclaimer
sleep(8)

print(f'Input file: {input_file}')
print(f'Output file: {output_file}')

#try:
if not path.exists(input_file): # or path:
    print(f'File {input_file} not found.\nMake sure file exists and run script again.')
    sys.exit(0)
else:
    # path.exists(input_file):
    print(f'Parsing {input_file}...')
    with open(input_file) as file_object:
        for line in file_object:
            # Metadata regexes

            # recipient regex
            recipient_regex = re.compile(f'[a-z0-9]@[a-z0-9]\.[a-z]')
            recipient = recipient_regex.search(line)

            # subject regex
            subject_regex = re.compile(f'Subject [a-zA-Z0-9_\s]+')
            subject = subject_regex.search(line)

            # sender regex
            sender_regex = re.compile(f'From [a-zA-Z0-9_\s]+]')
            sender = sender_regex.search(line)

            # x-sender regex
            xsender_regex = re.compile(f'xsender [a-zA-Z0-9_\s]+')
            xsender = xsender_regex.search(line)
            
            # reply regex
            reply_regex = re.compile(f'Reply [a-zA-Z0-9_\s]+')
            reply = reply_regex.search(line)

            # date/time regex
            date_regex = (
                r"^(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun), "  # Day of the week
                r"\d{2} "  # Day of the month
                r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) "  # Month
                r"\d{4} "  # Year
                r"\d{2}:\d{2}:\d{2} "  # Time (HH:MM:SS)
                r"[+-]\d{4}$"  # Timezone offset
            )
            dates = re.compile(f'Date: {date_regex}')
            date_search = dates.search(line)


            # return[email, subject, sender, xsender, reply]

            
    # file output
    with open(output_file, 'w') as file_output:
        print(f'IOCs from file: {input_file}')
        # recipient
        for line in recipient:
            print(line)
        #[email, subject, sender, xsender, reply]
        #    print(f'email, subject, sender, xsender, reply]')

        # sender
        for line in sender:
            print(line)

        # x-sender
        for line in xsender:
            print(line)

        # reply
        for line in reply:
            print(line)

    print(f'Script completed successfully.  Check "{output_file}" for more information.')
