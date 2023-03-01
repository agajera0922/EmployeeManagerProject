# **Employee Manager Project**

This project is a Django-based employee management system that allows users to view employees and their managers.

## Installation

1. Clone the repository to your local machine.
2. Change into the project directory:
- **cd EmployeeManagerApp**
3. Create and activate a virtual environment (optional):
- **python -m venv env**
- **source env/bin/activate**
4. Install the necessary dependencies by running the following commands:
- **pip install django**
- **pip install djangorestframework**

## To start the development server, run the following command:

- **python manage.py runserver**
- You can access server at http://127.0.0.1:8000/

## Available Endpoints

1. **/admin:** Provides a built-in web-based interface for site administrators to manage site content and user accounts.You can access the admin page at http://127.0.0.1:8000/admin.
2. **/employee/relationship:** Displays the employee and corresponding manager of all employees. You can access the employee management system at http://127.0.0.1:8000/employee/relationship.

## Database Commands

1. Run the following command to open the SQLite3 shell and connect to the database:
- **sqlite3 db.sqlite3** (Enter ".help" for usage hints.)

2. Run database migrations with the following command:
- **python manage.py migrate**

3. Run database new migration files based on the changes made to the models
- **python manage.py makemigrations**

## Running the tests
To run the automated tests for this system, run the following command:
- **python manage.py test**

This will execute all the tests in the tests.py file and output the results to the console. If any tests fail, you will see detailed error messages explaining why the test failed.

