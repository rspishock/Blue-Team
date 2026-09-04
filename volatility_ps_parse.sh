#! /bin/bash

if ! command -v vol &> /dev/null && ! command -v volatility3 &> /dev/null; then
    echo "Volatility not found. Installing Volatility 3..."
    pip3 install volatility3
else
    echo "Volatility is already installed."
fi


# check for valid image
if [[ -z '$1' ]]; then
    echo "Enter a valid memory file."
fi

# run volatility
python3 vol.py -f {$1} | awk 'print{$2}' >> services.txt