=================
community_mailbot
=================

The ``community_mailbot`` is a friendly bot that tells subscribers to LSST DM's legacy Mailman email lists about things happening on `community.lsst.org <http://community.lsst.org>`_.

Installation
------------

Create a virtual environment running Python 3.5, then::

    pip install git+https://github.com/lsst-sqre/community_mailbit.git@tickets/DM-3690


Getting started
---------------

You'll need to get API keys from community.lsst.org and Mandrill.
Set them to the following environment variables:

* ``$MANDRILL_KEY`` (note, use the API key for the ``community_mailbot`` subaccount)
* ``$DISCOURSE_KEY`` (the Discourse key should corresond to a user with sufficient permissions)
* ``$DISCOURSE_USER``

Optionally set ``$COMMUNITY_MAILBOT_CACHE`` to the location where you want the Mailbot to keep track of its sent topics.

``forward_discourse`` is the main script. To learn how to use it, run::

    forward_discourse --help

The help message describes a configuration JSON file that you should create that maps Discourse topics to destination email addresses.

Running tests
-------------

To run the test suite you'll need to clone the repository and run ``unittest``::

    git clone https://github.com/lsst-sqre/community_mailbot.git
    cd community_mailbot
    python -m unittest discover -s community_mailbot/tests


License
-------

Copyright 2015 AURA/LSST.

MIT licensed; see ``LICENSE`` file.
