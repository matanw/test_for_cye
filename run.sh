virtualenv -p python3 venv
export FLASK_APP=word_count_service/app.py
venv/bin/python3 -m pip install flask requests
venv/bin/python3 -m pip flask run
