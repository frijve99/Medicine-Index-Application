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
```


Navigate to the project directory:
```bash
cd Medicine-Index-Application/medicineIndex
```

Create a MySQL database for the project.

Set up the database configuration in settings.py:

```python
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
```
Make migrations and migrate the database:
```python
python manage.py makemigrations
python manage.py migrate
```
Create a superuser:
```python
python manage.py createsuperuser
```
Run the development server:
```python
python manage.py runserver
```

# Features

**Medicine Listing**: Users have access to a comprehensive catalog of medicinal products within the system. Each medicine entry meticulously presents details such as name, generic name, manufacturer, description, price, and batch number, offering users a thorough understanding of available options.

**Search Functionality**: Our robust search feature enables users to efficiently locate specific medicines by utilizing keywords matching either the medicine name or generic name. Search results are meticulously presented in a user-friendly manner, facilitating swift navigation. Keywords are thoughtfully highlighted to expedite the search process.

**User Roles and Permissions**: 
- **Public Users**: Public users are granted the ability to peruse and search for medicines, providing an opportunity for exploration and inquiry.
- **Logged-in Users (Admins)**: Admins hold elevated privileges and are equipped to conduct all CRUD (Create, Read, Update, Delete) operations on medicine records. This includes managing inventory, updating information, and ensuring database integrity.

**Technologies Used**: The Medicine Index Application leverages a suite of advanced technologies, including Django, Python, HTML, CSS, JavaScript, and Bootstrap. These technologies collectively contribute to the application's sophisticated user interface and seamless functionality.

Feel free to explore the Medicine Index Application at your convenience. Should you have any inquiries or require further assistance, our team remains at your disposal to provide support and guidance.

