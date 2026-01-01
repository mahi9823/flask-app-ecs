from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_all():
    return """
    ssh -i "docker-in-one-shot.pem" ubuntu@ec2-15-134-205-21.ap-southeast-2.compute.amazonaws.com<br>
    sudo apt update<br>
    sudo apt-get update<br>
    sudo apt-get install docker.io<br>
    sudo systemctl status docker<br>
    docker ps<br>
    whoami<br>
    sudo usermod -aG docker $USER<br>
    newgrp docker<br>
    docker images<br>
    docker login
    """

@app.route('/health')
def health():
    return 'Server is up and running'

