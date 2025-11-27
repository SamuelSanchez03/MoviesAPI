# Movies API — FastAPI + PostgreSQL + SQLAlchemy

A REST API built with **FastAPI** to provide movie categories and related movies. The database is hosted on **PostgreSQL (Render)**, and the API is intended to be consumed by a **React Native mobile application**.

---

## Features

* FastAPI backend
* PostgreSQL on Render as the database
* SQLAlchemy ORM
* Modular architecture
* Endpoints for:

  * Listing categories
  * Getting a category by ID
  * Listing movies by category
  * Listing all movies
  * Getting a movie by ID

---

## Project Structure

```
app/
│── __init__.py
│── main.py
│── models.py
│── schemas.py
│── crud.py
│
├── database/
│   ├── __init__.py
│   └── database.py
│
└── routers/
    ├── __init__.py
    ├── categories.py
    └── movies.py
```

---

## Database Tables

### categories

* id
* name
* icon

### movies

* id
* title
* year
* image
* description
* director
* imdb_score
* rating
* category_id (foreign key)

---

## Setup

### 1. Clone the repository

```
git clone https://github.com/SamuelSanchez03/MoviesAPI.git
cd MoviesAPI
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Create a `.env` file

```
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=5432
DB_NAME=your_database
DB_SSLMODE=require
```

---

## Running Locally

```
uvicorn app.main:app --reload
```

---

## Endpoints

### Categories

| Method | Route                     | Description                |
| ------ | ------------------------- | -------------------------- |
| GET    | `/categories/`            | Get all categories         |
| GET    | `/categories/{id}`        | Get a category by ID       |
| GET    | `/categories/{id}/movies` | Get movies from a category |

### Movies

| Method | Route          | Description       |
| ------ | -------------- | ----------------- |
| GET    | `/movies/`     | Get all movies    |
| GET    | `/movies/{id}` | Get a movie by ID |

---

## Local Testing

Base URL:

```
http://127.0.0.1:8000
```

Example requests:

* `/categories/`
* `/categories/1/movies`
* `/movies/`
* `/movies/5`

---

## Technologies Used

* Python 3.10+
* FastAPI
* SQLAlchemy
* PostgreSQL
* Uvicorn
* Pydantic v2
