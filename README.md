# <div align="center">CP317 - Fall 2021 - Restaurant Management System</div>

---

<p>Getting Started</p>

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
    $source venv/bin/activate
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

