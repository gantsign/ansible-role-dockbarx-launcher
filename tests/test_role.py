from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_dockbarx_config(Sudo, Command):
    # Need to -set-home when using sudo for gconftool-2 to work
    output = Command.check_output("sudo %s --set-home gconftool-2 --get %s",
                                  '--user=test_usr',
                                  '/apps/dockbarx/launchers')
    assert 'test-app;/usr/share/applications/test-app.desktop' in output
