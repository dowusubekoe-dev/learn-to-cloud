# Provider information
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Create the S3 bucket
resource "aws_s3_bucket" "movie_covers" {
  bucket = "movie-cover-thumbnails"
}

# Create the NoSQL (DynamoDB) database and table
resource "aws_dynamodb_table" "movies" {
  name         = "Movies"
  billing_mode = "PAY_PER_REQUEST"

  attribute {
    name = "MovieID"
    type = "S" # String
  }
  hash_key = "MovieID"
}

# IAM Role for Lambda Execution
resource "aws_iam_role" "lambda_execution_role" {
  name = "lambda-execution-role"
  assume_role_policy = jsonencode({
    Version : "2012-10-17"
    Statement : [
      {
        Effect : "Allow"
        Principal : {
          Service : "lambda.amazonaws.com"
        }
        Action : "sts:AssumeRole"
      }
    ]
  })
}


# IAM Policy for Lambda Function (access to DynamoDB and S3)
resource "aws_iam_role_policy" "lambda_execution_policy" {
  name = "lambda-execution-policy"
  role = aws_iam_role.lambda_execution_role.name
  policy = jsonencode({
    Version : "2012-10-17"
    Statement : [
      {
        Effect : "Allow"
        Action : [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource : "arn:aws:logs:*:*:*"
      },
      {
        Effect : "Allow"
        Action : [
          "dynamodb:*",
          "s3:*"
        ]
        Resource : "*"
      }
    ]
  })
}

# Lambda Function (no CloudFront, directly accessed via API Gateway)
resource "aws_lambda_function" "movie_function" {
  function_name = "movie_function"
  role          = aws_iam_role.lambda_execution_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"
  filename      = "function.zip" # Your Lambda deployment package (zip file)

  environment {
    variables = {
      TABLE_NAME  = aws_dynamodb_table.movies.name
      BUCKET_NAME = aws_s3_bucket.movie_covers.bucket
    }
  }
}

# API Gateway to expose the Lambda function
resource "aws_api_gateway_rest_api" "movie_api" {
  name        = "movie-api"
  description = "API for accessing movie data"
}

resource "aws_api_gateway_resource" "movies" {
  rest_api_id = aws_api_gateway_rest_api.movie_api.id
  parent_id   = aws_api_gateway_rest_api.movie_api.root_resource_id
  path_part   = "movies"
}

resource "aws_api_gateway_method" "get_movie" {
  rest_api_id   = aws_api_gateway_rest_api.movie_api.id
  resource_id   = aws_api_gateway_resource.movies.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id             = aws_api_gateway_rest_api.movie_api.id
  resource_id             = aws_api_gateway_resource.movies.id
  http_method             = aws_api_gateway_method.get_movie.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = "arn:aws:apigateway:${var.region}:lambda:path/2015-03-31/functions/${aws_lambda_function.movie_function.arn}/invocations"
}

# API Gateway Deployment
resource "aws_api_gateway_deployment" "movie_api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.movie_api.id

  # Add dependencies to ensure changes in methods or integrations trigger new deployments
  depends_on = [
    aws_api_gateway_method.get_movie,
    aws_api_gateway_integration.lambda_integration,
  ]
}

# Allow API Gateway to invoke the Lambda function
resource "aws_lambda_permission" "allow_api_gateway" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.movie_function.function_name
  principal     = "apigateway.amazonaws.com"
}

# Define the API Gateway stage
resource "aws_api_gateway_stage" "movie_api_stage" {
  stage_name    = "prod"
  rest_api_id   = aws_api_gateway_rest_api.movie_api.id
  deployment_id = aws_api_gateway_deployment.movie_api_deployment.id
}

# Output the URL for the Postman API request
output "api_url" {
  value = "${aws_api_gateway_stage.movie_api_stage.invoke_url}/movies"
}