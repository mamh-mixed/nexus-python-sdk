# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.20.1-01
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from nexus_api_python_client.configuration import Configuration


class PageTaskXO(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'items': 'list[TaskXO]',
        'continuation_token': 'str'
    }

    attribute_map = {
        'items': 'items',
        'continuation_token': 'continuationToken'
    }

    def __init__(self, items=None, continuation_token=None, local_vars_configuration=None):  # noqa: E501
        """PageTaskXO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._items = None
        self._continuation_token = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if continuation_token is not None:
            self.continuation_token = continuation_token

    @property
    def items(self):
        """Gets the items of this PageTaskXO.  # noqa: E501


        :return: The items of this PageTaskXO.  # noqa: E501
        :rtype: list[TaskXO]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PageTaskXO.


        :param items: The items of this PageTaskXO.  # noqa: E501
        :type: list[TaskXO]
        """

        self._items = items

    @property
    def continuation_token(self):
        """Gets the continuation_token of this PageTaskXO.  # noqa: E501


        :return: The continuation_token of this PageTaskXO.  # noqa: E501
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this PageTaskXO.


        :param continuation_token: The continuation_token of this PageTaskXO.  # noqa: E501
        :type: str
        """

        self._continuation_token = continuation_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PageTaskXO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageTaskXO):
            return True

        return self.to_dict() != other.to_dict()