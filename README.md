Ansible Role: DockbarX Launcher
===============================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-dockbarx-launcher.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-dockbarx-launcher)

Role to add items to the DockbarX launcher.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Users with items to add to the DockbarX launcher
users: []
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.docbarx-launcher
      users:
        - username: vagrant
          docbarx_launcher_items:
            - 'exo-terminal-emulator;/usr/share/applications/exo-terminal-emulator.desktop'
            - 'thunar;/usr/share/applications/Thunar-folder-handler.desktop'
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
