To deploy the service, run:
make run

assuming you already have python3 and virtualenv on your machine.
** if instead "python3" your os recognize "python3.6" or other version, 
please change it in makefile


to test the service please enter to http://localhost:5000/static/ (it must be this, 
not http://127.0.0.1:5000/static/ because google captcha client requires domain localhost)
once you hit "I'm not a robot", simple e2e test is executed, see web console from logs

list of endpoint available in http://localhost:5000/


 you can build it from dockerfile. 
 (the EXPOSE port didn't work for me on mac, but you can send 
 requests by curl from inside the docker)