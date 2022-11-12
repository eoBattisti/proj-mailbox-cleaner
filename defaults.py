import logging
import os
import yaml

parsed_yaml = None
with open('config.yml', 'r') as f:
    parsed_yaml = yaml.safe_load(f)

if parsed_yaml is None:
    logging.error('There\'s no config file!')
    exit(-1)

USERNAME = os.getenv('EMAIL_USERNAME', None)
PASSWORD = os.getenv('EMAIL_PASSWORD', None)

if USERNAME is None or PASSWORD is None:
    logging.error('The username or the password is not defined!')
    exit(-1)

EMAILS_TO_EXCLUDE = parsed_yaml['emails']['to_exclude']
