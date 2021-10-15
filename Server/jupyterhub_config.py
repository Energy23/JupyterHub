import os
import pwd
import sys
from shutil import copytree, copyfile, rmtree

#--------------------------------------------------------------------------------
# Fill this variables to get things working
#--------------------------------------------------------------------------------
# Admin usernames
admins= set({''})

# url of your server
server_ip = '' # needed for idle-culler

# Path where files are stored
data_path = ''  # has to end with a slash

# If you use oAuth
use_oAuth = True # Set to false if not
oAuth_client_ID = ''
oAuth_client_secret = ''
oAuth_callback_url = ''

# For ssl encryption
path_ssl_key = ''
path_ssl_cert = ''

# Allowed images
# use list or dict for example {'image1':'jupyterhub/image1:0.1'} 
docker_images = 

# Use JupyterLab on launch, set to false for classic notebook
use_lab = True 

#--------------------------------------------------------------------------------
# Configuration starts here
#--------------------------------------------------------------------------------

# create homefolders on server, to get data persistence
def fix_dir(spawner):
    username = spawner.user.name
    path = os.path.join('/home', username)
    statement = username +":" + str(100) + " " + path
    s = "chown -R " + statement
    t = "chmod -R ugo+rw " + path
    if not os.path.exists(path):
        os.chdir('/home')
        os.mkdir(username)
    os.system(s)
    os.system(t)
## The ip address for the Hub process to *bind* to.
#
# See `hub_connect_ip` for cases where the bind and connect address should differ.
c.JupyterHub.hub_ip = '0.0.0.0'

# Path to logfile
c.JupyterHub.log_level = 'WARN'

## The class to use for spawning single-user servers.
#

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.notebook_dir = '/home/{username}'

# attach the hook function to the spawner
c.Spawner.pre_spawn_hook = fix_dir

#Set CPU Limit
c.Spawner.cpu_limit = 0.5
c.Spawner.mem_limit = '1500M'
c.DockerSpawner.allowed_images = docker_images

c.DockerSpawner.volumes = {'/home/{username}': '/home/{username}'}

# Allow users to have multiple container 
c.JupyterHub.allow_named_servers = True
c.DockerSpawner.name_template = '{prefix}-{username}-{servername}'

#------------------------------------------------------------------------------
# Authenticator(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
#  Defaults to an empty set, in which case no user has admin access.
c.Authenticator.admin_users = admins

#  Supports Linux and BSD variants only.
c.LocalAuthenticator.create_system_users = True

# The docker instances need access to the Hub, so the default loopback port doesn't work:
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]

# Use JupyterLab instead of classic
if use_lab:
    c.Spawner.default_url = '/lab'

# GitLab OAuth
if use_oAuth:
    from oauthenticator.gitlab import GitLabOAuthenticator
    c.JupyterHub.authenticator_class = 'oauthenticator.gitlab.LocalGitLabOAuthenticator'
    c.LocalAuthenticator.create_system_users = True
    c.LocalGitLabOAuthenticator.oauth_callback_url = oAuth_callback_url
    c.GitLabOAuthenticator.client_id = oAuth_client_ID
    c.GitLabOAuthenticator.client_secret = oAuth_client_secret

#  When setting this, you should also set ssl_key
c.JupyterHub.ssl_key = path_ssl_key
c.JupyterHub.ssl_cert = path_ssl_cert

# Set path to cookie file
c.JupyterHub.cookie_secret_file = data_path +'jupyterhub_cookie_secret'
c.JupyterHub.db_url = data_path +'jupyterhub.sqlite'

c.JupyterHub.services = [
    {
        'name': 'idle-culler',
        'admin': True,
        'command': [
            sys.executable,
            '-m', 'jupyterhub_idle_culler',
            '--timeout=3600',
                '--url=' +server_ip +':8081/hub/api'
        ],
    }
]

