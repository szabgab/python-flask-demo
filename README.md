# Python Flask Demo

Application to showcase deploying a simple web application in the cloud


### Linux / Mac

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requiremets.txt
pytest -svv
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000
```

### Windows

```
pip install -r requiremets.txt
pytest -svv
set FLASK_APP=app
set FLASK_DEBUG=1
flask run --port 5000
```

