# coding: utf-8

"""
    Common Fate

    Common Fate API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class Groups(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class additional_properties(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                
                @staticmethod
                def items() -> typing.Type['GroupOption']:
                    return GroupOption
        
            def __new__(
                cls,
                arg: typing.Union[typing.Tuple['GroupOption'], typing.List['GroupOption']],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'additional_properties':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> 'GroupOption':
                return super().__getitem__(i)
    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
    ) -> 'Groups':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.group_option import GroupOption