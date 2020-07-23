# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "user_login"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/login/v1/"

from .test_case_01 import TestCase01UserLoginAPITestCase

__all__ = [
    "TestCase01UserLoginAPITestCase"
]
