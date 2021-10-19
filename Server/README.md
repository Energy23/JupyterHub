# Jupyterhub Server Setup
**The commands tested on Debain-based Linux distributions**  
This setup runs Jupyterhub as a service, where every user can spawn (one or more) docker container and work inside them.  
So the hub just manages the docker containers and the authentication.  
Benefits are:  
+ Data persistence, even if containers are deleted
+ Use different containers for different needs (R-Kernel, different Python versions / packages)

## Prequisites
You need to install the following packages:
* Python 3.5 or greater
* NodeJS / npm
    apt-get install npm nodejs-legacy 
* Jupyterhub
    python3 -m pip install jupyterhub
* Configurable http-proxy
    npm install -g configurable-http-proxy
* Docker
<https://docs.docker.com/engine/install/debian/>
* Dockerspawner
    pip3 install dockerspawner
* Install oAuth
    python3 -m pip install oauthenticator

## Run Jupyterhub as a service

