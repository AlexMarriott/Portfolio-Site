"""
This file is used for replacing the environment variables during the deployment stage. The variables are held in travis-ci for the repo.
This means that the env variables are not included on the website, reducing the security risk.
"""
from yaml import load, dump, Loader, YAMLError
import os
import sys

mongo_pw = sys.argv[1]
token = sys.argv[2]

#Replace variables in javascript file.
with open('mongo-init.js', 'r') as f :
  mongo_file = f.read()

# Replace the target string
mongo_file = mongo_file.replace('MONGO_INITDB_ROOT_PASSWORD', mongo_pw)

# Write the file out again
with open('mongo-init.js', 'w') as f:
  f.write(mongo_file)

#Replace variables in evn file.
with open('.env', 'r') as file :
  env_file = file.read()

# Replace the target string
env_file = env_file.replace('MONGO_INITDB_ROOT_PASSWORD', mongo_pw).replace('GITHUB_TOKEN', token)

# Write the file out again
with open('.env', 'w') as file:
  file.write(env_file)