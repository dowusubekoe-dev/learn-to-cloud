#!/bin/bash

# Check if the configuration file exists
if [ ! -f "aws_credentials.txt" ]; then
    echo "Error: Configuration file (aws_credentials.txt) not found."
    exit 1
fi

# Read and export AWS credentials
source aws_credentials.txt