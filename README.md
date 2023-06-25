<br />
<p align="center">
  <h1 align="center">Mozio: API integration assessment</h1>
</p>

## Table of Contents

* [Project Structure](#project-structure)
* [How to run the application](#how-to-run-the-application)
* [Endpoints](#endpoints)
* [Output data](#output-data)
* [Tests](#tests)
* [Clone the Application](#clone-the-application)
* [Contributing](#contributing)


## Project Structure

    ├── Monzio                    
    │   ├── app                        # App's Python scripts 
    │   │    ├── __init__.py       
    │   │    ├── external_api.py       # API's requests
    │   │    └── views.py              # API's endpoints
    │   ├── config                     # Configuration
    │   │    ├── __init__.py
    │   │    └── settings.py           # Configuration settings
    │   ├── api-tests                  # Tests
    │   │    ├── tests.py              # unittests
    │   │    └── test_integration.py   # Integration tests 
    │   ├── .env.example               # .env file example        
    │   ├── .gitignore                 
    │   ├── requierements.txt          # Package dependencies
    │   ├── run.py                     # Run the app
    │   └── README.md                  # README file

## How to run the application

1. Clone the app to your local machine
2. Change properly the working directory
3. Create a .env file according to .env.example
4. Execute "python run.py" to a command prompt

## Endpoints

Endpoint: /v2/search/  <br />
Allowed methods: POST  <br />
Parameters and response specification:  <br />
https://api.mozio.com/v2/docs/#operation/search_create  <br />
  <br />
Endpoint: /v2/search/<search_id>/poll/  <br />
Allowed methods: GET  <br />
Parameters and response specification:  <br />
https://api.mozio.com/v2/docs/#operation/search_poll  <br />
  <br />
Endpoint: /v2/reservations/  <br />
Allowed methods: POST  <br />
Parameters and response specification:  <br />
https://api.mozio.com/v2/docs/#operation/reservations_create  <br />
  <br />
Endpoint: /v2/reservations/<search_id>/poll/  <br />
Allowed methods: GET  <br />
Parameters and response specification:  <br />
https://api.mozio.com/v2/docs/#operation/reservations_poll  <br />
  <br />
Endpoint: /v2/reservations/<reservation_id>/  <br />
Allowed methods: DELETE  <br />
Parameters and response specification:  <br />
https://api.mozio.com/v2/docs/#operation/reservations_delete  <br />


## Output data

Output data would be on json format.

## Tests

1. *tests.py*   <br /> Unittests for API  <br /> Execution: "python tests.py" in command prompt  <br />

2. *test_integration.py* <br /> Integration test according to assessment:  <br />
* Booking using search parameters:  <br />
{   <br />
  "start_address": "44 Tehama Street, San Francisco, CA, USA",  <br />
  "end_address": "SFO",  <br />
  "mode": "one_way",  <br />
  "pickup_datetime": "2023-12-01 15:30",  <br />
  "num_passengers": 2,  <br />
  "currency": "USD",  <br />
  "campaign": "{your full name}"  <br />
}  <br />
* Cancel the cooking   <br />
* Return confirmation number  <br />

Execution: "python test_integration.py" in command prompt   <br />
Expected outcome: confirmation number  <br />

## Clone the Application

``
git clone https://github.com/pkmath/Mozio.git
``

## Contributing

1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
