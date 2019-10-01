FROM python:3.7-slim-buster

WORKDIR /opt/{{cookiecutter.repo_name}}

USER root

RUN apt-get update
RUN apt-get -y install gcc python3-dev

RUN addgroup --system --gid 112 kubeapp
RUN adduser --system --gid 112 --uid 107 kubeapp

ENV AWS_DEFAULT_REGION ap-southeast-2
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ADD . .

RUN chown -R kubeapp:kubeapp /opt/{{cookiecutter.repo_name}}/

USER kubeapp

ENTRYPOINT [ "./start.sh" ]
# CMD ["bash"]