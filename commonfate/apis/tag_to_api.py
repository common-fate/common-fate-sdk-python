import typing_extensions

from commonfate.apis.tags import TagValues
from commonfate.apis.tags.end_user_api import EndUserApi
from commonfate.apis.tags.admin_api import AdminApi
from commonfate.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.END_USER: EndUserApi,
        TagValues.ADMIN: AdminApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.END_USER: EndUserApi,
        TagValues.ADMIN: AdminApi,
        TagValues.DEFAULT: DefaultApi,
    }
)
