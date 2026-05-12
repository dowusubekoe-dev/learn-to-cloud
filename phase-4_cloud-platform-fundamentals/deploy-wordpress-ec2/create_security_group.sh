#!/bin/bash

# Define variables
SECURITY_GROUP_NAME="web_app_security_group"
DESCRIPTION="My security group"
VPC_ID="vpc-05b4a3e9f72a034ef"  # Replace with your VPC ID

# Create a new security group
echo "Creating new security group..."
GROUP_ID=$(aws ec2 create-security-group --group-name "$SECURITY_GROUP_NAME" --description "$DESCRIPTION" --vpc-id $VPC_ID --query 'GroupId' --output text)
echo "Security Group Created with ID: $GROUP_ID"

# Add a rule to allow HTTP access (port 80)
echo "Adding HTTP rule..."
aws ec2 authorize-security-group-ingress --group-id $GROUP_ID --protocol tcp --port 80 --cidr 0.0.0.0/0

echo "Security group setup complete."
