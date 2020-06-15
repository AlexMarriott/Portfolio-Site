#!/bin/bash

eval "$(ssh-agent -s)" # Start ssh-agent cache
chmod 600 id_rsa # Allow read access to the private key
ssh-add id_rsa # Add the private key to SSH

git config --global push.default matching
git remote add deploy ssh://git@$IP:$PORT$DEPLOY_DIR
git push deploy master

# Skip this command if you don't need to execute any additional commands after deploying.
ssh -tt app@$IP -p $PORT <<EOF
  cd $DEPLOY_DIR
  docker-compose down
  docker rmi $(docker images |grep 'my-site_web') || true
  docker rm $(docker ps -a -f status=exited -q) || true
  docker-compose up -d
EOF