This is a simple api that in that we have some gamers with mobile_number and score.
This project was developed on **TDD** approach which means we first code our tests and then try to pass these tests.


**1. Clone project by this command and then cd to the project directory**

`git clone https://gitlab.com/aali361/django-rest-gold-key.git`

**2. Build docker image by this command**

`docker build -t django-rest-ghorbani .`  

**2. Create a container from previous image by this command**

`docker run -p 8000:8000 -d django-rest-ghorbani`


**-----------------------------------------**

**You can do this operations on this api**

**1. Creating new gamer:**

`POST /api/v1/gamers/ `  
> with json body   {"mobile":"09121111111", "score":"330"} 


**2. Get all gamers:**

`GET /api/v1/gamers/`



**3. Updating gamer score:**

`PUT /api/v1/gamers/09121111111/`
>  with json body {"score":"450"} 


**4. Deleting a gamer:**

`DEL /api/v1/gamers/09121111111/`

