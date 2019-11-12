FROM jupyterhub/jupyterhub:0.9.6
ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com --user
ADD ./jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py
