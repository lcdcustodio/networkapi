NetworkApi
===========

Available Features
==================

* IP address management
* RESTful API
* IPv4 only

------------

Project Goals
=============

* Provide solution able to manage Network IP Addresses  through web interface and API


------------

Installation
===========================

Install version using the following commands:

.. code-block:: shell

    git clone https://github.com/lcdcustodio/networkapi.git
    cd networkapi
    pip install -r requirements.txt


Launch the server:

.. code-block:: shell

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver


You can access the admin interface at `http://127.0.0.1:8000/admin/`.

Run Tests
===========================

Run the test suite:

.. code-block:: shell

    python manage.py test





RESTful API Documentation
=========================


`Documentation <http://ec2-52-90-92-199.compute-1.amazonaws.com/html/>`_