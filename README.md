# API Performance Challenge - PetStore - OpenAPI 3.0

Proposed Test cases for Automation:
----------------------

I consider the most impacting scenarios regarding the performance were the followings:

**Pets**
1. Create a new pet (POST)
2. Delete an existing Pet (DELETE)
3. Get a pet detail by its ID (GET)
4. Get all pets by status (GET)
5. Get all pets by tags (GET)

**Users**
1. Create a new user (POST)
2. Delete an existing user (DELETE)
3. Get a user detail by its username (GET)
4. Log in user (GET)

```Note: Testing for store could not be implemented due to time issues. I have attached the execution report with 30 users```

Setup Instructions (Macbook)
----------------------

1. Install pyenv(https://github.com/pyenv/pyenv#installation)

2. Install Python 3.10 or higher. Make sure you have previously installed the python version in this case 3.10.0. you can use the following command:

```bash
$ pyenv versions
```

3. In case you don't have the specific version you can install it using

```bash
$ pyenv install 3.10.0
```

### Test Project Setup

Let's set up the test project! For this tutorial
1. Create a directory for the project with the name you prefer:

```bash
$ mkdir <project name>
$ cd <project name>
```

2. Set up the virtual environment ( it is recommended to use pyenv-virtualenv for this)

```bash
$ pyenv virtualenv 3.10.0 <virtualenv name>
```

**Note**: you can use `venv` or the name you want

3. After creating a virtual environment, you must "activate" it.
On macOS or Linux, use the following command:

```bash
$ pyenv activate <virtualenv name>
```

4. To install necessary packages you have to execute the command on the root to install the dependencies

```bash
$ pip install -r requirements.txt
```

Execute Performance testing with locust

1. Execute the following command: ```locust -f petstore_load.py```

2. Go on 'http://0.0.0.0:8089' link in the console to open the Locust in the Browser

3. Set up the configuration as following:
   - Number of users: Numbers of users o simulate
   - Ramp up: Number of users started/second
   - Host: http://localhost:8080/api/v3
   - Click on the Start button


### Author
- Carlos Andres Jaramillo