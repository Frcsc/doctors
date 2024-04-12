### Doctors

# Assumptions
    - Every Doctor belongs to one category.
    - Every Doctor operates in one district.
    - A doctor may be able to offer his/her services in multiple languages.
    - Multiple doctors may speak similar language(s).
    - Every doctor has his/her own operating hours. 


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


