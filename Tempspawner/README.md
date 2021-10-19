# Jupyterhub for temporary use
TEXT
## Prequisites
You need to install the following packages:
* Python 3.5 or greater
* NodeJS / npm
````bash
apt-get install npm nodejs-legacy
````
* Jupyterhub
````bash
python3 -m pip install jupyterhub
````
* Configurable http-proxy
````bash
npm install -g configurable-http-proxy
````
* Docker
<https://docs.docker.com/engine/install/debian/>
* Dockerspawner
````bash
pip3 install dockerspawner
````
* TmpAuthenticator
````bash
pip3 install jupyterhub-tmpauthenticator
````
* NBGitPuller
````bash
pip3 install nbgitpuller
````
