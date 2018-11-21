[![Build Status](https://travis-ci.org/pescobar/ansible-role-postgres.svg?branch=master)](https://travis-ci.org/pescobar/ansible-role-postgres)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-pescobar.postgres-blue.svg)](https://galaxy.ansible.com/pescobar/postgres)

pescobar.postgres
=========

Install postgresql database and create a db and a user

Role Variables
--------------
```
postgres_version: "9.6"

# https://wiki.postgresql.org/wiki/YUM_Installation
postgres_yum_repos_rpm: "https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-redhat96-9.6-3.noarch.rpm"

# postgres_version_no_dots is defined in tasks/main.yml using set_fact
postgres_packages:
  - "postgresql{{ postgres_version_no_dots }}"
  - "postgresql{{ postgres_version_no_dots }}-server"
  - "postgresql{{ postgres_version_no_dots }}-contrib"
  - "postgresql{{ postgres_version_no_dots }}-libs"

postgres_user_to_create: 'testuser1'

postgress_user_password: 'testpasswd1'

postgres_db_to_create: 'testdb1'
```

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: pescobar.postgres,
	 	   postgres_user_to_create: "user1",
		   postgress_user_password: "coolP4ss",
		   postgres_db_to_create: 'cooldb'}

License
-------

GPLv3

Author Information
------------------

Pablo Escobar
