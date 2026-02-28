#!/bin/bash

# Function to display help information
function display_help() {
    echo "CloudUploader CLI"
    echo "Usage: clouduploader [OPTIONS] FILE_PATH"
    echo "Options:"
    echo "  -d, --destination    Specify the destination folder in the cloud storage"
    echo "  -h, --help           Display this help and exit"
}

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    key="$1"

    case $key in
        -d|--destination)
            DESTINATION="$2"
            shift # past argument
            shift # past value
            ;;
        -h|--help)
            display_help
            exit 0
            ;;
        *)
            DIRECTORY_PATH="$1"
            shift
            ;;
    esac
done

# Check if the directory path is provided
if [ -z "$DIRECTORY_PATH" ]; then
    echo "Error: Directory path not provided."
    display_help
    exit 1
fi

# Check if the directory exists
if [ ! -d "$DIRECTORY_PATH" ]; then
    echo "Error: Directory not found."
    exit 1
fi

# Choose your cloud provider (e.g., AWS, GCP, Azure)
# Set AWS credentials using the configuration script
source set_aws_credentials.sh

# Example: AWS S3 Upload
# Generate a pre-signed URL for each file and upload using curl
find "$DIRECTORY_PATH" -type f | while read -r file; do
    file_name=$(basename "$file")
    url=$(aws s3api create-presigned-url --bucket clouduploader --key "$DESTINATION/$file_name" --expires-in 3600)
    curl -X PUT --upload-file "$file" -L -H "Expect:" --progress-bar "$url"
done

# Use the --recursive flag to upload all files in the directory
aws s3 cp "$DIRECTORY_PATH" s3://clouduploader/$DESTINATION --recursive --no-progress

# Example: Google Cloud Storage Upload
# gsutil cp "$FILE_PATH" gs://your-bucket/$DESTINATION

# Example: Azure Blob Storage Upload
# az storage blob upload -c your-container -n $DESTINATION -t block -t page -t append --type block --account-name your-account-name --account-key your-account-key --source "$FILE_PATH"

# Add additional features and feedback here

# Display success message
# Get the number of files uploaded
num_files=$(find "$DIRECTORY_PATH" -type f | wc -l)
if [ $num_files -gt 1 ]; then
    echo "Files uploaded successfully to AWS S3!"
else
    echo "File uploaded successfully to AWS S3!"
fi
