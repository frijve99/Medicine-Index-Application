# Medicine-Index-Application


Welcome to the Medicine Index Application! This Django project allows users to manage and view information about various medicines. Below is a guide on how to set up and use the project.

Installation
Before running the project, ensure you have the following installed:

Python
Django
MySQL client
Setup
Clone the project repository:

```bash
git clone https://github.com/frijve99/Medicine-Index-Application.git
```bash


Navigate to the project directory:
```bash
Copy code
cd Medicine-Index-Application/medicineIndex
```bash

Create a MySQL database for the project.

Set up the database configuration in settings.py:

```python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```python
Make migrations and migrate the database:
```python
Copy code
python manage.py makemigrations
python manage.py migrate
```python
Create a superuser:
```python
Copy code
python manage.py createsuperuser
```python
Run the development server:
```python
Copy code
python manage.py runserver
```python

#Features

**Medicine Listing:**
Users can view a list of all medicines in the system.
Each medicine entry displays details such as name, generic name, manufacturer, description, price, and batch number.

**Search Functionality:**
Users can search for medicines using keywords matching either the medicine name or generic name.
Search results are displayed in a user-friendly manner, highlighting matched keywords.

**User Roles and Permissions:**
Public Users:
Can view and search for medicines.

Logged-in Users (Admins):
Can perform all CRUD (Create, Read, Update, Delete) operations on medicine records.



Technologies Used
Django
HTML
CSS
JavaScript
Bootstrap


Feel free to explore and enjoy using the Medicine Index Application! If you have any questions or need further assistance, don't hesitate to reach out.
