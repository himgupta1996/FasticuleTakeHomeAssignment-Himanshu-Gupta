## Hello and welcome!

This sandbox requires Docker and Python 3.9 or greater. A virtual Python environment is recommended!

Install dependencies:
```bash
pip install -e '.[dev]'
```
Run the service:
```bash
uvicorn --app-dir service main:service --reload
```
Run the tests:
```bash
pytest service
```
Access the service from your browser:

http://localhost:8000

Build a Docker image:
```bash
docker build -t fasticule:$(git rev-parse --short HEAD) fasticule:latest .
```
Run a corresponding container:
```bash
docker run --rm -it -p 8001:8001 fasticule
```
Access the Dockerized service from your browser:

http://localhost:8001

## Challenges

Select any 2 of the following 3 challenges. Once a challenge is completed, commit it with an appropriate comment so we can find your work. 

1. The service provides an http endpoint - use the provided self-signed certificate and key (in the `localhost-cert` directory) to create an https endoint for the service. Update the README to describe how to do this and how to test that it works.
1. By default, Docker containers run as root. Following the principle of least privilege, update the Dockerfile to run the service as a non-root user. 
1. Create a GitHub Actions workflow to build the docker image on each commit to the main branch.

## Challenge 1: Creating an https endoint for the service

For running the FAST API web application, we are using Uvicorn as ASGI server. By default the service provides an http endpoint. Using SSL certificates present in the server we can make the communication between client and the server secure. Following are the 3 processes that can be followed based on preference for exposing the HTTPS endpoint to the client instead of HTTPS and establishing a secure connection between them. `Process 3` is recommended for production environment.

### Process 1: Running fastapi server directly on the host server
To the run the server:
```bash
uvicorn --app-dir service main:service --reload --ssl-keyfile localhost-cert/key.pem --ssl-certfile localhost-cert/cert.pem
```
Here we provided the location of SSL cert and key while instantiating the web server so that the communication only happens securely over HTTPS protocol.
Test:
1. Go to the brower and access the service by entering the url: https://localhost:8001
2. Run the tests: 
```bash
pytest service
```

### Process 2: Dockerizing the fast api server and exposing HTTPS endpoint
To run the server:
```bash
docker build -f Dockerfile.https -t fasticule_secure:latest .
docker run --rm -it -p 8001:8001 fasticule_secure:latest
```
Here also we provided the location of SSL cert and key while runnning the web server in the docker container so that the communication only happens securely over HTTPS protocol. `Dockerfile.https` is used instead `Dockerfile` in this case.
Test:
1. Go to the brower and access the service by entering the url: https://localhost:8001
2. Run the tests: 
```bash
pytest service
```

### Process 3(Preferred): Dockerizing the fast api server and using Traefik as a rerverse proxy server for SSL termination
Requirement: docker-compose(tested on `docker-compose version 1.29.1, build c34c88b2`)
To run the server:
```bash
sudo docker-compose up --build
```
In above two process we saw that we provide SSL termination at the application layer making the webserver to deal with complex encryption flow. In production scenarios, it is better to use SSL in a reverse proxy which eases the process of managing / installing / reconfiguring certificates on the web servers themselves. We have used `traefik` as the proxy server to handle the HTTPS request, and then internally communicating with the web server container for fetching the response.
Due to above mentioned reason, `Process 3` is preferred way of creating an https endpoint for the web service.
Test:
1. Go to the brower and access the service by entering the url: https://localhost:8001
2. Run the tests: 
```bash
pytest service
```
Note: the configuration in the reverse proxy is set so tha HTTP request will be automatically redirected to https and a secure connection will be established.







