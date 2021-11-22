# <div align="center">CP317 - Fall 2021 - Restaurant Management System<br>[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/mBuilt/restaurant-management-system/blob/main/LICENSE)</div>

## Table of Contents

- [About](#about)
- [Dependencies](#dependencies)
- [Getting Started](#getting_started)
<br>

## About <a name = "about"></a>
Web-application based, handles all of the basic operating functions of a restaurant.
<br>

## Dependencies <a name = "dependencies"></a>
Languages:
- Python
- SQL
- HTML
- CSS

Python Packages:
- [Django 3.2.9](https://www.djangoproject.com/)
- [Pillow 8.4.0](https://pillow.readthedocs.io/en/stable/)

SQL:
- [SQLite3](https://sqlite.org/index.html)

<br>

## Getting Started <a name = "getting_started"></a>

- Download & extract the files to a specified directory

- In your terminal (powershell for windows) cd (short for change directory) into that specified directory

    ```
    $ cd your\path\to\specified\directory
    ```

- Create the virtual environment:
   
    ```
    $ virtualenv venv
    ```

- Access the virtual environment:
    
    ```
    // Windows
    $ venv/Scripts/activate

    //Linux or MacOS
    $ source venv/bin/activate
    ```

- Install dependencies:

    ```
    $ pip install -r requirements.txt
    ```

- Running the application:

    ```
    $ python manage.py migrate
    $ python manage.py runserver
    ```

- Access the site via localhost [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

- Access Admin panel via [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
    
    ```
    user: admin
    pass: 12345
    ```
<br>

