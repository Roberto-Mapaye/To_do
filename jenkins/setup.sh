#!/bin/bash

echo "Setup stage"

# installing requirements
sudo apt-get update
sudo apt install -y curl jq
curl https://get.docker.com | sudo bash

sudo usermod -aG docker jenkins
newgrp docker

version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

docker login --username $DOCKER_HUB_CREDS_USR --password $DOCKER_HUB_CREDS_PSW

