Dynamic VAT Label for Partners
==============================

Overview
--------
In many business environments, different types of partners require different identification numbers:

- Companies → VAT / Tax ID
- Individuals → National ID
- Foreign partners → Passport ID

Odoo uses a single "VAT" field for all cases, which can be confusing for users and lead to incorrect data entry.

This module dynamically updates the label and placeholder of the VAT field based on the partner type.

Features
--------
- Automatically changes VAT label based on partner type
- Supports:
  - Company → Tax ID
  - Individual → National ID
  - Foreign → Passport ID
- No configuration required
- Lightweight and fast
- Fully integrated with Contacts module

Usage
-----
1. Go to Contacts
2. Open or create a partner
3. Change the partner type
4. The VAT label will update automatically

Technical Details
-----------------
- Uses JavaScript patching to dynamically modify the UI
- Extends the standard `res.partner` form view
- No impact on backend logic or database structure

Dependencies
------------
- Contacts

License
-------
LGPL-3

Author
------
Mahmoud Magdy
https://github.com/mahmoudmagdy146
