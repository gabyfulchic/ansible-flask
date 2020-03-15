def test_dependencies_are_installed(host):
    ansible_vars = host.ansible.get_variables()
    print(ansible_vars)
    dependencies = ansible_vars['centos_development_tools_pkgs']
    for i in dependencies:
        assert host.package(i).is_installed

def test_base_pkgs_are_installed(host):
    ansible_vars = host.ansible.get_variables()
    base_pkgs = ansible_vars['centos_base_pkgs']
    for i in base_pkgs:
        assert host.package(i).is_installed

def test_python3_is_installed(host):
    python3 = host.run("python3 -V")
    pip3 = host.run("pip3 -V")
    assert python3.rc == 0 
    assert pip3.rc == 0
