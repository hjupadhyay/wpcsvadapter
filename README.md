wpcsvadapter
============

Insert wordpress posts via python from a csv file


Intent:
======

Wordpress CSV adapter is a basic python script that
- Reads csv file from file system
- Creates posts to wordpress via XML-RPC
- CSV first column is taken as title
- Second column is the post content

USAGE:
======
- change the relevent details from the script (username and password etc.)
- python wpadapter.py from command line (terminal)

TODO:
=====
- A lot to do ...
- Pass settings as CLI arguments
- Remove credentials from versioning (how to ?)
- Make CSV column specification available on script
- Usage help on CLI (--version and --help etc.)

REQUEST:
========
Please fork and suggest improvements (Pull requests are most welcome)