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
