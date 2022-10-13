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

# Documentation
Function used : get_profile()
Source: ProfilesAPI.py

Parameters : id (required)

Unique integer representing the ID of each user in the db.



Response : Success: Returns success status with the database data. Error: Returns error message

Example : GET http://localhost:8080/profiles/0

Function used : create_new_profile
Source: ProfilesAPI.py

Parameters : 

Creates new user in the database, together with all their scores. 



Response : Success: Returns success status. Error: Returns error message

Example : POST http://localhost:8080/profiles/profiles

Function used : delete_profile()
Source: ProfilesAPI.py

Parameters : id (required)

Delete user and corresponding data from the db



Response : Success: Returns success status with deleted user info and updated db. Error: Returns error message

Example : DELETE http://localhost:8080/profiles/3


Function used : get_min_score()
Source: ProfilesAPI.py

Parameters : id (required)

Returns list of scores that are greater than the min score. Else, return all scores 



Response : Success: Returns success status with the list of scores of user. Error: Returns error message

Example : GET http://localhost:8080/profiles/0/score?minScore=3

Function used : register_user()
Source: AuthAPI.py

Parameters :

Register new user and grant access to db 



Response : Success: Returns success status. Error: Returns error message

Example : POST http://localhost:8080/auth/register?username=test?password=test123

Function used : login_user()
Source: AuthAPI.py

Parameters : id (required)

Log user into the database 



Response : Success: Returns success status with hashed password of user. Error: Returns error message

Example : GET http://localhost:8080/profiles/0/score?minScore=3

