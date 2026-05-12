#!/usr/bin/python
sample = {
  "service": "journal-api",
  "status": "healthy",
  "region": "eastus",
  "requests_last_hour": 128,
}

for key, value in sample.items():
    print(f"{key}: {value}")
