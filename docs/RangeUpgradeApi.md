# electrificationutils.RangeUpgradeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**range_upgrade_range_upgrade_v1_get**](RangeUpgradeApi.md#range_upgrade_range_upgrade_v1_get) | **GET** /range_upgrade/v1/ | Range Upgrade


# **range_upgrade_range_upgrade_v1_get**
> List[EnergyTradeoff] range_upgrade_range_upgrade_v1_get(current_fuel, occupants)

Range Upgrade

Analyze the potential energy usage effects of a range upgrade.  We assume that the caller is contemplating replacing a natural gas or propane-burning range with an electric one. Based on the fuel their current range uses and the number of occupants in their household, we estimate how the use of electricity, natural gas, and propane will be likely to change under three different scenarios.  The scenarios are low, medium, and high use, which correspond to using a range 80% as much as a typical household, exactly as much as a typical household, and 120% as much as a typical household.  Parameters ---------- current_fuel     The currently used fuel. occupants     the number of occupants in the household.  Returns -------     Changes in energy use across a number of fuels.

### Example


```python
import electrificationutils
from electrificationutils.models.energy_tradeoff import EnergyTradeoff
from electrificationutils.models.range_fuel_type import RangeFuelType
from electrificationutils.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = electrificationutils.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with electrificationutils.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = electrificationutils.RangeUpgradeApi(api_client)
    current_fuel = electrificationutils.RangeFuelType() # RangeFuelType | The fuel used by the current range.
    occupants = 56 # int | The number of occupants in the household.

    try:
        # Range Upgrade
        api_response = api_instance.range_upgrade_range_upgrade_v1_get(current_fuel, occupants)
        print("The response of RangeUpgradeApi->range_upgrade_range_upgrade_v1_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RangeUpgradeApi->range_upgrade_range_upgrade_v1_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **current_fuel** | [**RangeFuelType**](.md)| The fuel used by the current range. | 
 **occupants** | **int**| The number of occupants in the household. | 

### Return type

[**List[EnergyTradeoff]**](EnergyTradeoff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

