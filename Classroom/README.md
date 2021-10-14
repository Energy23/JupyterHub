# Classroom Setup
This Setup runs a whole JupyterHub instance in one Docker container including user-data persistence, nbgrader and several Python3 packages  
Classroom is initially setup with Firstuse Spawner, so that every user can pick its username/passwort at first sign in.  
So make sure, that your admin accounts declared in jupyterhub_config.py are set and that you set your nbgrader account.  

**Build Classroom Docker Image:**  
docker build -t NAMESPACE/NAME:Version .  
for example: docker build -t jupyterhub/classroom:0.1 .  

**Start Container from Image:**  
docker run docker run -d -p HOSTPORT:8000 --name CONTAINERNAME IMAGE  
for example: docker run -d -p 9100:8000 --name classroom1 jupyterhub/classroom:0.1  

**Setup your webserver / reverse-proxy**  
I've made good expiriences with nginx, see config for example  
**DONE!**  
