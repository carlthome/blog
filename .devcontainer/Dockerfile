FROM debian:bullseye

COPY apt.txt .
RUN apt-get update && apt-get install -y $(cat apt.txt)

RUN useradd --create-home --shell=/bin/bash --groups=sudo developer
RUN echo 'developer ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
