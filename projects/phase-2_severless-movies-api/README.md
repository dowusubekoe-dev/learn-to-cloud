# **Serverless Movie API**

**Description**  
This project involves setting up a scalable and secure infrastructure for a serverless Movies API on AWS. It showcases my expertise in designing and implementing cloud-native solutions using Infrastructure-as-Code, serverless architecture, and monitoring tools.

---

## **Table of Contents**

0. [Overview]
1. [Architecture Diagram]
2. [Skills and Technologies]
3. [Prerequisites]
4. [Setup Instructions]
5. [Project Features]
6. [Challenges and Solutions]
7. [Outcomes and Key Learnings]
8. [Future Improvements]
9. [References]

---
## **Overview**

### **Project Goals**

The main objectives of the project are;
    - Build a serverless API to manage and retrieve movie data.
    - Use Infrastructure-as-Code to automate resource provisioning on AWS.
    - Ensure high availability and scalability using cloud-native services.

### **Key Highlights**

- Demonstrates skills in Terraform, AWS Lambda, DynamoDB, S3, and API Gateway.
- Includes automation scripts for CI/CD pipelines.
- Implements best practices for security and monitoring.

---

## **Architecture Diagram**

- **Components**:
    - API Gateway → Lambda Functions → DynamoDB
    - S3 Bucket for storage
    - CloudWatch for monitoring

![Architecture Diagram](https://chatgpt.com/c/link-to-your-diagram.png)

---

## **Skills and Technologies**

Highlight the tools, technologies, and skills used in the project.

- **Cloud Provider**: AWS (DynamoDB, S3, Lambda, API Gateway, CloudWatch)
- **Infrastructure-as-Code**: Terraform / CloudFormation
- **Languages**: Python, YAML, HCL
- **CI/CD**: GitHub Actions, AWS CodePipeline
- **Monitoring**: AWS CloudWatch, CloudTrail

---
## **Prerequisites**

The tools and configurations required to set up and run the project locally or on the cloud are listed below.

- AWS account with administrative access
- Installed tools:
    - Terraform (v1.x) or AWS CLI (v2.x)
    - Python 3.9+
    - Git

---

## **Setup Instructions**

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/your-username/project-repo.git
cd project-repo
```

### **Step 2: Configure AWS Credentials**

Set up AWS credentials for Terraform or AWS CLI:

```bash
aws configure
```

### **Step 3: Deploy Infrastructure**

#### **Using Terraform**:

```bash
terraform init
terraform apply
```

#### **Using CloudFormation**:

```bash
aws cloudformation deploy --template-file template.yaml --stack-name project-stack
```

### **Step 4: Deploy Serverless Functions**

Package and upload Lambda functions:

```bash
cd lambda_functions
zip get_movies.zip get_movies.py
aws lambda update-function-code --function-name getMovies --zip-file fileb://get_movies.zip
```

---

## **Project Features**

Describe the features and functionality of the project in detail.

1. **Infrastructure as Code**:
    - Provisioned resources using Terraform/CloudFormation, ensuring consistency and repeatability.
2. **Serverless Architecture**:
    - APIs powered by AWS Lambda for dynamic content delivery.
3. **High Availability**:
    - Resources designed with scalability in mind using DynamoDB and S3.
4. **Monitoring**:
    - CloudWatch dashboards for real-time metrics and logging.

---
## **Challenges and Solutions**

Documenting challenges encountered during the project and how you solved them highlights your problem-solving skills.

|**Challenge**|**Solution**|
|---|---|
|Configuring API Gateway with custom domains was complex.|Researched AWS documentation and tutorials to configure API Gateway with Route 53.|
|DynamoDB query for sorting movies by year was returning inconsistent results.|Optimized queries using DynamoDB Global Secondary Indexes (GSIs) for efficient sorting.|
|Debugging Lambda cold start delays.|Utilized provisioned concurrency to minimize cold start latency for Lambda functions.|
|Managing IaC dependencies between resources.|Used Terraform’s `depends_on` attribute to enforce proper deployment order.|

---
## **Outcomes and Key Learnings**

Summarize what you accomplished and learned during the project.

- Successfully deployed a fully automated, scalable, and secure infrastructure.
- Improved skills in Terraform for managing AWS resources.
- Gained hands-on experience in building and deploying serverless applications.

---

## **Future Improvements**

Outline areas where the project can be enhanced. This shows foresight and continuous learning.

- Implement authentication and authorization (e.g., AWS Cognito).
- Integrate a CI/CD pipeline for automated deployments.
- Add cost-optimization strategies (e.g., reserved instances, lifecycle policies).

---

## **References**

Provide links to external resources, tutorials, or official documentation used in the project.

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Serverless Framework](https://www.serverless.com/)

---

## **Example Outputs**

Showcase screenshots or API responses for the deployed project to give recruiters a glimpse of the functionality.

Example:

- **GET /movies**
    
    ```json
    [
      {
        "id": "1",
        "title": "Inception",
        "release_year": 2010,
        "cover_image": "https://serverless-movies-api-covers.s3.amazonaws.com/inception.jpg"
      }
    ]
    ```
    
- **Monitoring Dashboard**  
    ![Monitoring Screenshot](https://chatgpt.com/c/link-to-your-dashboard-screenshot.png)
