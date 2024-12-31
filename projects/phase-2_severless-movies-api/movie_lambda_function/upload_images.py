import boto3
import os

# AWS S3 bucket name
BUCKET_NAME = "movie-cover-thumbnails"

# Folder containing movie cover images
IMAGE_FOLDER = "/home/dorbsyfx-iac-svr/my_journal/devops-job_oriented-roadmap/projects/phase-2_severless-movies-api/movie_covers"

# Initialize the S3 client
s3_client = boto3.client("s3")

def upload_images_to_s3():
    for image_name in os.listdir(IMAGE_FOLDER):
        image_path = os.path.join(IMAGE_FOLDER, image_name)
        
        if os.path.isfile(image_path):
            print(f"Uploading {image_name} to S3 bucket {BUCKET_NAME}")
            s3_client.upload_file(image_path, BUCKET_NAME, image_name)
    
    print("All images uploaded successfully.")

if __name__ == "__main__":
    upload_images_to_s3()
