# BarainerHub Practical Task
This repo is the solution for the Practical task given by BrainerHub Solution. The description of the problem is as follows.

## Problem Statement
1. Create an API in Python which will read from an Excel/CSV file and insert
data into the database. (you can use any Python framework of your
choice).
2. For the database, you need to create two table: Employee and Company. (You
can use any database of your choice).
3. You need to establish one-to-many relationships between the Company and
Employee table where one company can have multiple employees.
4. The Excel file provided with this task has Employee details mentioned like
first_name, last_name, phone_number, etc.
5. From the Excel file, you need to store the company_name in the "Company"
table and use its id as a foreign key in the Employee table.
6. The API you will create should read this Excel file with serializers and
insert the data into both the table without using any "SQL" or "ORM" query
in the loop.

## Steps to implement: 
1. Clone the repo and change the current working directory to brainerhub:
```
git clone https://github.com/LSRAO/brainerhub.git
cd brainerhub
```

2. Set-up virtual environment:
  * The repo already includes the virtual Env for Python 3.12, which can be used by activating it:
```
source .venv/bin/activate
```
  * Otherwise, a new Virtual environment can be set up:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Start the FastAPI server:
```
uvicorn app.main:app --reload
```
4. Test the API:
* Send a POST request to the /upload/ endpoint with the path to the Excel file.
* If you are testing on a browser, the POST method can be found in [Docs in fastAPI](http://127.0.0.1:8000/docs).
  


