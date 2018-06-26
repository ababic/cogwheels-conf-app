import sys

from cogwheels import BaseAppSettingsHelper


class MyAppSettingsHelper(BaseAppSettingsHelper):
    pass


sys.modules[__name__] = MyAppSettingsHelper()
