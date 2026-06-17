# *********************************************
# *        Environmental preperation          *
# *********************************************
$USER = $env:UserName
$DIRECTORY = "C:\Security Test\%DATE%_%TIME%\"

if (Test-Path -Path $DIRECTORY) {
    Remove-Item -Path $DIRECTORY
} else {
    mkdir $DIRECTORY
    cd $DIRECTORY
}

# *********************************************
# *               Perform scans               *
# *********************************************
# view network shares
# *Note: this command is checking the network shares on the local host, represented by the IP address 127.0.0.1


# view network sessions
echo "Sessions:" >> connections.txt
Get-NetTCPConnection >> connections.txt

#lists information related to mapped connections


# view active TCP connections
echo "Active connections:"
Get-NetTCPConnection -State Established >> connections.txt

