import boto3
import json

# AWS service resources
dynamodb = boto3.resource("dynamodb")
s3_client = boto3.client("s3")

# DynamoDB table name
TABLE_NAME = "Movies"

# S3 bucket name
BUCKET_NAME = "movie-cover-thumbnails"

def get_s3_url(object_key):
    """Generate the public URL for an S3 object."""
    return f"https://{BUCKET_NAME}.s3.amazonaws.com/{object_key}"

def load_movie_data():
    # Load movie data from JSON file
    with open("movies-data.json", "r") as file:
        movies = json.load(file)
    
    table = dynamodb.Table(TABLE_NAME)

    for movie in movies:
        movie_id = movie["MovieID"]
        cover_image = movie["CoverImage"]

        # Generate the S3 URL for the cover image
        cover_image_url = get_s3_url(cover_image)

        # Add the URL to the movie record
        movie["CoverImageURL"] = cover_image_url

        # Put the item in DynamoDB
        print(f"Adding movie: {movie_id} to DynamoDB")
        table.put_item(Item=movie)

    print("All movie data loaded successfully.")

if __name__ == "__main__":
    load_movie_data()
