# Azure Resume Challenge - Static Web App + Managed API + Cosmos DB

This project is a cloud-hosted resume website built on Microsoft Azure. It uses Azure Static Web Apps for the frontend, a managed Azure Functions API for the visitor counter, and Azure Cosmos DB for persistent data storage.

## Architecture

- Azure Static Web Apps
- Managed Azure Functions API
- Azure Cosmos DB
- GitHub for source control and deployment

## Features

- Responsive resume website
- Visitor counter
- Serverless backend API
- Persistent data storage with Cosmos DB
- Cloud deployment through Azure

## How It Works

1. A visitor opens the resume website.
2. JavaScript on the frontend sends a request to `/api/visitor-count`.
3. The Azure Function reads and updates the visitor count in Cosmos DB.
4. The updated count is returned and displayed on the page.

## Tech Stack

- HTML
- CSS
- JavaScript
- Python
- Azure Static Web Apps
- Azure Functions
- Azure Cosmos DB

- JavaScript
- Python
- Azure Static Web Apps
- Azure Functions
- Azure Cosmos DB

## Project Structure
text
.
├── .github/
├── api/
│ ├── VisitorCount/
│ │ ├── __init__.py
│ │ └── function.json
│ ├── host.json
│ └── requirements.txt
├── .gitignore
├── index.html
├── main.js
├── styles.css
└── README.md

## Local Development

1. Clone the repository
2. Install dependencies
3. Run the project locally
4. Start the API locally for testing

## Configuration

The following settings are required in Azure:

- COSMOS_ENDPOINT
- COSMOS_KEY
- COSMOS_DATABASE_NAME
- COSMOS_CONTAINER_NAME

Do not store secrets in the repository.

## Deployment

This project is deployed through Azure Static Web Apps connected to GitHub.

## Lessons Learned

- Building and deploying a full-stack serverless app in Azure
- Connecting Azure Functions to Cosmos DB
- Debugging frontend/backend integration issues
- Working with CORS and cloud environment configuration
## Live Demo

[https://red-smoke-066d40b1e.4.azurestaticapps.net/]


