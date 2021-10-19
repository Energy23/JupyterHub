# Jupyterhub for temporary use
TEXT
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
* TmpAuthenticator
    pip3 install jupyterhub-tmpauthenticator
* NBGitPuller
    pip3 install nbgitpuller
