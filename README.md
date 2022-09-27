### PART 4 Of the Assignment

# 1) why I opted for Django
- a)
    - Pros
        - It's mainly based on Django's ORM. Giving that python itself is primarily based on OOP, Django was a wise choice.
        - Django is a full-stack framework. If in the feature, one decides to build a client application for this project, Django will suffice.
        - Django admin is quite a handy dashboard.
        - It is the python framework I am most familiar with.
    - Cons
        - It can be an overkill for small projects.
        - relatively heavyweight compared to its counterpart, flask.

- b)
    - It provides multiple built-in methods for database relationships.
    - there are multiple helpful third-part libraries build specifically for it.
    - Excellent documentation.


# 2) Potential improvement
    - I'll use oauth 2.0 to validate all api requests. I'll provide a client_id and access tokens to authorized frontend applications to make requests. 
        https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/rest-framework.html
    - I'll add permission_classes to all api endpoint.
    - if possible, re-write the operating_hours model. This will allow different doctors to occupy weekdays they have in common, even if they have different working hours. It'll also make the admin dashboard look cleaner.
    - Expand serializer validations.
    - Use factory_boy library and fuzzy attributes to build dummy models. It'll also allow me to write more objective tests. 
        (https://factoryboy.readthedocs.io/en/stable/orms.html)
    - Write negative tests. For example, run a bad 'POST' request and verify that it is BadRequest.
    - Write more than the 6 test cases I currently have.
    - Test calling my API endpoints using different languages.
    - Dockerize the project to save the next developer time.
    - Perhaps space out my git commits, rather than commiting large and different changes all at once.


# 3) Production consideration
    - I have adjusted the settings.py file to allow for environment variables configuration. Please refer to 'dev-example.env' to find the environment variables for this project.
    - Please use postgres because the database setting is currently configured for it.
    - Always set DEBUG=False in production.
    - A custom domain name can be added to 'ALLOWED_HOSTS' during deployment to production. 
    - Remember to run the collecstatic command (python3 manage.py collecstatic). If you are considering deploying the application in an EC2 instance, add a container command under in the '.evextensions' directory/commands.config.
    - Apply all migrations to setup your database tables.
    - Please add all sensitive informations to your environment variables.
    - If you plan to deploy this application to an EC2 instance on AWS, please consider an S3 bucket to handle your media and static files. 


# 3) Assumptions
- a)
    - Every Doctor belongs to one category.
    - Every Doctor operates in one district.
    - A doctor may be able to offer his/her services in multiple languages.
    - Multiple doctors may speak similar language(s).
    - Every doctor has his/her own operating hours. 

- b)
    - Time to learn a second language, Mandarin perhaps.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

### HOW TO RUN THIS PROJECT

# Prerequisites
    - python 3.10
    - pipenv
    - postgres

# Steps
    - Navigate to the directory containing the Pipfile
    - check your python and your pip version.
        (python --version & pip --version) 
    - install pipenv 
        (pip install pipenv)
    - install all the packages from the Pipfile
        (pipenv install)
    - run the application
        (python manage.py runserver / python3 manage.py runserver)


--------------------------------------------------------------------------------------------------------------------------------------------------------------------
### API Documentation

# Get list of doctors
    url = doamin_name/doctor
    body_type = json
    request_method_type = GET
    response_success_code = 200

    response_body_example = [
        {
            "id": "9f8eec21-84a2-4534-b7b6-028fe8e95e98",
            "name": "Yusuf hamdan",
            "address": "new york",
            "postcode": "631000",
            "email": "sedia.jaiteh@ymail.com",
            "price": "5400.00",
            "consultation_fee": "400.00",
            "consultation_fee_description": "No extra add-ons",
            "district_name": {
                "id": 41,
                "name": "Jalan Ampan"
            },
            "language": [
                {
                    "id": 63,
                    "name": "Arabic"
                },
                {
                    "id": 64,
                    "name": "English"
                }
            ],
            "category": {
                "id": 47,
                "name": "Obgyn"
            },
            "operating_hours": [
                {
                    "if_public_holiday": true,
                    "weekday": 1,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 2,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 3,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 4,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 5,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 6,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 7,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                }
            ]
        },
        {
            "id": "4729e2c7-f699-488d-8571-ee872f96e118",
            "name": "Abu Mohamed",
            "address": "new york",
            "postcode": "631000",
            "email": "sedia.jaiteh@horizons45.com",
            "price": "5400.00",
            "consultation_fee": "400.00",
            "consultation_fee_description": "No extra add-ons",
            "district_name": {
                "id": 42,
                "name": "Dengkil Valley"
            },
            "language": [
                {
                    "id": 64,
                    "name": "English"
                },
                {
                    "id": 65,
                    "name": "Turkish"
                }
            ],
            "category": {
                "id": 48,
                "name": "Cardiologits"
            },
            "operating_hours": [
                {
                    "if_public_holiday": true,
                    "weekday": 1,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 2,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 3,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 4,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 5,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 6,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                },
                {
                    "if_public_holiday": true,
                    "weekday": 7,
                    "open_time": "06:00:00",
                    "close_time": "21:00:00"
                }
            ]
        }
    ]
