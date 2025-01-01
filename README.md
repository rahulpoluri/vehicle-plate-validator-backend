# Vehicle Plates Storage System

A backend application built with FastAPI to use with vehicle monitoring and surveillance systems in recording German vehicle plate numbers with timestamps at intersections.

---

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [APIs Provided](#apis-provided)
4. [Technologies and Tools Used](#technologies-and-tools-used)
5. [Project Structure](#project-structure)
6. [Requirements/Prerequisites](#requirementsprerequisites)
7. [Installation](#installation)
8. [Usage](#usage)
9. [Roadmap](#roadmap)
10. [License](#license)
11. [Contact](#contact)

---

## Description

This FastAPI-based backend supports vehicle monitoring systems by recording German vehicle plate numbers passing through intersections along with timestamps. It includes authentication and authorization to ensure secure API interactions.

---

## Features

- **Store Valid German Vehicle Plate Numbers**: Accepts inputs from humans or detection devices.
- **Search and Query**: Perform fuzzy searches to retrieve vehicle plate data and timestamps.
- **Authentication & Authorization**: Secure access with token-based authentication.

---

## APIs Provided

| Method | Endpoint             | Description                                   |
|--------|----------------------|-----------------------------------------------|
| GET    | `/plates`            | Retrieve vehicle plate numbers with timestamps. |
| POST   | `/plates`            | Store vehicle plate numbers and their timestamps. |
| POST   | `/token`             | Obtain a token for authentication.            |
| POST   | `/users`             | Create new users.                             |
| DELETE | `/users`             | Delete existing users.                        |
| PATCH  | `/password`   | Update user passwords.                        |

**API Documentation**: [Swagger UI](http://localhost:80/docs) can be accessed after running the application.

---

## Technologies and Tools Used

- **Programming Language**: Python
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **Cache**: Redis
- **Package Manager**: Poetry
- **Containerization**: Docker
- **Reverse Proxy**: Nginx
- **ORM**: SQLAlchemy with Alembic for migrations
- **Testing**: Pytest
- **Linting and Code Quality**: Black, Flake8, Isort, MyPy
- **CI/CD**: GitHub Actions
- **Authentication**: FastAPI JWT Auth
- **Environment Management**: python-dotenv

---

## Project Structure

```
.
├── Dockerfile
├── LICENSE
├── README.md
├── application
│   ├── auth.py
│   ├── config.py
│   ├── db
│   │   ├── migrations
│   ├── routes
│   ├── schemas
│   └── scripts
├── docker
├── docker-compose.yml
├── pyproject.toml
└── tests
```

---

## Requirements/Prerequisites

Ensure the following are installed:
- Docker & Docker Compose ([Installation Guide](https://docs.docker.com/engine/install/))

---

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/rahulpoluri/vehicle-plate-validator-backend.git
    cd vehicle-plate-validator-backend
    ```

2. **Install Poetry**
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Install Dependencies**
    ```bash
    poetry install
    ```

4. **Set Up Environment Variables**  
   Create a `.env` file and configure as follows:
    ```bash
    SECRET_KEY=secret
    ALGORITHM=HS256
    REDIS_URL=redis://redis:6379/0
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=password
    POSTGRES_DB=vehicle-plates
    DATABASE_URL=postgresql://postgres:password@db:5432/vehicle-plates
    JWT_ALGORITHM=HS256
    TOKEN_EXPIRY_MINUTES=60
    SUPER_ADMIN_USER_NAME=superadmin
    SUPER_ADMIN_PASSWORD=superadminpassword
    ```

5. **Run the Application**
    ```bash
    docker-compose up --build
    ```

**Access Application**: [http://localhost:80](http://localhost:80)  
**API Documentation**: [Swagger UI](http://localhost:80/docs)

---

## Usage

### User Roles

1. **Superadmin**: Manages admins. Limited API access.  
2. **Admin**: Creates and manages users. Full API access.  
3. **User**: Reads vehicle data.  
4. **Machine**: Writes vehicle data.

On first startup, a `superadmin` user is created with credentials from `.env`.  

**Basic Workflow**:
1. Superadmin creates an admin.
2. Admin changes the password and creates users.
3. Users/Machines interact with the API using tokens.

---

## Roadmap

1. Enhance role-based permissions.
2. Add Redis caching for repeated queries.
3. Implement comprehensive test coverage.
4. Introduce monitoring, logging, and health checks.
5. Deploy using Kubernetes with CI/CD pipelines.
6. Improve scalability with async DB and Redis.

---

## License

Licensed under the Apache License. See [LICENSE](LICENSE) for details.

---

## Contact

For queries or suggestions, reach out at:  
**Email**: rahul.poluri1306@gmail.com  

---