# Algorithmic Financial Processing Pipeline

## Overview

This project implements a backend service for processing company financial data and calculating financial metrics using FastAPI and MySQL.

## Features

* REST API built using FastAPI
* Company financial data stored in MySQL
* Financial leverage ratio calculation
* SQLAlchemy ORM for database interaction
* Interactive API documentation using Swagger

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* MySQL
* Uvicorn

## API Endpoints

### Create Company

POST `/api/v1/companies`

### Get Company Leverage

GET `/api/v1/companies/{company_id}/leverage`

## Run the Project

Install dependencies:

```
pip install -r requirements.txt
```

Start the server:

```
python -m uvicorn main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```
