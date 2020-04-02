netapi
===========

Available Features
==================

* IPv4 IP address management
* RESTful API to for CRUD operations

------------

Project Goals
=============

* provide RESTful API solution able to manage Network IP Addresses


------------

Install Development Version
===========================

Install the development version using the following commands:

.. code-block:: shell

    git clone https://github.com/lcdcustodio/networkapi.git
    cd netapi
    pip install -r requirements.txt


Launch the development sever:

.. code-block:: shell

    python manage.py makemigrations    
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

You can access the admin interface at `http://127.0.0.1:8000/admin/`.


RESTful API Documentation
=========================


`Documentation <http://ec2-52-90-92-199.compute-1.amazonaws.com/html/>`_