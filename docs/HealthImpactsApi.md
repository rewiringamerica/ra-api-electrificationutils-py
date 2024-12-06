# electrificationutils.HealthImpactsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_health_impacts**](HealthImpactsApi.md#query_health_impacts) | **GET** /api/v1/health_impacts/ | Query Health Impacts


# **query_health_impacts**
> object query_health_impacts(metrics, upgrade, county_fips=county_fips, state=state, groupby=groupby)

Query Health Impacts

Query and aggregate results of Rewiring America's health impacts modeling data.  This endpoint allows users to filter data by county, state, and upgrade options. It aggregates data based on specified pollutant and health-related metrics and provides the option to group results by user-defined columns.  Parameters ---------- county_fips : List[str], optional     A list of county FIPS codes to filter the data by. Defaults to an empty list.     Example: ['001', '075'].  state : List[str], optional     A list of states to filter the data by. Defaults to an empty list.     Example: ['CA', 'TX'].  upgrade : List[str], required     A list of upgrade options to filter the data by. Defaults to an empty list.     Example: ['med_eff_hp_hers_sizing_no_setback', 'hp_dryer'].  metrics : List[str], required     A list of pollutant or economic valuation metrics to aggregate in the query.     This field is required.     Example: ['nh3_kg_delta', 'premature_mortality_incidence_delta'].  groupby : List[str], optional     A list of columns to group the query results by. Defaults to an empty list.     Example: ['in_sqft_bin', 'acs_housing_type'].  Returns ------- dict     A dictionary containing the aggregated health data, with results filtered and grouped     based on the provided parameters.

### Example


```python
import electrificationutils
from electrificationutils.models.group_by import GroupBy
from electrificationutils.models.metrics import Metrics
from electrificationutils.models.upgrade_option import UpgradeOption
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
    api_instance = electrificationutils.HealthImpactsApi(api_client)
    metrics = [electrificationutils.Metrics()] # List[Metrics] | A list of pollutant emissions metrics or economic valuations to aggregate.
    upgrade = [electrificationutils.UpgradeOption()] # List[UpgradeOption] | A list of upgrades to filter by.
    county_fips = [] # List[str] | A list of three-digit county FIPS codes to filter by. (optional) (default to [])
    state = [] # List[str] | A list of state abbreviations to filter by. (optional) (default to [])
    groupby = [] # List[GroupBy] | A list of columns to group by. (optional) (default to [])

    try:
        # Query Health Impacts
        api_response = api_instance.query_health_impacts(metrics, upgrade, county_fips=county_fips, state=state, groupby=groupby)
        print("The response of HealthImpactsApi->query_health_impacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthImpactsApi->query_health_impacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics** | [**List[Metrics]**](Metrics.md)| A list of pollutant emissions metrics or economic valuations to aggregate. | 
 **upgrade** | [**List[UpgradeOption]**](UpgradeOption.md)| A list of upgrades to filter by. | 
 **county_fips** | [**List[str]**](str.md)| A list of three-digit county FIPS codes to filter by. | [optional] [default to []]
 **state** | [**List[str]**](str.md)| A list of state abbreviations to filter by. | [optional] [default to []]
 **groupby** | [**List[GroupBy]**](GroupBy.md)| A list of columns to group by. | [optional] [default to []]

### Return type

**object**

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

