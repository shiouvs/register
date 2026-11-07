# User Registration System

A comprehensive registration system with:
- Java Spring Boot backend
- MySQL database
- Optional Python utilities for data processing

## Setup Instructions

1. **MySQL Database Setup**:
   ```sql
   CREATE DATABASE user_registration;
   USE user_registration;
   CREATE TABLE users (
     id INT AUTO_INCREMENT PRIMARY KEY,
     username VARCHAR(50) NOT NULL UNIQUE,
     email VARCHAR(100) NOT NULL UNIQUE,
     password VARCHAR(255) NOT NULL,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

2. **Java Backend**: Spring Boot application with REST API endpoints

3. **Python Utilities**: Optional scripts for data validation and processing

## API Endpoints
- POST `/api/register` - Register a new user
- GET `/api/users` - Get all users
- GET `/api/users/{id}` - Get user by ID

## Running the Application
1. Start MySQL server
2. Run the Spring Boot application
3. Use Python utilities as needed
