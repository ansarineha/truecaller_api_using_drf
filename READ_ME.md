# DJANGO TRUECALLER

Steps to run the API
## Install dependencies
```
pip3 install -r requirements.txt
```

## Runserver
```
python3 manage.py runserver
```
## Test the API
```
Route: http://localhost:8000/register/
Request Type: POST
Data: 

    {
        "name":"user1",
        "email":"user1@gmail.com",
        "password":"user1123",
        "phone":"2200331010"
    }

```
Route: http://localhost:8000/login/
Request Type: POST
Data: 

    {
        "username":"user1",
        "password":"user1123"
    }
```
### JWT AUTH
You will receive a JWT Auth Token after register and login.
Include the JWT token in headers as a Bearer Token for all private requests
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhbmt1ciJ9.eQicFQy2nYric9Gl2mhqOH4l8An7B_Kf2CKoJmZrPcA
```

### To view all the contacts
```
Public Route: http://localhost:8000/contacts/
Request Type: GET, POST
Data:
    {
        "name":"tim",
        "email":"tim@gmail.com",
        "password":"tim123",
        "phone_number":"2200331010",
        "spam":"false"
    }

```

### To mark a contact as SPAM
```
Private Route: http://localhost:8000/spams/
Request Type: POST
Data:
    {
        "phone_number": "2200331010"
    }
```

### To search a contact by name
```
Private Route: http://localhost:8000/search_by_name/
Request Type: POST
Data:
    {
       "name":"kim"
    }
```

### To search a contact by phone
```
Private Route: http://localhost:8000/search_by_phone_number/
Request Type: POST
Data:
    {
       "phone_number": "2200331010"
    }

```