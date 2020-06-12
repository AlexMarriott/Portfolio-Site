#!/bin/bash

eval "$(ssh-agent -s)" # Start ssh-agent cache
chmod 600 id_rsa # Allow read access to the private key
ssh-add id_rsa # Add the private key to SSH

git config --global push.default matching
git remote add deploy ssh://git@$IP:$PORT$DEPLOY_DIR
git push deploy master
#export MONGO_INITDB_ROOT_PASSWORD=$MONGO_INITDB_ROOT_PASSWORD
#export GITHUB_TOKEN=$GITHUB_TOKEN
# Skip this command if you don't need to execute any additional commands after deploying.
ssh -tt app@$IP -p $PORT <<EOF

  cd $DEPLOY_DIR
  exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>log.out 2>&1



  python3 env_replace.py
  docker-compose down && docker-compose up &
EOF