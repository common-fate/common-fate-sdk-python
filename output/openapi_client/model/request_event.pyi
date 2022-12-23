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


class RequestEvent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "createdAt",
            "requestId",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            requestId = schemas.StrSchema
            createdAt = schemas.StrSchema
            actor = schemas.StrSchema
        
            @staticmethod
            def fromStatus() -> typing.Type['RequestStatus']:
                return RequestStatus
        
            @staticmethod
            def toStatus() -> typing.Type['RequestStatus']:
                return RequestStatus
        
            @staticmethod
            def fromTiming() -> typing.Type['RequestTiming']:
                return RequestTiming
        
            @staticmethod
            def toTiming() -> typing.Type['RequestTiming']:
                return RequestTiming
            
            
            class fromGrantStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
                
                @schemas.classproperty
                def REVOKED(cls):
                    return cls("REVOKED")
                
                @schemas.classproperty
                def EXPIRED(cls):
                    return cls("EXPIRED")
            
            
            class toGrantStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
                
                @schemas.classproperty
                def REVOKED(cls):
                    return cls("REVOKED")
                
                @schemas.classproperty
                def EXPIRED(cls):
                    return cls("EXPIRED")
            grantCreated = schemas.BoolSchema
            requestCreated = schemas.BoolSchema
            grantFailureReason = schemas.StrSchema
            recordedEvent = schemas.DictSchema
            __annotations__ = {
                "id": id,
                "requestId": requestId,
                "createdAt": createdAt,
                "actor": actor,
                "fromStatus": fromStatus,
                "toStatus": toStatus,
                "fromTiming": fromTiming,
                "toTiming": toTiming,
                "fromGrantStatus": fromGrantStatus,
                "toGrantStatus": toGrantStatus,
                "grantCreated": grantCreated,
                "requestCreated": requestCreated,
                "grantFailureReason": grantFailureReason,
                "recordedEvent": recordedEvent,
            }
    
    createdAt: MetaOapg.properties.createdAt
    requestId: MetaOapg.properties.requestId
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestId"]) -> MetaOapg.properties.requestId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actor"]) -> MetaOapg.properties.actor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromStatus"]) -> 'RequestStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toStatus"]) -> 'RequestStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromTiming"]) -> 'RequestTiming': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toTiming"]) -> 'RequestTiming': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromGrantStatus"]) -> MetaOapg.properties.fromGrantStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toGrantStatus"]) -> MetaOapg.properties.toGrantStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grantCreated"]) -> MetaOapg.properties.grantCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestCreated"]) -> MetaOapg.properties.requestCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grantFailureReason"]) -> MetaOapg.properties.grantFailureReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recordedEvent"]) -> MetaOapg.properties.recordedEvent: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "requestId", "createdAt", "actor", "fromStatus", "toStatus", "fromTiming", "toTiming", "fromGrantStatus", "toGrantStatus", "grantCreated", "requestCreated", "grantFailureReason", "recordedEvent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestId"]) -> MetaOapg.properties.requestId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actor"]) -> typing.Union[MetaOapg.properties.actor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromStatus"]) -> typing.Union['RequestStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toStatus"]) -> typing.Union['RequestStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromTiming"]) -> typing.Union['RequestTiming', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toTiming"]) -> typing.Union['RequestTiming', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromGrantStatus"]) -> typing.Union[MetaOapg.properties.fromGrantStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toGrantStatus"]) -> typing.Union[MetaOapg.properties.toGrantStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grantCreated"]) -> typing.Union[MetaOapg.properties.grantCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestCreated"]) -> typing.Union[MetaOapg.properties.requestCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grantFailureReason"]) -> typing.Union[MetaOapg.properties.grantFailureReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recordedEvent"]) -> typing.Union[MetaOapg.properties.recordedEvent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "requestId", "createdAt", "actor", "fromStatus", "toStatus", "fromTiming", "toTiming", "fromGrantStatus", "toGrantStatus", "grantCreated", "requestCreated", "grantFailureReason", "recordedEvent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, ],
        requestId: typing.Union[MetaOapg.properties.requestId, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        actor: typing.Union[MetaOapg.properties.actor, str, schemas.Unset] = schemas.unset,
        fromStatus: typing.Union['RequestStatus', schemas.Unset] = schemas.unset,
        toStatus: typing.Union['RequestStatus', schemas.Unset] = schemas.unset,
        fromTiming: typing.Union['RequestTiming', schemas.Unset] = schemas.unset,
        toTiming: typing.Union['RequestTiming', schemas.Unset] = schemas.unset,
        fromGrantStatus: typing.Union[MetaOapg.properties.fromGrantStatus, str, schemas.Unset] = schemas.unset,
        toGrantStatus: typing.Union[MetaOapg.properties.toGrantStatus, str, schemas.Unset] = schemas.unset,
        grantCreated: typing.Union[MetaOapg.properties.grantCreated, bool, schemas.Unset] = schemas.unset,
        requestCreated: typing.Union[MetaOapg.properties.requestCreated, bool, schemas.Unset] = schemas.unset,
        grantFailureReason: typing.Union[MetaOapg.properties.grantFailureReason, str, schemas.Unset] = schemas.unset,
        recordedEvent: typing.Union[MetaOapg.properties.recordedEvent, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RequestEvent':
        return super().__new__(
            cls,
            *args,
            createdAt=createdAt,
            requestId=requestId,
            id=id,
            actor=actor,
            fromStatus=fromStatus,
            toStatus=toStatus,
            fromTiming=fromTiming,
            toTiming=toTiming,
            fromGrantStatus=fromGrantStatus,
            toGrantStatus=toGrantStatus,
            grantCreated=grantCreated,
            requestCreated=requestCreated,
            grantFailureReason=grantFailureReason,
            recordedEvent=recordedEvent,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.request_status import RequestStatus
from openapi_client.model.request_timing import RequestTiming
