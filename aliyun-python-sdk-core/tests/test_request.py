# coding=utf-8

import unittest

from aliyunsdkcore.request import AcsRequest, RpcRequest, RoaRequest, OssRequest, CommonRequest
from aliyunsdkcore.acs_exception.exceptions import ClientException

class TestRequest(unittest.TestCase):

    def test_rpc_request(self):
      r = RpcRequest("product", "version", "action_name")
      # accept format
      self.assertIsNone(r.get_accept_format())
      r.set_accept_format('json')
      self.assertEqual(r.get_accept_format(), "json")
      # action name
      self.assertEqual(r.get_action_name(), "action_name")
      r.set_action_name('new action name')
      self.assertEqual(r.get_action_name(), "new action name")
      # body params
      self.assertDictEqual(r.get_body_params(), {})
      r.set_body_params({'key': 'value'})
      self.assertDictEqual(r.get_body_params(), {'key': 'value'})
      r.add_body_params("key2", "value2")
      self.assertDictEqual(r.get_body_params(), {'key': 'value', 'key2': 'value2'})
      # content
      self.assertIsNone(r.get_content())
      r.set_content("content")
      self.assertEqual(r.get_content(), "content")
      # headers
      self.assertDictEqual(r.get_headers(), {'x-sdk-invoke-type': 'normal'})
      r.set_headers({})
      self.assertDictEqual(r.get_headers(), {})
      r.add_header("key", "value")
      self.assertDictEqual(r.get_headers(), {"key": "value"})
      # location endpoint type
      self.assertEqual(r.get_location_endpoint_type(), 'openAPI')
      ## no set_location_endpoint_type ??
      # location_service_code
      self.assertEqual(r.get_location_service_code(), None)
      r.set_location_service_code('new service code')
      self.assertEqual(r.get_location_service_code(), 'new service code')
      # method
      self.assertEqual(r.get_method(), 'GET')
      r.set_method('POST')
      self.assertEqual(r.get_method(), 'POST')
      # product
      self.assertEqual(r.get_product(), 'product')
      r.set_product('new-product')
      self.assertEqual(r.get_product(), 'new-product')
      # protocol_type
      self.assertEqual(r.get_protocol_type(), "http")
      r.set_protocol_type('https')
      self.assertEqual(r.get_protocol_type(), "https")
      # query params
      self.assertDictEqual(r.get_query_params(), {})
      r.set_query_params({'key':'value'})
      self.assertDictEqual(r.get_query_params(), {'key':'value'})
      r.add_query_param("key2", "value2")
      self.assertDictEqual(r.get_query_params(), {'key':'value', "key2": "value2"})
      # signed_header
      self.assertEqual(r.get_signed_header(), {})
      r.add_header("x-acs-xxx", "value")
      self.assertDictEqual(r.get_signed_header(), {"x-acs-xxx": "value"})
      # style
      self.assertEqual(r.get_style(), "RPC")
      # uri params
      self.assertEqual(r.get_uri_params(), None)
      r.set_uri_params({'user': "jacksontian"})
      self.assertDictEqual(r.get_uri_params(), {'user': 'jacksontian'})
      # uri pattern
      self.assertEqual(r.get_uri_pattern(), None)
      r.set_uri_pattern('/users/:userid')
      self.assertEqual(r.get_uri_pattern(), '/users/:userid')
      # url
      ## TODO: need to mock timestamp nonce
      # self.assertEqual(r.get_url("regionid", "accesskeyid", "secret"), "/?SignatureVersion=1.0&Format=json&key2=value2&RegionId=regionid&Signature=uZrjNVXfZARxwbMTO9Z%2B38eJxes%3D&AccessKeyId=accesskeyid&SignatureMethod=HMAC-SHA1&Version=version&key=value&Timestamp=2018-12-01T03%3A34%3A02Z&Action=new%20action%20name&SignatureNonce=1aeea4ad-cff0-4359-b595-9a1b2131bc0e&SignatureType=")
      # version
      self.assertEqual(r.get_version(), "version")
      r.set_version('2014-10-18')
      self.assertEqual(r.get_version(), "2014-10-18")

    def test_roa_request(self):
      r = RoaRequest("product", "version", "action_name")
      # accept format
      self.assertEqual(r.get_accept_format(), "RAW")
      r.set_accept_format('json')
      self.assertEqual(r.get_accept_format(), "json")
      # action name
      self.assertEqual(r.get_action_name(), "action_name")
      r.set_action_name('new action name')
      self.assertEqual(r.get_action_name(), "new action name")
      # body params
      self.assertDictEqual(r.get_body_params(), {})
      r.set_body_params({'key': 'value'})
      self.assertDictEqual(r.get_body_params(), {'key': 'value'})
      r.add_body_params("key2", "value2")
      self.assertDictEqual(r.get_body_params(), {'key': 'value', 'key2': 'value2'})
      # content
      self.assertIsNone(r.get_content())
      r.set_content("content")
      self.assertEqual(r.get_content(), "content")
      # headers
      self.assertDictEqual(r.get_headers(), {'x-sdk-invoke-type': 'normal'})
      r.set_headers({})
      self.assertDictEqual(r.get_headers(), {})
      r.add_header("key", "value")
      self.assertDictEqual(r.get_headers(), {"key": "value"})
      # location endpoint type
      self.assertEqual(r.get_location_endpoint_type(), 'openAPI')
      ## no set_location_endpoint_type ??
      # location_service_code
      self.assertEqual(r.get_location_service_code(), None)
      r.set_location_service_code('new service code')
      self.assertEqual(r.get_location_service_code(), 'new service code')
      # method
      self.assertEqual(r.get_method(), None)
      r.set_method('POST')
      self.assertEqual(r.get_method(), 'POST')
      # product
      self.assertEqual(r.get_product(), 'product')
      r.set_product('new-product')
      self.assertEqual(r.get_product(), 'new-product')
      # protocol_type
      self.assertEqual(r.get_protocol_type(), "http")
      r.set_protocol_type('https')
      self.assertEqual(r.get_protocol_type(), "https")
      # query params
      self.assertDictEqual(r.get_query_params(), {})
      r.set_query_params({'key':'value'})
      self.assertDictEqual(r.get_query_params(), {'key':'value'})
      r.add_query_param("key2", "value2")
      self.assertDictEqual(r.get_query_params(), {'key':'value', "key2": "value2"})
      # signed_header
      # self.assertEqual(r.get_signed_header("region_id", "access_key_id", "access_key_secret"), {})
      # r.add_header("x-acs-xxx", "value")
      # self.assertDictEqual(r.get_signed_header(), {"x-acs-xxx": "value"})
      # style
      self.assertEqual(r.get_style(), "ROA")
      # uri params
      self.assertEqual(r.get_uri_params(), None)
      r.set_uri_params({'user': "jacksontian"})
      self.assertDictEqual(r.get_uri_params(), {'user': 'jacksontian'})
      # uri pattern
      self.assertEqual(r.get_uri_pattern(), None)
      r.set_uri_pattern('/users/:userid')
      self.assertEqual(r.get_uri_pattern(), '/users/:userid')
      # url
      ## TODO: need to mock timestamp nonce
      # self.assertEqual(r.get_url("regionid", "accesskeyid", "secret"), "/?SignatureVersion=1.0&Format=json&key2=value2&RegionId=regionid&Signature=uZrjNVXfZARxwbMTO9Z%2B38eJxes%3D&AccessKeyId=accesskeyid&SignatureMethod=HMAC-SHA1&Version=version&key=value&Timestamp=2018-12-01T03%3A34%3A02Z&Action=new%20action%20name&SignatureNonce=1aeea4ad-cff0-4359-b595-9a1b2131bc0e&SignatureType=")
      # version
      self.assertEqual(r.get_version(), "version")
      r.set_version('2014-10-18')
      self.assertEqual(r.get_version(), "2014-10-18")

    def test_common_request(self):
      r = CommonRequest()
      # accept format
      self.assertIsNone(r.get_accept_format())
      r.set_accept_format('json')
      self.assertEqual(r.get_accept_format(), "json")
      # action name
      self.assertEqual(r.get_action_name(), None)
      r.set_action_name('new action name')
      self.assertEqual(r.get_action_name(), "new action name")
      # body params
      self.assertDictEqual(r.get_body_params(), {})
      r.set_body_params({'key': 'value'})
      self.assertDictEqual(r.get_body_params(), {'key': 'value'})
      r.add_body_params("key2", "value2")
      self.assertDictEqual(r.get_body_params(), {'key': 'value', 'key2': 'value2'})
      # content
      self.assertIsNone(r.get_content())
      r.set_content("content")
      self.assertEqual(r.get_content(), "content")
      # headers
      self.assertDictEqual(r.get_headers(), {'x-sdk-invoke-type': 'common'})
      r.set_headers({})
      self.assertDictEqual(r.get_headers(), {})
      r.add_header("key", "value")
      self.assertDictEqual(r.get_headers(), {"key": "value"})
      # location endpoint type
      print r.get_location_endpoint_type()
      self.assertEqual(r.get_location_endpoint_type(), 'openAPI')
      ## no set_location_endpoint_type ??
      # location_service_code
      self.assertEqual(r.get_location_service_code(), None)
      r.set_location_service_code('new service code')
      self.assertEqual(r.get_location_service_code(), 'new service code')
      # method
      self.assertEqual(r.get_method(), 'GET')
      r.set_method('POST')
      self.assertEqual(r.get_method(), 'POST')
      # product
      self.assertEqual(r.get_product(), None)
      r.set_product('new-product')
      self.assertEqual(r.get_product(), 'new-product')
      # protocol_type
      self.assertEqual(r.get_protocol_type(), "http")
      r.set_protocol_type('https')
      self.assertEqual(r.get_protocol_type(), "https")
      # query params
      self.assertDictEqual(r.get_query_params(), {})
      r.set_query_params({'key':'value'})
      self.assertDictEqual(r.get_query_params(), {'key':'value'})
      r.add_query_param("key2", "value2")
      self.assertDictEqual(r.get_query_params(), {'key':'value', "key2": "value2"})

      # uri params
      self.assertEqual(r.get_uri_params(), None)
      r.set_uri_params({'user': "jacksontian"})
      self.assertDictEqual(r.get_uri_params(), {'user': 'jacksontian'})
      # uri pattern
      self.assertEqual(r.get_uri_pattern(), None)
      r.set_uri_pattern('/users/:userid')
      self.assertEqual(r.get_uri_pattern(), '/users/:userid')
      # url
      ## TODO: need to mock timestamp nonce
      # self.assertEqual(r.get_url("regionid", "accesskeyid", "secret"), "/?SignatureVersion=1.0&Format=json&key2=value2&RegionId=regionid&Signature=uZrjNVXfZARxwbMTO9Z%2B38eJxes%3D&AccessKeyId=accesskeyid&SignatureMethod=HMAC-SHA1&Version=version&key=value&Timestamp=2018-12-01T03%3A34%3A02Z&Action=new%20action%20name&SignatureNonce=1aeea4ad-cff0-4359-b595-9a1b2131bc0e&SignatureType=")
      # version
      self.assertEqual(r.get_version(), None)
      r.set_version('2014-10-18')
      self.assertEqual(r.get_version(), "2014-10-18")

    def test_trans_to_acs_request_rpc(self):
      r = CommonRequest()
      # signed_header
      with self.assertRaises(ClientException) as ex:
        r.trans_to_acs_request()
      self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
      self.assertEqual(ex.exception.message, "common params [version] is required, cannot be empty")
      r.set_version("version")
      with self.assertRaises(ClientException) as ex:
        r.trans_to_acs_request()
      self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
      self.assertEqual(ex.exception.message, "At least one of [action] and [uri_pattern] has a value")
      r.set_action_name('action_name')
      with self.assertRaises(ClientException) as ex:
        r.trans_to_acs_request()
      self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
      self.assertEqual(ex.exception.message, "At least one of [domain] and [product_name] has a value")
      r.set_product('product')
      r.trans_to_acs_request()
      self.assertEqual(r.get_style(), "RPC")

    def test_trans_to_acs_request_to_roa(self):
      r = CommonRequest()
      # signed_header
      with self.assertRaises(ClientException) as ex:
        r.trans_to_acs_request()
      self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
      self.assertEqual(ex.exception.message, "common params [version] is required, cannot be empty")
      r.set_version("version")
      with self.assertRaises(ClientException) as ex:
        r.trans_to_acs_request()
      self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
      self.assertEqual(ex.exception.message, "At least one of [action] and [uri_pattern] has a value")
      r.set_uri_pattern("/users/:userid")
      with self.assertRaises(ClientException) as ex:
        r.trans_to_acs_request()
      self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
      self.assertEqual(ex.exception.message, "At least one of [domain] and [product_name] has a value")
      r.set_product('product')
      r.trans_to_acs_request()
      self.assertEqual(r.get_style(), "ROA")