import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')

movies = [
    {
        "title": "Inception",
        "releaseYear": "2010",
        "genre": "Science Fiction, Action",
        "coverUrl": "https://your-s3-bucket-url/inception.jpg"
    },
    {
        "title": "The Shawshank Redemption",
        "releaseYear": "1994",
        "genre": "Drama, Crime",
        "coverUrl": "https://your-s3-bucket-url/shawshank-redemption.jpg"
    },
    {
        "title": "The Dark Knight",
        "releaseYear": "2008",
        "genre": "Action, Crime, Drama",
        "coverUrl": "https://your-s3-bucket-url/dark-knight.jpg"
    }
]

# Insert movie data into DynamoDB
for movie in movies:
    table.put_item(Item=movie)

