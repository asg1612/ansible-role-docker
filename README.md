![Status](https://travis-ci.org/asg1612/ansible-role-docker.svg?branch=master)

Role Docker
=========

This role is for install Docker system. Testing with molecule

Requirements
------------

None

Role Variables
--------------
**daemon_json**: Dictionary with daemon.json options

Dependencies
------------

None


Example Playbook
----------------

    - hosts: servers
      vars:
        daemon_json:
          registry-mirrors:
            - http://example.com:5001
          insecure-registries:
            - example.com:5000
          dns:
            - 8.8.8.8
      roles:
         - { role: asg1612.ansible-role-docker }


License
-------

GNU General Public License v 3.0


Author Information
------------------

Andrés Sánchez García

twitter: @asg1612

e-mail: asg1612@gmail.com

linkedin: https://www.linkedin.com/in/asg1612/

website: http://andressaga.es/
