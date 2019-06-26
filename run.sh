virtualenv -p python3 venv
venv/bin/python3 -m pip install flask requests flask_restplus flask-login flask-security flask-sqlalchemy

#export FLASK_APP=word_count_service/app.py
#PYTHONPATH=. venv/bin/python3 -m pip flask run

 PYTHONPATH=. venv/bin/python3 word_count_service/app2.py