--------------------------------------------------------------------

# Get a specific doctor using his/her id
    url = doamin_name/doctor/id
    request_method_type = GET
    body_type = json
    response_success_code = 200

    request_url_example = doctor/9f8eec21-84a2-4534-b7b6-028fe8e95e98
    response_body_example = {
        "id": "9f8eec21-84a2-4534-b7b6-028fe8e95e98",
        "name": "Yusuf hamdan",
        "address": "new york",
        "postcode": "631000",
        "email": "sedia.jaiteh@ymail.com",
        "price": "5400.00",
        "consultation_fee": "400.00",
        "consultation_fee_description": "No extra add-ons",
        "district_name": {
            "id": 41,
            "name": "Jalan Ampan"
        },
        "language": [
            {
                "id": 63,
                "name": "Arabic"
            },
            {
                "id": 64,
                "name": "English"
            }
        ],
        "category": {
            "id": 47,
            "name": "Obgyn"
        },
        "operating_hours": [
            {
                "if_public_holiday": true,
                "weekday": 1,
                "open_time": "06:00:00",
                "close_time": "21:00:00"
            },
            {
                "if_public_holiday": true,
                "weekday": 2,
                "open_time": "06:00:00",
                "close_time": "21:00:00"
            },
            {
                "if_public_holiday": true,
                "weekday": 3,
                "open_time": "06:00:00",
                "close_time": "21:00:00"
            },
            {
                "if_public_holiday": true,
                "weekday": 4,
                "open_time": "06:00:00",
                "close_time": "21:00:00"
            },
            {
                "if_public_holiday": true,
                "weekday": 5,
                "open_time": "06:00:00",
                "close_time": "21:00:00"
            },
            {
                "if_public_holiday": true,
                "weekday": 6,
                "open_time": "06:00:00",
                "close_time": "21:00:00"
            },
            {
                "if_public_holiday": true,
                "weekday": 7,
                "open_time": "06:00:00",
                "close_time": "21:00:00"
            }
        ]
    }
------------------------------------------------------------

# Create one or more doctors

    url: doamin_name/doctor/
    request_method_type = POST
    body_type = json
    response_success_code: 201

    request_body_example = [
        {
            "name": "Yusuf hamdan",
            "address": "new york",
            "postcode": "631000",
            "email": "sedia.jaiteh@ymail.com",
            "price": "5400",
            "consultation_fee": "400",
            "consultation_fee_description": "No extra add-ons",
            "language": [
                {
                    "name": "Arabic"
                },
                {
                    "name": "English"
                }
            ],
            "category": {
                "name": "Obgyn"
            },
            "district_name": {
                "name": "Jalan Ampan"
            },
            "operating_hours": [
                {
                    "if_public_holiday": "True",
                    "weekday": "1",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "2",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "3",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "4",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "5",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "6",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "7",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                }
            ]
        },
            {
            "name": "Abu Mohamed",
            "address": "new york",
            "postcode": "631000",
            "email": "sedia.jaiteh@horizons45.com",
            "price": "5400",
            "consultation_fee": "400",
            "consultation_fee_description": "No extra add-ons",
            "language": [
                {
                    "name": "English"
                },
                {
                    "name": "Turkish"
                }
            ],
            "category": {
                "name": "Cardiologits"
            },
            "district_name": {
                "name": "Dengkil Valley"
            },
            "operating_hours": [
                {
                    "if_public_holiday": "True",
                    "weekday": "1",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "2",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "3",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "4",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "5",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "6",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                },
                {
                    "if_public_holiday": "True",
                    "weekday": "7",
                    "open_time":"06:00:00.000000",
                    "close_time":"21:00:00.000000"
                }
            ]
        }
    ]


