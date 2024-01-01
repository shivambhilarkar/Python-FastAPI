# FastAPI

### Install FastAPI and Uvicorn webserver
```bash
$ python -m pip install fastapi
$ pip install uvicorn
```
---
### Run Uvicorn webserver
```
$ uvicorn MyApi:app --reload 
```
default port : 8000

---

### Swagger UI
fast api provides swagger ui to test api call through browser.
```
URL : http://127.0.0.1:8000/docs
```
---


### API  Methods
- GET 
- PUT
- POST
- DELETE
---

### Sample Program
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/) 
def index_page():
    return { "message" : "welcome to fastapi basics" }

```