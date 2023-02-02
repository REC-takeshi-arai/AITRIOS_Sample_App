# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.paths.api_v1_devices_device_id_inferenceresults_collectstart import post  # noqa: E501
from aitrios_console_rest_client_sdk_primitive import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1DevicesDeviceIdInferenceresultsCollectstart(ApiTestMixin, unittest.TestCase):
    """
    ApiV1DevicesDeviceIdInferenceresultsCollectstart unit test stubs
        StartUploadInferenceResult  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
