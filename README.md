# Ansible role to deploy a Flask project.  
![ansible-software-version](https://img.shields.io/badge/ansible-v2.9.6-informational)
![flask-software-version](https://img.shields.io/badge/Flask-v1.1.1-important)
![molecule-software-version](https://img.shields.io/badge/Molecule-v2.22-lightgrey)
  
## Description
  
- Install `python & dependencies`
- Install `Pypi pkgs` following requirements file
- Setup `env vars`
- Launch project using `flask run`
  
## Dependencies
  
- `python3.8`
- `python3.8-pip`
- `pip install --upgrade pip`
- `pip install -r requirements.txt`
- `certbot certonly --standalone` for your domain & fill `roles/flask/defaults/main.yaml` with it.

## Getting Started  

```bash
Run >  
ansible-playbook -i inventory.ini provisioning-flask-app.yaml  
No Host Key Check >  
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i inventory.ini provisioning-flask-app.yaml  
```
  
## Test the project
  
```bash
pip install molecule==2.22
molecule test
```

## Debug
  
```bash
Dry-run >  
ansible-playbook --check --diff -i inventory.ini provisioning-flask-app.yaml  
Verbose mode >  
ansible-playbook -vvv --diff -i inventory.ini provisioning-flask-app.yaml  
```
