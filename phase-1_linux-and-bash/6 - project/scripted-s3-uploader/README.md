

### Automate Credential

Secure AWS Credentials:

Never hardcode AWS credentials directly in your script.
Use environment variables or configuration files to securely store and retrieve AWS credentials.

export AWS_ACCESS_KEY_ID="your-access-key-id"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"

Before running the script, you would set the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables in your shell or in a script that calls this CloudUploader script.

export AWS_ACCESS_KEY_ID="your-access-key-id"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
./clouduploader /path/to/file.txt

./cloudupload.sh -d assets /d/devftp/madebygps/s3_upload