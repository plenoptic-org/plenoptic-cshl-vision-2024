FROM --platform=linux/amd64 pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y python3-dev python3-pip

# to get docker image working for binder
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}
RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

COPY . ${HOME}
RUN pip3 install jupyterlab notebook jupyterhub
RUN pip3 install -r ${HOME}/plenoptic-cshl-vision-2024/requirements.txt
RUN python3 ${HOME}/scripts/setup.py
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
WORKDIR ${HOME}
