# RHDEVS-AY2223-BE2-flask

Setup a basic API to simulate a website that tracks profiles and scores for exams.

A simulated db is provided. Note that the db will not be updated between runs.

In main: 
- GET / homepage that returns a welcome message 

In profiles API (/profiles prefix):

- GET /{id} to retrieve the name and all scores of a profile 
- POST /profiles to create a new profile (name only) 
- DELETE /{id} to delete a profile 
- GET /{id}/score?minScore= to retrieve all scores of a profile, above the min score. If min score not provided, return all scores


In authentication API (/auth prefix):
- POST /register stores a username and hashedPassword (given as hashed) Store it in a local array Login /login checks if the provided information is valid and return a jwt token + success message

Give a reasonable return format with appropriate status code and messages. {“message” : “success/fail”, “data”:””} 

Remember to create a documentation as well (Refer to Google Docs)

OPTIONALS: Add environmental variables into the system (for jwt signing secret) In the login route, check if jwt token is provided and valid Assume URL argument has token “?token=sdlkaskdnalsdnsald” See if username and password field are present


Retrieves the name and scores of a profile

Function used : getProfile()
Source: ProfilesAPI.py

Parameters : id (Required)

Unique integer representing the ID of each user in the db

Response : Returns a dictionary containing the user's profile and a success message

Example :
{
    "data": {
        "name": "Chun Yu",
        "scores": [
            1,
            3,
            3,
            4,
            5
        ]
    },
    "status": "success"
}

Create a new profile to store the name of the user

Function used : createProfile()
Source: ProfilesAPI.py

Parameters : name (Required)

The name of the new user

Response : Returns a dictionary containing the name of the user and a success message

Example :
{
    "details": {
        "name": "John"
    },
    "status": "success"
}

Deletes the profile from db based on the ID received

Function used : delProfile()
Source: ProfilesAPI.py

Parameters : id (Required)

Unique integer representing the ID of each user in the db

Response : Returns a dictionary containing the remaining profiles in the database and a success message

Example :
{
    "details": [
        {
            "name": "Chun Yu",
            "scores": [
                1,
                3,
                3,
                4,
                5
            ]
        },
        {
            "name": "Marcus",
            "scores": [
                5,
                4,
                3,
                2,
                1
            ]
        }
    ],
    "status": "success"
}

Retrieves the name and scores of a profile

Function used : getScore()
Source: ProfilesAPI.py

Parameters : id (Required), minScore (Required)

id: Unique integer representing the ID of each user in the db

minScore: The minimum score to be checked against

Response : Returns a dictionary containing all the user's scores above the
           minimum score and a success message

Example :
["GET"] http://localhost:8080/profiles/1/score?minScore=1
{
    "scores": [
        5,
        4,
        3,
        2
    ],
    "status": "success"
}

Registers the username and passwordHash of a user and stores it in a local array

Function used : registerUser()
Source: AuthAPI.py

Parameters : username (Required), passwordHash (Required)

username: Username of the user
passwordHash: Unique hash representing the password of the user

Response : Returns a success message indicating the user has been registered

Example :
["POST"] http://localhost:8080/auth/login?username=joe&passwordHash=test
{
    "message": "User registered",
    "status": "success"
}

Checks if the username and passwordHash provided is valid. If valid, encodes it and returns a jwt token
and a success message.

Function used : login()
Source: AuthAPI.py

Parameters : username (Required), passwordHash (Required)

username: Username of the user
passwordHash: Unique hash representing the password of the user

Response : Returns a jwt token and a success message

Example :
["POST"] http://localhost:8080/auth/login?username=joe&passwordHash=test
{
    "status": "success",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvZSIsInBhc3N3b3JkSGFzaCI6InRlc3QifQ.a-hr1ovPgwZVjAnPRPjgBPlQPF6lGp_CjAbOVpZZuUA"
}