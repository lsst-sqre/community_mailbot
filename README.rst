=================
community_mailbot
=================

.. image:: https://img.shields.io/pypi/v/community_mailbot.svg

The ``community_mailbot`` is a friendly bot that tells subscribers to LSST DM's legacy Mailman email lists about things happening on `community.lsst.org <http://community.lsst.org>`_.

The bot likes to be awakened regularly by ``cron``; each time it will ask the Discourse server about latest messages in different categories that the bot tracks (you can set this with a simple ``config.json`` file).
If there is are new topics, ``community_mailbot`` will send an email to the appropriate email lists using its buddy, `Mandrill <http://mandrillapp.com>`_.
Before the bot goes back to sleep, it keeps note of all the topics it's emailed already in a simple JSON cache file.

Installation
------------

Create a virtual environment running Python 3.5, then:

.. code-block:: bash

   pip install community_mailbot

Running the community mailbot
-----------------------------

Keys to the Kingdom
~~~~~~~~~~~~~~~~~~~

You'll need to get API keys from community.lsst.org and Mandrill.
Set them to the following environment variables:

* ``$MANDRILL_KEY`` (note, use the API key for the ``community_mailbot`` subaccount)
* ``$DISCOURSE_KEY`` (the Discourse key should correspond to a user with sufficient permissions)
* ``$DISCOURSE_USER``

Optionally set ``$COMMUNITY_MAILBOT_CACHE`` to the location where you want the Mailbot to keep track of its topics it has forwarded.

Setup Topic → Email Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To setup how Discourse categories are mapped to recipient email addresses, you need to know the integer IDs for each relevant category.
To get these, run the included script:

.. code-block:: bash

   discourse_categories

If you set the aforementioned environment variables, you won't need to provide any arguments to the script.

Next, create a ``config.json`` file.
It's a simple hash structure; each key-value pair is the Discourse category ID and a list of email recipients for that category.
The general format is:

.. code-block:: json

   {
       "<id>": [{"email": "<email address>",
                 "name": "<recipient name>",
                 "type": "to"}],
   }

The structure of the ``dict`` in the value matches the `Mandrill send-template API`_.
The ``"type"`` field should typically be ``"to"``, but could also be ``"cc"`` or ``"bcc"``.

.. _`Mandrill send-template API`: https://mandrillapp.com/api/docs/messages.python.html#method-send-template

Note that since the recipient information for each category is a ``list``, you can have multiple recipients.

Pre-cache old topics
~~~~~~~~~~~~~~~~~~~~

Before having the bot send emails, you'll want it to know about and ignore older messages.
To warm up the cache, we'll run the ``forward_discourse`` script with the ``--cache-only`` option.

.. code-block:: bash

   forward_discourse config.json --cache-only

Note that ``forward_discourse`` can configure itself with the environment variables you've already setup.
Run ``forward_discourse --help`` for the full set of options.

Set up a cron schedule
~~~~~~~~~~~~~~~~~~~~~~

The bot works best when it regularly monitors a Discourse site for new topics.
``cron`` is a great way to set this up.

It's useful to create a shell script to contain all of the script arguments.
For example, create a script called ``run_mailbot.sh``:

.. code-block:: bash

   #!/bin/bash
   source /home/ec2-user/.bash_profile
   source activate community_mailbot
   forward_discourse /home/ec2-user/config.json

   echo "$(date) Ran forward_discourse"

This script sets up up the shell environment, loads a Python environment, and then runs the mailbot.

Then instruct ``cron`` to run this script every 10 minutes

First, open the ``crontab`` in your terminal

.. code-block:: bash

   crontab -e

And add a line for the bot

.. code-block:: bash

    */10 * * * * /home/ec2-user/run_mailbot.sh

Then sit back and watch the email flow.

Development
-----------

To develop on the ``community_mailbot``, you'll need to clone the repository and install a development copy (preferably in a ``virtualenv``):

.. code-block:: bash

   git clone https://github.com/lsst-sqre/community_mailbot.git
   cd community_mailbot
   python setup.py develop

To run the test suite:

.. code-block:: bash

    python -m unittest discover -s community_mailbot/tests


Rough Spots
-----------

The ``community_mailbot`` is meant to be fairly general and usable for any Discourse installation.

*However*, beware that the Mandrill email template information is current hard-coded.
Ideally this would be user-configurable.


License
-------

Copyright 2015 AURA/LSST.

MIT licensed; see ``LICENSE`` file.
