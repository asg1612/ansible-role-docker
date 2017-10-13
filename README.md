![Status](https://travis-ci.org/asg1612/ansible-docker.svg?branch=master)

Role Docker
=========

This role is for Docker system. Testing based on geerlingguy (https://github.com/geerlingguy)

Requirements
------------


Role Variables
--------------
*registry_mirrors* registry mirror for docker system
*insecure_registries* insecure registries for docker system
*dns* dns servers for docker system

Dependencies
------------


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      vars:
        registry_mirrors:
          - http://example.com:5001
          - http://example2.com:5000
        insecure_registries:
          - example.com:5000
          - example2.com:5001
        dns:
         - 8.8.8.8
         - 9.9.9.9
      roles:
         - { role: username.rolename, x: 42 }


License
-------

GNU General Public License v 3.0


Author Information
------------------

Andrés Sánchez García
twitter: @asg1612
e-mail: asg1612@gmail.com
linkedin: https://www.linkedin.com/in/asg1612/
