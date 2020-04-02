
NetworkAPI's documentation!
================================

RESTful API
=====================

RESTful API to for CRUD operations. Designed for IPv4 only Networks.


GET ALL
.....

Returns all Networks info.::

    GET /api/v1/network/

Response.::

    {
        "id": "ip_address-id",
        "ip_address": "ip_address",
        "subnet": "subnet with cidr",
        "description": "optional description"
    }
    

SEARCH
.....

Searchs a particular IP address info.::

    GET /api/v1/network?ip_address=<ip_address>


POST
.....

Create a new IP Address.::

    POST /api/v1/network/new/

Post Parameters

===========    ========================================
Parameters       Description
===========    ========================================
ip_address     IPv4 address value
subnet         Subnet with CIDR notation
description    Optional description for the IP address
===========    ========================================


DELETE
.....

Delete an IP address instance..::

    DELETE /api/v1/network/<ip_address-id>


.. toctree::
   :maxdepth: 2
   
  


