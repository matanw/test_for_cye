FROM ubuntu:18.04
CMD apt-get update
CMD  apt-get install python3
#COPY ./word_count_service /root/

#WORKDIR /root/
#COPY word_count_service /root/word_count_service
ENTRYPOINT ["sleep","3600"]