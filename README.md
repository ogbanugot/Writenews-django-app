# Writenews-django-app
The django peoject contains two apps, article and authorization. The api endpoints in each app is described below  
view the api endpoints here https://writenews.herokuapp.com/auth/login/

## auth/signup  
Endpoint for signing up; Allowed http method: POST.  
Sample request: {"email":"ogbanugot@gmail.com","password":"ogban","name":"ogban ugot","bio":"Scientist"}  

## auth/login  
Endpoint for login; Allowed http method: POST.  
Sample request: {"email":"ogbanugot@gmail.com","password":"ogban"}  
  
## augh/logout  
Endpoint for logout; Allowed http method: POST.  
Sample request: {" "}    
  
## article/  
Endpoint for getting all articles; Allowed http method: GET  

## article/id?  
Endpoint for getting a particular article; Allowed http method: GET,POST, PUT, DELETE PATCH   
Sample response: {
        "id": 1,
        "user": "ogban ugot",
        "article_name": "My first article",
        "category": "Horror",
        "description": "This is a horror story with a happy end set in...."
    }  
 
## article/users  
Endpoint for getting all writers; Allowed http method: GET  
Returns json of all writers  

## article/users/id?  
Endpoint for getting a particular writer; Allowed http method: POST, GET  
Sample response: {
        "id": 1,
        "name": "ogban ugot",
        "bio": "Scientist",
        "email": "ogbanugot@gmail.com"
    }   



