# coding: utf-8

"""
    Common Fate

    Common Fate API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from commonfate.paths.api_v1_admin_providersetups_providersetup_id_complete.post import AdminCompleteProvidersetup
from commonfate.paths.api_v1_admin_access_rules.post import AdminCreateAccessRule
from commonfate.paths.api_v1_admin_groups.post import AdminCreateGroup
from commonfate.paths.api_v1_admin_users.post import AdminCreateUser
from commonfate.paths.api_v1_admin_access_rules_rule_id.get import AdminGetAccessRule
from commonfate.paths.api_v1_admin_access_rules_rule_id_versions_version.get import AdminGetAccessRuleVersion
from commonfate.paths.api_v1_admin_access_rules_rule_id_versions.get import AdminGetAccessRuleVersions
from commonfate.paths.api_v1_admin_deployment_version.get import AdminGetDeploymentVersion
from commonfate.paths.api_v1_admin_groups_group_id.get import AdminGetGroup
from commonfate.paths.api_v1_admin_providers_provider_id.get import AdminGetProvider
from commonfate.paths.api_v1_admin_providers_provider_id_args.get import AdminGetProviderArgs
from commonfate.paths.api_v1_admin_providersetups_providersetup_id.get import AdminGetProvidersetup
from commonfate.paths.api_v1_admin_providersetups_providersetup_id_instructions.get import AdminGetProvidersetupInstructions
from commonfate.paths.api_v1_admin_users.get import AdminGetUsers
from commonfate.paths.api_v1_admin_identity.get import AdminIdentityConfiguration
from commonfate.paths.api_v1_admin_identity_sync.post import AdminIdentitySync
from commonfate.paths.api_v1_admin_access_rules.get import AdminListAccessRules
from commonfate.paths.api_v1_admin_groups.get import AdminListGroups
from commonfate.paths.api_v1_admin_providers_provider_id_args_arg_id_options.get import AdminListProviderArgOptions
from commonfate.paths.api_v1_admin_providers.get import AdminListProviders
from commonfate.paths.api_v1_admin_providersetups.get import AdminListProvidersetups
from commonfate.paths.api_v1_admin_requests.get import AdminListRequests
from commonfate.paths.api_v1_admin_providersetups_providersetup_id_steps_step_index_complete.put import AdminSubmitProvidersetupStep
from commonfate.paths.api_v1_admin_access_rules_rule_id.put import AdminUpdateAccessRule
from commonfate.paths.api_v1_admin_groups_group_id.put import AdminUpdateGroup
from commonfate.paths.api_v1_admin_users_user_id.post import AdminUpdateUser
from commonfate.paths.api_v1_admin_providersetups_providersetup_id_validate.post import AdminValidateProvidersetup


class AdminApi(
    AdminCompleteProvidersetup,
    AdminCreateAccessRule,
    AdminCreateGroup,
    AdminCreateUser,
    AdminGetAccessRule,
    AdminGetAccessRuleVersion,
    AdminGetAccessRuleVersions,
    AdminGetDeploymentVersion,
    AdminGetGroup,
    AdminGetProvider,
    AdminGetProviderArgs,
    AdminGetProvidersetup,
    AdminGetProvidersetupInstructions,
    AdminGetUsers,
    AdminIdentityConfiguration,
    AdminIdentitySync,
    AdminListAccessRules,
    AdminListGroups,
    AdminListProviderArgOptions,
    AdminListProviders,
    AdminListProvidersetups,
    AdminListRequests,
    AdminSubmitProvidersetupStep,
    AdminUpdateAccessRule,
    AdminUpdateGroup,
    AdminUpdateUser,
    AdminValidateProvidersetup,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass