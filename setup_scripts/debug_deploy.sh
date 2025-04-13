#!/bin/bash
github_project_name="o1_backend"
github_repo_name="https://github.com/MichaelSalata/${github_project_name}.git"
git_branch="main"
newgrp docker <<EOF
if [ ! -d "${github_project_name}" ]; then
  git clone ${github_repo_name}
fi

cp ./terraform.tfvars ./${github_project_name}/terraform/terraform.tfvars
cp ./.env ./${github_project_name}/backend/.env
# bash update_vm_env.sh

cd ./${github_project_name}/backend

mkdir -p ./data
sudo chown -R :docker ./data
sudo chmod g+s ./data
# Sets the setgid bit, which ensures that all new files and directories created under ./data inherit the docker group.
mkdir -p ./data/postgres-db-volume ./data/data_pgadmin
sudo chmod 770 ./data/data_pgadmin
sudo chown -R 5050:5050 ./data
DOCKER_BUILDKIT=1 docker compose build
docker compose up
EOF