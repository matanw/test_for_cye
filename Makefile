venv:
	virtualenv -p python3 venv
	venv/bin/python3 -m pip install flask requests flask_restplus flask-login flask-security flask-sqlalchemy flask-jwt-extended passlib

run: venv
	PYTHONPATH=. venv/bin/python3 word_count_service/app.py