# UWin Rent Server

*The instructions are for unix based OS's*

## Technologies overview
* Ariadne - Graphql
* Flask - Web Server
* Gunicorn - Reverse Proxy Entry Point

## How to run

### Requirements
* python 3.8+
* pyvenv
* pip

#### Update Requirements

run `pip freeze > requirements.txt`

### Install Requirements

run `pip3 install -r requirements.txt`


### Setup

1. cd into `<MAIN>/server`
   
   run `cd ./server`

* Create venv(optional but reccomeneded for dev)

  * create `<MAIN>/server/venv`
   
    run `mkdir ./venv`
 
  * create venv 
  
    run `python3 -m venv ./venv/`
 
  * activate venv 
    
    run `source ./venv/bin/activate` 
   
2. Install the dependencies

   run `pip3 install -r requirements.txt`

3. Actually run the code
   
   run `gunicorn --bind 127.0.0.1:5000 wsgi:app`
   

### Migrate

1. cd into `<MAIN>/server`
   
   run `cd ./server`
   
2. Initial database

   run `flask db init`

3. Migrate database

   run `flask db migrate`

4. Upgrade database

   run `flask db upgrade`
