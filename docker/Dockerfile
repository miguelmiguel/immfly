# Dockerfile
FROM python:3.11.2-buster
LABEL maintainer="Miguel Ambrosio"

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY docker/nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/backend
RUN mkdir -p /opt/app/backend/logs
COPY requirements.txt docker/start-server.sh /opt/app/
WORKDIR /opt/app/
RUN pip install -r requirements.txt
COPY ./immfly /opt/app/backend

RUN chmod 755 /opt/app/start-server.sh
RUN chown -R www-data:www-data /opt/app

ENV http_proxy ""
ENV https_proxy ""

# start server
EXPOSE 8989
STOPSIGNAL SIGTERM
ENTRYPOINT ["bash", "/opt/app/start-server.sh"]