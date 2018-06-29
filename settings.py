import sys

from cogwheels import BaseAppSettingsHelper


class MyAppSettingsHelper(BaseAppSettingsHelper):
    pass


# See: https://mail.python.org/pipermail/python-ideas/2012-May/014969.html
sys.modules[__name__] = MyAppSettingsHelper()
