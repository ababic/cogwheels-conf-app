"""
Any setting you wish to support in your app must be defined here with a
sensible default value.

**DO:**

- Use upper case names for settings
- Feel free to use values of any built-in python type

**DON'T:**

- Prefix setting names with 'YOURAPP_' or similar (that isn't necessary here)
- Put all your configuration in one giant dictionary (that's just lazy!)


Django model settings
---------------------

For settings that refer to Django models, the default value should be a string
in the format 'app_name.Model', e.g.:

ORDER_ITEM_MODEL = 'yourproject.SimpleOrderItem'


Python module settings
----------------------

For settings that refer to Python modules, the default value should be an
'import path' string, e.g.:

DISCOUNTS_BACKEND = 'yourproject.discount_backends.simple'


Other importable python object settings
---------------------------------------

For settings that refer to classes, methods, or other importable Python
objects, the default value should be an 'object import path' string, e.g.:

EDIT_FORM = 'myapp.subapp.forms.DefaultEditForm'

ACTION_VIEW_CLASS = 'myapp.subapp.views.ActionView'
"""
