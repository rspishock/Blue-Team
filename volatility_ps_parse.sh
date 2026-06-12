#! /bin/bash

# check for valid image
if [[ -z '$1' ]]; then
    echo "Enter a valid memory file."
fi

# run volatility
python3 vol.py -f {$1} | awk 'print{$2}' >> services.txt