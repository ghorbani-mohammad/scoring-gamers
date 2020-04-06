This is a simple api that in that we have some gamers with mobile_number and score.
This project was developed on **TDD** approach which means we first code our tests and then try to pass these tests.

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

