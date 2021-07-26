#  NEIGHBORHOOD

#### Author: [Kiptoo Rotich](https://github.com/kiptoo-rotich)

## Screenshot
### Landing page/Chats
![chathome](https://user-images.githubusercontent.com/48821300/127058737-4f98b499-009a-4ff7-8b83-83673ebdeff0.png)

### Profile
![profile](https://user-images.githubusercontent.com/48821300/127058825-4ba4d01d-f519-4074-a341-883cf9b058b1.png)

### Businesses
![business](https://user-images.githubusercontent.com/48821300/127058890-dab18a49-a54c-4621-bf3e-d69759626bea.png)

### Neighborhood
![neigh](https://user-images.githubusercontent.com/48821300/127058960-6b5bf561-c79b-4e15-bd03-6d847a29025d.png)

### Search results
![search](https://user-images.githubusercontent.com/48821300/127059026-015a4da9-e6a5-402c-b2c4-4cf33f1ef2cc.png)


## Description
This application allow neigbor to share their thoughts and know businesses within their neigborhood

As a user of the web application you will be able to:

1. Sign up and log in
2. Post business
3. View posted businesses and chats
4. Edit your profile
5. Search for a business


## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`
* Access the live site using the local host provided
* Create your superuser account `python manage.py createsuperuser` inside virtual environment.
* Add data from admin dashboard

## End points
```bash
https://github.com/kiptoo-rotich/neighborhood/
```

## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip
* postgresql
  

#### Clone the Repo and rename it to suit your needs.
```bash
git clone `https://github.com/kiptoo-rotich/neighborhood`
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='gallery'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.8 manage.py check
python manage.py makemigrations news
python3.8 manage.py sqlmigrate news 0001
python3.8 manage.py migrate
```

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test myhood`
        
## Built With

* [Python3.8](https://docs.python.org/3/)
* Django==3.2.5
* Postgresql 
* Boostrap
* HTML
* CSS


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license)