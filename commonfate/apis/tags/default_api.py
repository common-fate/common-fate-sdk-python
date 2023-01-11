# coding: utf-8

"""
    Common Fate

    Common Fate API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from commonfate.paths.api_v1_admin_access_rules_rule_id_archive.post import AdminArchiveAccessRule
from commonfate.paths.api_v1_admin_providersetups.post import AdminCreateProvidersetup
from commonfate.paths.api_v1_admin_groups_group_id.delete import AdminDeleteGroup
from commonfate.paths.api_v1_admin_providersetups_providersetup_id.delete import AdminDeleteProvidersetup
from commonfate.paths.api_v1_access_rules_lookup.get import UserAccessRuleLookup
from commonfate.paths.api_v1_favorites.post import UserCreateFavorite
from commonfate.paths.api_v1_favorites_id.delete import UserDeleteFavorite
from commonfate.paths.api_v1_favorites_id.get import UserGetFavorite
from commonfate.paths.api_v1_favorites.get import UserListFavorites
from commonfate.paths.api_v1_requests_past.get import UserListRequestsPast
from commonfate.paths.api_v1_requests_upcoming.get import UserListRequestsUpcoming
from commonfate.paths.api_v1_favorites_id.put import UserUpdateFavorite


class DefaultApi(
    AdminArchiveAccessRule,
    AdminCreateProvidersetup,
    AdminDeleteGroup,
    AdminDeleteProvidersetup,
    UserAccessRuleLookup,
    UserCreateFavorite,
    UserDeleteFavorite,
    UserGetFavorite,
    UserListFavorites,
    UserListRequestsPast,
    UserListRequestsUpcoming,
    UserUpdateFavorite,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
