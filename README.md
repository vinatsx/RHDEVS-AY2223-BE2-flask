# RHDEVS-AY2223-BE2-flask

Setup a basic API to simulate a website that tracks profiles and scores for exams.

A simulated db is provided. Note that the db will not be updated between runs.

In main: 
- GET / homepage that returns a welcome message <>

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
