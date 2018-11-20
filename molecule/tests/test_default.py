import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_var_lib_pgsql(host):
    f = host.file('/var/lib/pgsql/')
    assert f.exists
    assert f.user == 'postgres'
    assert f.group == 'postgres'


def test_user_postgres(host):
    u = host.user('postgres')
    assert u.name
