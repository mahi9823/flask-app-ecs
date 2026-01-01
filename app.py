from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_all():
    return 'ssh -i "docker-in-one-shot.pem" ubuntu@ec2-15-134-205-21.ap-southeast-2.compute.amazonaws.com,sudo apt update,sudo apt -get update,sudo apt-get install docker.io,sudo systemctl status docker,docker ps,whoami,sudo usermod -aG docker $USER,newgrp docker,docker images,docker login'

@app.route('/health')
def health():
    return 'Server is up and running'
