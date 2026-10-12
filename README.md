# Dockerizing and Deploying a Flask Application on AWS EC2

A simple Python Flask web application packaged into a Docker image and suitable for deployment on an AWS EC2 Linux instance.

## Project structure

```text
python-flask-app/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Prerequisites

- Docker Engine
- Git
- An AWS EC2 instance if deploying to AWS

## Run locally with Docker

Clone the repository:

```bash
git clone https://github.com/Vinayak202003/python-flask-app.git
cd python-flask-app
```

Build the image:

```bash
docker build -t pythonapp .
```

Create a custom bridge network:

```bash
docker network create network1
```

Run the container on that network:

```bash
docker run -d -p 5000:5000 --name pythonapp --network network1 pythonapp
```

Open [http://localhost:5000](http://localhost:5000).

## Verify the deployment

Check the running container:

```bash
docker ps
```

List Docker networks:

```bash
docker network ls
```

Inspect the custom network and its connected containers:

```bash
docker network inspect network1
```

## Deploy on AWS EC2

1. Launch an EC2 instance and install Docker Engine and Git.
2. Clone this repository and move into the project directory.
3. Build the image and create the Docker network using the commands above.
4. Run the container with port mapping `-p 5000:5000`.
5. In the EC2 security group's inbound rules, allow TCP port 5000 only from trusted IP addresses when possible.
6. Visit `http://<EC2-PUBLIC-IP>:5000`.

The Flask development server is suitable for learning and testing. For production deployments, use a production WSGI server such as Gunicorn and configure HTTPS and appropriate network access controls.

## Technologies

- Python
- Flask
- Docker
- Docker bridge networking
- AWS EC2
- Git
