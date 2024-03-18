
# Dental-Delight

Dental-Delight is a simple dental management website that uses a CRUD (Create, Read, Update, Delete) system. 

Dentists or their receptionists can use this web app to store patient information and schedule appointments. 

Additionally, it can manage dental office staff members and assign one or more of them to each appointment.


## Screenshots

![App Screenshot](/screenshots/screenshot1.png)
![App Screenshot](/screenshots/screenshot2.png)
![App Screenshot](/screenshots/screenshot3.png)
![App Screenshot](/screenshots/screenshot4.png)
![App Screenshot](/screenshots/screenshot5.png)
![App Screenshot](/screenshots/screenshot6.png)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

In case you are running locally, you should just set

`DEBUG = TRUE`

However, in case you want to host the website you might need the following variables for the Email Confirmation functionality to work. 

`DEBUG = FALSE`
`EMAIL_HOST_USER = {YOUR SMTP EMAIL HOST USER}`
`EMAIL_HOST_PASSWORD = {YOUR SMTP EMAIL HOST PASSWORD}`


## Installation

Install the requirements with

```bash
pip install -r requirements.txt
```

Migrate with 
```bash
python3 manage.py migrate
```

Run with 
```bash
python3 manage.py runserver
```