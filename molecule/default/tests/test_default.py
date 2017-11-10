import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_daemon_file(host):
    f = host.file('/etc/docker/daemon.json')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_docker_service(host):
    s = host.service('docker')

    assert s.is_enabled
    assert s.is_running


def test_docker_socket(host):
    assert host.socket("unix:///var/run/docker.sock").is_listening
