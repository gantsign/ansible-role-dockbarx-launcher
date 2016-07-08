Ansible Role: DockbarX Launcher
===============================

Role to add items to the DockbarX launcher.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Items to add to the DockbarX launcer
docbarx_launcher_items: []
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.docbarx-launcher
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
