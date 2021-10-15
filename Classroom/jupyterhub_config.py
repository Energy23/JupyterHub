import os
import shutil
import sys

#--------------------------------------------------------------------------------
# Fill this variables to get things working
#--------------------------------------------------------------------------------
# Please select at leat one admin, if using firstuse spawner make sure, that you login 
admin_users = set({'USER1'})

# Formgrader users are allowed to create, distribute and evaluate nbgrader execises
grader_users = []

# If you run the classroom in a subdirectory, i.e. https://jupyterserver.com/classroom1
subdir=''

# Port the docker container is mapped to (in docker run ... -p HOST:CONATINER) HOST is the one you need to use.
# Use this for reverse-proxying in nginx or other
local_port='8000'

#--------------------------------------------------------------------------------
# Other config starts here
#--------------------------------------------------------------------------------
def fix_dir(spawner):
    username = spawner.user.name
    path = os.path.join('/home', username)
    statement = username +":" + str(100) + " " + path
    s = "chown -R " + statement
    t = "chmod -R 0700 " + path
    if not os.path.exists(path):
        u = "useradd " + username
        os.system(u)
        os.chdir('/home')
        os.mkdir(username)
        os.system(t)
    os.system(s)
    os.system('jupyter serverextension enable nbgrader.server_extensions.validate_assignment')

#Setup auth
import firstuseauthenticator
c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'
c.FirstUseAuthenticator.create_users=True

c.Authenticator.admin_users = admin_users

c.JupyterHub.cookie_secret_file = '/root/jupyterhub_cookie_secret'
c.JupyterHub.db_url = '/root/jupyterhub.sqlite'

c.Spawner.pre_spawn_hook = fix_dir
url=''
if subdir:
    c.JupyterHub.bind_url = 'http://:' +local_port +'/' +subdir
    url='--url=http://127.0.0.1:8081/' +subdir +'/hub/api'
else:
    c.JupyterHub.bind_url = 'http://:' +local_port +'/'
    url='--url=http://127.0.0.1:8081/hub/api'

c.JupyterHub.load_groups = {
    'formgrader': grader_users
}


c.JupyterHub.services = [
    {
        'name': 'nbgrader',
        'url': 'http://127.0.0.1:9999',
        'command': [
            'jupyterhub-singleuser',
            '--group=formgrader',
            '--debug',
        ],
        'user': 'grader',
        'cwd': '/home/grader'
    },
    {
        'name': 'idle-culler',
        'admin': True,
        'command': [
            sys.executable,
            '-m', 'jupyterhub_idle_culler',
            '--timeout=1800',url
        ],
    }
]
