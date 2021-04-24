#!/bin/bash

set -e

# OVERVIEW
# This script sets username and email address in Git config

# PARAMETERS
YOUR_USER_NAME="nov05"
YOUR_EMAIL_ADDRESS="***"

sudo -u ec2-user -i <<EOF
git config --global user.name "$YOUR_USER_NAME"
git config --global user.email "$YOUR_EMAIL_ADDRESS"
EOF

# OVERVIEW
# This script sets environment variables

touch /etc/profile.d/jupyter-env.sh
echo "export TWILIO_ACCOUNT_SID=***" >> /etc/profile.d/jupyter-env.sh
echo "export TWILIO_AUTH_TOKEN=***" >> /etc/profile.d/jupyter-env.sh
echo "export TWILIO_NUMBER_FROM=+1***" >> /etc/profile.d/jupyter-env.sh
echo "export TWILIO_NUMBER_TO=+1***" >> /etc/profile.d/jupyter-env.sh
initctl restart jupyter-server --no-wait