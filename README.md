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
ansible-playbook -i inventory.ini --diff provisioning-flask-app.yaml
```
