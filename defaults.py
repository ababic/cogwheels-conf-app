"""
Any setting you wish to support in your app must be defined here with a
sensible default value.

-   The variable names for your settings should be in upper case
    (e.g. SOME_SETTING).
-   There's no need to prefix setting names with "YOURAPP_" or similar here.
    Cogwheels will take care of adding this prefix automatically when it is
    useful.
-   You can use any native Python type as a value (e.g. string, int, boolean,
    float, list, tuple, dict, date, time), but try to stick to well-known types
    that are easy for your app's users to define when they want to override
    something.
-   It's absolutely fine to use dictionaries to allow overriding of more
    complicated features, but try to avoid grouping together unrelated bits of
    configuration into larger dictionaries when they would make more sense as
    separate settings.

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
