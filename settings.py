import sys

from cogwheels import BaseAppSettingsHelper


class AppSettingsHelper(BaseAppSettingsHelper):
    pass


sys.modules[__name__] = AppSettingsHelper()
