def test_requirements_file(host):
    defaults_file = "file=../../defaults/main.yaml"
    defaults_vars = host.ansible("include_vars", defaults_file)
    print(defaults_vars)
    requirements_file = defaults_vars['requirement_path']
    assert requirements_file.exists
    assert requirements_file.is_file
    assert requirements_file.user == 'root'
    assert requirements_file.group == 'group'
    assert oct(requirements_file.mode) == '0755'

def test_pip_pkgs_are_installed(host):
    defaults_vars = host.ansible("include_vars", "file=../../../roles/flask/defaults/main.yaml")
    requirements_file = defaults_vars['requirement_path']
    ansible_host_vars = host.ansible.get_variables()
    requirements_content = ansible_host_vars['requirement_list']
    print(requirements_content)
    installed_pip_pkgs = host.check_output("pip3 list")
    print(installed_pip_pkgs)
    for pkg in requirements_content:
        print(pkg)
        assert installed_pip_pkgs.contains(pkg)
