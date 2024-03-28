# ZED

A minimal clone of X (Twitter) with most of the features of the original service.

## Screenshots

Click [here](https://github.com/EngRobot33/ZED/blob/master/screenshots/Screenshots.md) for viewing the application screenshots!

## Installation

* First of all clone the project:
```
git clone https://github.com/EngRobot33/ZED.git
```
* Then, we need a virtual environment you can create like this:
```
virtualenv venv
```
* Activate it with the command below:
```
source venv/bin/activate
```
* After that, you must install all the packages in `requirements.txt` file in project directory:
```
pip install -r requirements.txt
```
* You should install PostgreSQL and its dependecies:
  ```shell
  sudo apt update
  sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
  ```
* Now setup your database in PostgreSQL shell:
  * Open PostgreSQL shell:
    ```shell
    sudo -u postgres psql
    ```
  * Create database:
    ```sql
    CREATE DATABASE <database_name>;
    ```
  * Create user:
    ```sql
    CREATE USER <database_user> WITH PASSWORD '<database_password>';
    ```
  * Grant all privileges to zed database user:
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <database_user>;
    ```

* Create a `.env` file in root directory and add your created config like `.env.sample`:
```python
SECRET_KEY = 'Your secret key generated by https://djecrety.ir'
DEBUG = 'Project debug status'
ALLOWED_HOSTS = 'Host/Domain names list that this site can serve for e.g ['*'] allows all hosts'

DB_NAME = '<database_name>'
DB_USER = '<database_user>'
DB_PASS = '<database_password>'
DB_HOST = '<database_host>'
DB_PORT = '<database_port>'
```
* After that, migration:
```
python3 manage.py migrate
```
* Then make sure that Redis is actually running on your machine:
```
redis-server
```
* Now you should install all the packages in `package.json` file. Just make sure npm is installed:
```
npm install
```
* That's finished! Now you can run the project:
```
python3 manage.py runserver
```
## Run with docker
* You need to [install docker](https://docs.docker.com/get-docker/)
  
 
  

* Then clone the project:
```
git clone https://github.com/EngRobot33/ZED.git
```
* Create a `.env` file in root directory and add your created config like `.env.sample`:
```python
SECRET_KEY = 'Your secret key generated by https://djecrety.ir'
DEBUG = 'Project debug status'
ALLOWED_HOSTS = 'Host/Domain names list that this site can serve for e.g ['*'] allows all hosts'
```

* That's finished! Now you can run the project:
```
docker compose up -d 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
