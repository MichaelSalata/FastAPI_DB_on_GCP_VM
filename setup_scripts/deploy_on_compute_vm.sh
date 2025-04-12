#!/bin/bash
github_project_name="FastAPI_DB_on_GCP_VM"
github_repo_name="https://github.com/MichaelSalata/${github_project_name}.git"
git_branch="main"

sudo snap install docker
sudo groupadd -f docker
sudo usermod -aG docker $(whoami)

echo "Waiting for Docker socket to be available..."
while [ ! -S /var/run/docker.sock ]; do sleep 1; done

sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock

newgrp docker <<EOF
if [ ! -d "${github_project_name}" ]; then
  git clone --branch ${git_branch} --single-branch --depth 1 ${github_repo_name}
  cp ./terraform.tfvars ./${github_project_name}/terraform/terraform.tfvars
  cp ./.env ./${github_project_name}/backend/.env
# bash update_vm_env.sh
fi  

cd ./${github_project_name}/backend
DOCKER_BUILDKIT=1 docker compose build
docker compose up -d
EOF