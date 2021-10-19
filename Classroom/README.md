# Classroom Setup
This Setup runs a whole JupyterHub instance in one Docker container including user-data persistence, nbgrader and several Python3 packages  
Classroom is initially setup with Firstuse Spawner, so that every user can pick its username/passwort at first sign in.  
So make sure, that your admin accounts declared in jupyterhub_config.py are set and that you set your nbgrader account.  
## Prequisites
You need to install the following packages:  
* Docker
* Nginx 

## Build Classroom Docker Image  
**Before building image, make sure that you've set the right git url in dockerfile** 
There a two dockerfiles for classrooms. They are quite similar, despite that the nbgrader runs on Python 3.6 and the other one is on Python 3.9.  
This is because the Nbgitpuller needs Python 3.7 or higher, and nbgrader still has problems with Python versions above 3.6.  
So rename the file you want to 'dockerfile'.  
Now we have to build the Docker image for the classroom container:
````bash
docker build -t NAMESPACE/NAME:Version .  
````
for example: 
````bash
docker build -t jupyterhub/classroom:0.1 .  
````
## Start Container from Image
Next step is to start your classroom container from the former build docker image.   
````bash
docker run docker run -d -p HOSTPORT:8000 --name CONTAINERNAME IMAGE  
````
for example:  
````bash
docker run -d -p 9100:8000 --name classroom1 jupyterhub/classroom:0.1  
````
**Note the HOSTPORT for your webserver config**  

## Setup your webserver / reverse-proxy
I've made good expiriences with nginx, see config for example.  
Edit the config file depending on your server config:
* Set you domain
* Enable ssl
Copy the config file to your nginx configuratiom path:
    cp nginx /etc/nginx/sites-available/jupyterhub
Make config availible:
    ln -s /etc/nginx/sites-available/jupyterhub /etc/nginx/sites-enabled/jupyterhub
Reload nginx
    systemctl reload nginx  

**DONE!** 
## Git oAuth
If you use git for oAuth, here is a guide, how to setup:  
<https://docs.gitlab.com/ee/integration/oauth_provider.html>

## Change classroom configuration
To change your config file, log in into container an edit the config with the ewditor of your choice
````bash
docker exec -ti $CONTAINERNAME /bin/bash
nano jupyterhub_config.py
```` 

## Visualization
Here is a scematic overview how this setup works.  

<img src="https://github.com/Energy23/JupyterHub/blob/5d1b3e07e1c5565a5c1b9775b820f13c58c05462/.img/classroom.jpg" width="80%">
