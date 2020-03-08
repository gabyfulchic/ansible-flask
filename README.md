# Ansible role for Flask Apps

## Description
  
- Update pkg manager
- Install python & dependencies
- Install Pypi pkgs following variables
- Create virtualenv for your app
- Launch it and binding port following variables

## Getting Started
  
```bash
pip install --upgrade pip
pip install -r requirements.txt
ansible-playbook -i inventory --diff provisioning-flask-app.yaml
```



