# Blue Team

## phishing.py
Description: This script will parse .eml files extracting common points used during the analysis of potential phishing attacks.

### Usage:
Script needs the following permissions: 766
The user will not need to call the Python3 interpreter to execute the script.
./phishing.py -i <.eml file> -o <OUTPUT FILE>

## ir.bat
Description: This script will extract various network indicators from the suspected compromised host for futher analysis

### Usage:
ir.bat

## volatility_ps_parse.sh
Description: Runs Volatility on a memory file and extracts the process names for quick reference.  Output is written to 
a file called services.txt.
Note: This output is not intended to be an all inclusive investigation into the processes running on the host, rather, 
a quick look at these processes.

### Usage:
./volatility_ps_parse.sh <memoryfile>