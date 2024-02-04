# Password App

## Introduction
This is a simple Flask-based password management app that provides various API endpoints for password-related functionalities. The app includes features like generating strong passwords, encrypting passwords using the SHA256 algorithm, checking the strength of a password, and matching provided passwords against stored hashed passwords.

## Getting Started
To run the app locally, follow these steps:

### Prerequisites
- Python installed on your machine.
- Flask and required libraries installed. You can install them using:
  ```
  pip install Flask
  ```

### Running the App
1. Clone the repository.
2. Navigate to the project directory in your terminal.
3. Run the following command to start the Flask server:
   ```
   python -m flask run
   ```

## API Endpoints

### 1. Generate a Strong Password
- **Endpoint:** `/`
- **Method:** GET
- **Description:** Generates a new strong password.
- **Example:** `GET /` returns a JSON object with the generated password.

### 2. Encrypt Password
- **Endpoint:** `/encrypt/`
- **Method:** POST
- **Description:** Encrypts a password using the SHA256 algorithm.
- **Parameters:**
  - `password` (string): The password to be encrypted.
- **Example:** 
  - Request: `POST /encrypt/` with JSON body `{"password": "your_password"}`
  - Response: JSON object with the encrypted password.

### 3. Validate Password Strength
- **Endpoint:** `/validate`
- **Method:** POST
- **Description:** Checks the strength of a given password.
- **Parameters:**
  - `password` (string): The password to be validated.
- **Example:**
  - Request: `POST /validate` with JSON body `{"password": "your_password"}`
  - Response: JSON object with the validation result.

### 4. Check Matched Password
- **Endpoint:** `/match/`
- **Method:** POST
- **Description:** Checks if the provided password matches the stored hashed password.
- **Parameters:**
  - `stored_password` (string): The stored hashed password.
  - `provided_password` (string): The password provided for matching.
- **Example:**
  - Request: `POST /match/` with JSON body `{"stored_password": "hashed_password", "provided_password": "your_password"}`
  - Response: JSON object with the match result.

## Notes
- Always store hashed passwords securely in your database.
- Ensure proper error handling for API requests.

## Disclaimer
This app is a basic demonstration and should not be used in a production environment without thorough security considerations and testing. Always follow best practices for password management and security.
