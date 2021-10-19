import os
import tmpauthenticator
import sys

#--------------------------------------------------------------------------------
# Fill this variables to get things working
#--------------------------------------------------------------------------------
# If you run the classroom in a subdirectory, i.e. https://jupyterserver.com/classroom1
subdir=''

# Set the ip adress of your server for culling inactive notebooks
server_ip=''

# Choose your Docker image
docker_img=''

# SSL config
path_cert=''
path_key=''

# Path to store data (has to end with /)
path_data=''

# Delete container after stop 
rm_container = True 

#--------------------------------------------------------------------------------
# Other config starts here
#--------------------------------------------------------------------------------
c.DockerSpawner.post_start_cmd= 'cd /home/joyvan/jupyternotebooks && jupyter trust *.ipynb'
c.DockerSpawner.remove = rm_container

## The ip address for the Hub process to *bind* to.
#
# See `hub_connect_ip` for cases where the bind and connect address should differ.
c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.authenticator_class = tmpauthenticator.TmpAuthenticator

# Run Juypterhub in subdirectory
c.JupyterHub.bind_url = 'http://127.0.0.1:8000/' +subdir

## The class to use for spawning single-user servers.
#
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = docker_img

# c.Spawner.default_url = '/lab'

from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]

#------------------------------------------------------------------------------
#  Supports Linux and BSD variants only.
c.LocalAuthenticator.create_system_users = False

c.JupyterHub.ssl_cert = path_cert
c.JupyterHub.ssl_key = path_key 

c.JupyterHub.cookie_secret_file = path_data +'jupyterhub_cookie_secret'
c.JupyterHub.db_url = path_data +'jupyterhub.sqlite'


c.JupyterHub.services = [
    {
        'name': 'idle-culler',
        'admin': True,
        'command': [
            sys.executable,
            '-m', 'jupyterhub_idle_culler',
            '--timeout=1800',
                '--url=http://' +server_ip +'8081/' +subdir +'/hub/api'
        ],
    }
]

