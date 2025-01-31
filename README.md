# THIS IS LIBRARY MANAGEMENT PROJECT

## 1-step 
Clone project from github
`git clone https://github.com/OgabekMurodullaev/bookly.git`

## 2-step
Enter the project directory

## 3-step 
Create a virtual environment
`python3 -m venv .venv`

## 4-step
Activate virtual environment
For Linux: `source .venv/bin/activate`
For Windows: `.venv\Scripts\activate`

## 5-step
Create Database in your local machine
``` 
- psql
- CREATE DATABASE bookly;
- CREATE USER bookly WITH PASSWORD 'bookly';
- ALTER ROLE bookly SET client_encoding TO 'utf8';
- ALTER ROLE bookly SET default_transaction_isolation TO 'read committed';
- ALTER ROLE bookly SET timezone TO 'UTC';
- GRANT ALL PRIVILEGES ON DATABASE bookly TO bookly; 
```

## 6-step
Generate a secret key
```
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## 7-step
Create `.env` file and paste all credentials that copied from `.env.example` like below, put in above generated secret key to `SECRET_KEY` variable

```
# Base Configuration
SECRET_KEY=key
DEBUG=True
ALLOWED_HOSTS=127.0.0.0.1, localhost

# Database Configuration
DB_NAME=e_commerce
DB_USER=e_commerce
DB_PASSWORD=e_commerce
DB_HOST=localhost
DB_PORT=5432
```
## 8-step
Install all requirements
```
pip install requirements.txt
```

## 9-step 
Migrate the database

## 10-step
Create superuser
```
python manage.py createsuperuser
```

## 11-step 
Run the project
```
python manage.py runserver
```


