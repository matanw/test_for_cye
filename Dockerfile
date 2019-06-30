FROM ubuntu:18.04
COPY word_count_service /root/word_count_service
COPY run.sh /root/run.sh
RUN apt-get update
RUN apt-get install python3 virtualenv -y
WORKDIR /root/
RUN virtualenv -p python3 venv
RUN venv/bin/python3 -m pip install flask requests flask_restplus flask-login flask-security flask-sqlalchemy flask-jwt-extended passlib
RUN chmod u+x run.sh
CMD ./run.sh