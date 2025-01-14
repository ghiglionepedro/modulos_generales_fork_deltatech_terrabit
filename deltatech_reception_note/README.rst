========================
Deltatech reception_note
========================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:636620cc3406fc40b3c64acf2d49315110f5d1a17568400968da77235af47455
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-dhongu%2Fdeltatech-lightgray.png?logo=github
    :target: https://github.com/dhongu/deltatech/tree/15.0/deltatech_reception_note
    :alt: dhongu/deltatech

|badge1| |badge2| |badge3|

Features:
 - Creates new types of RFQ's: "RFQ only" and "Reception note"
 - RFQ only types cannot be validated, they can only be sent to the supplier
 - Reception note types can be validated, they decrement the quantities found in RFQ only types from the same supplier (until 0 qty remains). If not enough quantities found on RFQ's, an error is displayed. The quantity errors can be ignored by checking the "Ignore quantities" checkbox. A message wil be logged if any found

**Table of contents**

.. contents::
   :local:

Bug Tracker
===========

Bugs are tracked on `Terrabit Issues <https://www.terrabit.ro/helpdesk>`_.
In case of trouble, please check there if your issue has already been reported.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Terrabit
* Dan Stoica

Maintainers
~~~~~~~~~~~

.. |maintainer-dhongu| image:: https://github.com/dhongu.png?size=40px
    :target: https://github.com/dhongu
    :alt: dhongu

Current maintainer:

|maintainer-dhongu| 

This module is part of the `dhongu/deltatech <https://github.com/dhongu/deltatech/tree/15.0/deltatech_reception_note>`_ project on GitHub.

You are welcome to contribute.
