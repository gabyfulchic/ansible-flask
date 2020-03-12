# Ansible role for Flask Apps

## Description
  
- Update pkg manager
- Install python & dependencies
- Install Pypi pkgs following variables
- Create virtualenv for your app
- Launch it and binding port following variables
  
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
