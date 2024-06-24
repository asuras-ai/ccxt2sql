# CCXT2SQL

## Overview

CCXT2SQL is a project to store OHLCV data from various cryptocurrency exchanges using CCXT into a PostgreSQL database. The project includes a simple web interface to manage which exchanges, tickers, and timeframes to store in the database.

## Project Structure

- `backend`: Contains the backend code to fetch and store data.
- `frontend`: Contains the frontend code for the web interface.
- `docker-compose.yml`: Configuration file to run the application using Docker Compose.

## Setup and Deployment

### Prerequisites

- Docker
- Docker Compose

### Step-by-Step Deployment

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/ccxt2sql.git
   cd ccxt2sql

2. **Configure the environment variables:**

   Create a `.env` file in the root of the project directory and add the following content:

   ```env
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   POSTGRES_DB=ohlcv
   DB_URL=postgresql://user:password@db/ohlcv

3. **Build and start the Docker containers:**

    ```sh
   docker-compose up --build
    ```
    This command will:

    - Build the backend Docker image and start the container.
    - Build the frontend Docker image and start the container.
    - Pull the PostgreSQL image and start the container with the specified environment variables.

4. **Access the web interface:**

    Open your web browser and navigate to http://localhost:3000. You should see the CCXT2SQL web interface.

5. **Add exchanges, tickers, and timeframes:**

    Use the web interface to add the exchanges, tickers, and timeframes you want to store in the database.

### Database Credentials
The username and password for the PostgreSQL database are defined in the `.env` file as `POSTGRES_USER` and `POSTGRES_PASSWORD`. These values are used by the PostgreSQL container and are also included in the `DB_URL` environment variable for the backend service to connect to the database.

## Initial Data Import and Daily Updates
- The backend service will automatically run an initial import of historical OHLCV data based on the exchanges, tickers, and timeframes you add through the web interface.
- The backend service will also schedule a daily update to fetch and store the latest OHLCV data.

## Technologies Used
- Python
- CCXT
- TimescaleDB
- React
- Docker
- Docker Compose

## Troubleshooting
- If you encounter issues with the database connection, ensure that the `DB_URL` in the `.env` file matches the `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` values.
- Check the logs of the Docker containers for any error messages:
```sh
docker-compose logs backend
docker-compose logs frontend
docker-compose logs db
```

## Conclusion
With these steps, you should have a fully functional deployment of the CCXT2SQL project, allowing you to fetch and store OHLCV data from various cryptocurrency exchanges into a Timescale database, managed through a web interface.


