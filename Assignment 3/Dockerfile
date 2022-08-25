###################################################################
# This Dockerfile creates an Ubuntu image with MuJoCo 2.1.0 and its
# dependencies installed/configured in order to run code from
# assignment 3 of XCS234.
#
# Notes: the image->container this file creates executes assignment 
# code on the system CPU. Instructions for GPU setup are included 
# for students who wish to explore running the container with GPU 
# access. The labeling of steps below are distinct from the steps 
# outlined by Docker when creating the image.
###################################################################


# 1. Pull base ubuntu image
FROM ubuntu:20.04


# 2. Update apt repositories and perform core installations
RUN apt-get update -q \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    curl \
    git \
    libglu1 \
    libxrandr2 \
    libglfw3-dev \
    libgl1-mesa-dev \
    libgl1-mesa-glx \
    libglew-dev \
    libosmesa6-dev \
    software-properties-common \
    net-tools \
    zip \
    unzip \
    vim \
    virtualenv \
    wget \
    xpra \
    xserver-xorg-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# 3. Download patchelf binaries
RUN curl -o /usr/local/bin/patchelf https://s3-us-west-2.amazonaws.com/openai-sci-artifacts/manual-builds/patchelf_0.9_amd64.elf \
    && chmod +x /usr/local/bin/patchelf


# 4. Set LANG variable 
ENV LANG C.UTF-8


# 5. Install and configure Deepmind MuJoCo version 2.1.0
RUN mkdir -p /root/.mujoco \
    && wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz -O mujoco.tar.gz \
    && tar -xf mujoco.tar.gz -C /root/.mujoco \
    && rm mujoco.tar.gz

ENV LD_LIBRARY_PATH /root/.mujoco/mujoco210/bin:${LD_LIBRARY_PATH}


# 6. Switch working directory to assignment src mount location
WORKDIR /home/cs234-a3


# 7. Install required python libraries
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN rm /usr/bin/pip && ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install --no-cache-dir \
    'numpy>=1.21.1' \
    'mujoco-py<2.2,>=2.1' \
    torch \
    gym \
    matplotlib \ 
    scipy


# 8. Include first import to build mujoco-py
RUN python -c 'import mujoco_py'
