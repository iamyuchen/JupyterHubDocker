# Configuration file for Jupyter Hub
import os
c = get_config()

# spawn with Docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.Spawner.args = ['--debug', ]
# The docker instances need access to the Hub, so the default loopback port doesn't work:
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8889
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.hub_port = 8091
c.DockerSpawner.network_name = 'jupyter_hub_docker_default'
c.DockerSpawner.remove = True
c.DockerSpawner.hub_ip_connect = 'jupyterhub'
c.JupyterHub.allow_named_servers = True
# c.DockerSpawner.container_image = os.environ['DOCKER_NOTEBOOK_IMAGE']
# Explicitly set notebook directory because we'll be mounting a host volume to
# it.  Most jupyter/docker-stacks *-notebook images run the Notebook server as
# user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# We follow the same convention.
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work/'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.image = os.environ.get('DOCKER_NOTEBOOK_IMAGE') or 'jupyter/base-notebook'
# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.extra_create_kwargs = {'user': 'root'}
c.DockerSpawner.environment = {
  'GRANT_SUDO': '1',
  'UID': '0', # workaround https://github.com/jupyter/docker-stacks/pull/420
}
c.DockerSpawner.volumes = {
	'jupyterhub-user-{username}': notebook_dir,
	'jupyter_hub_docker_data_volume': '/home/jovyan/work/data/'
	}
# admin
c.Authenticator.admin_users = {'taylor', }
# OAuth with GitHub
# c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
c.Spawner.default_url = '/lab'

# c.Authenticator.whitelist = whitelist = set()
# c.Authenticator.admin_users = admin = set()

# import os

# join = os.path.join
# here = os.path.dirname(__file__)
# with open(join(here, 'userlist')) as f:
#     for line in f:
#         if not line:
#             continue
#         parts = line.split()
#         name = parts[0]
#         whitelist.add(name)
#         if len(parts) > 1 and parts[1] == 'admin':
#             admin.add(name)

# c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

# # User containers will access hub by container name on the Docker network


