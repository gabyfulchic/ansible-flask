# Ansible role to deploy a Flask project.  
![ansible-software-version](https://img.shields.io/badge/ansible-v2.9.6-informational)
![flask-software-version](https://img.shields.io/badge/Flask-1.1.1-important)
  
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

## Getting Started  

```bash
Run >  
ansible-playbook -i inventory.ini provisioning-flask-app.yaml  
No Host Key Check >  
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i inventory.ini provisioning-flask-app.yaml  
```
  
## Debug
  
```bash
Dry-run >  
ansible-playbook --check --diff -i inventory.ini provisioning-flask-app.yaml  
Verbose mode >  
ansible-playbook -vvv --diff -i inventory.ini provisioning-flask-app.yaml  
```
