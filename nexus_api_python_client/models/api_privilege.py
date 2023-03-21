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


class ApiPrivilege(object):
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
        'type': 'str',
        'name': 'str',
        'description': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'description': 'description',
        'read_only': 'readOnly'
    }

    def __init__(self, type=None, name=None, description=None, read_only=None, local_vars_configuration=None):  # noqa: E501
        """ApiPrivilege - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._description = None
        self._read_only = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if read_only is not None:
            self.read_only = read_only

    @property
    def type(self):
        """Gets the type of this ApiPrivilege.  # noqa: E501

        The type of privilege, each type covers different portions of the system. External values supplied to this will be ignored by the system.  # noqa: E501

        :return: The type of this ApiPrivilege.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiPrivilege.

        The type of privilege, each type covers different portions of the system. External values supplied to this will be ignored by the system.  # noqa: E501

        :param type: The type of this ApiPrivilege.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this ApiPrivilege.  # noqa: E501

        The name of the privilege.  This value cannot be changed.  # noqa: E501

        :return: The name of this ApiPrivilege.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPrivilege.

        The name of the privilege.  This value cannot be changed.  # noqa: E501

        :param name: The name of this ApiPrivilege.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[a-zA-Z0-9\-]{1}[a-zA-Z0-9_\-\.]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-]{1}[a-zA-Z0-9_\-\.]*$/`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiPrivilege.  # noqa: E501


        :return: The description of this ApiPrivilege.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiPrivilege.


        :param description: The description of this ApiPrivilege.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def read_only(self):
        """Gets the read_only of this ApiPrivilege.  # noqa: E501

        Indicates whether the privilege can be changed. External values supplied to this will be ignored by the system.  # noqa: E501

        :return: The read_only of this ApiPrivilege.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this ApiPrivilege.

        Indicates whether the privilege can be changed. External values supplied to this will be ignored by the system.  # noqa: E501

        :param read_only: The read_only of this ApiPrivilege.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

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
        if not isinstance(other, ApiPrivilege):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiPrivilege):
            return True

        return self.to_dict() != other.to_dict()
