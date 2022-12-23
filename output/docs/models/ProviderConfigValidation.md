# openapi_client.model.provider_config_validation.ProviderConfigValidation

A validation against the configuration values of the Access Provider.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A validation against the configuration values of the Access Provider. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[fieldsValidated](#fieldsValidated)** | list, tuple,  | tuple,  | The particular config fields validated, if any. | 
**name** | str,  | str,  |  | 
**id** | str,  | str,  | The ID of the validation, such as &#x60;list-sso-users&#x60;. | 
**[logs](#logs)** | list, tuple,  | tuple,  |  | 
**status** | str,  | str,  | The status of the validation. | must be one of ["IN_PROGRESS", "SUCCESS", "PENDING", "ERROR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fieldsValidated

The particular config fields validated, if any.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The particular config fields validated, if any. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# logs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Log**](Log.md) | [**Log**](Log.md) | [**Log**](Log.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
