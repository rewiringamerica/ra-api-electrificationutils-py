# electrificationutils.HealthImpactsApi

All URIs are relative to *http://api.rewiringamerica.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_health_impacts**](HealthImpactsApi.md#query_health_impacts) | **GET** /api/v1/health_impacts/ | Query Health Impacts


# **query_health_impacts**
> object query_health_impacts(metrics, upgrade, county_fips=county_fips, state=state, groupby=groupby)

Query Health Impacts

Query and aggregate results of Rewiring America's health impacts modeling data.

Rewiring America's health impacts research models the health and air quality benefits of residential electrification. This endpoint allows users to filter data by county, state, and upgrade options to return health and air quality benefits. It aggregates data based on specified pollutant and health-related metrics and provides the option to disaggregate results by specific housing characteristics enumerated below. Results describe the total annual benefit to the continental US.

[READ THE COMPANION REPORT](https://www.rewiringamerica.org/research/home-electrification-health-benefits)


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
    host = "http://api.rewiringamerica.org"
)


# Enter a context with an instance of the API client
with electrificationutils.ApiClient(configuration) as api_client:
    api_client.default_headers['Authorization']= 'Bearer YOUR API TOKEN HERE'
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
 **metrics** | [**List[Metrics]**](Metrics.md)| A list of pollutant emissions metrics or economic valuations to aggregate. Valid inputs: `pm25-pri_kg_delta`, `nh3_kg_delta`, `nox_kg_delta`, `voc_kg_delta`, `so2_kg_delta`, `premature_mortality_incidence_delta`, `premature_mortality_valuation_dollars_delta` | 
 **upgrade** | [**List[UpgradeOption]**](UpgradeOption.md)| A list of electrification upgrades to filter by. Valid inputs: `hp_dryer`, `hp_water_heater`, `med_eff_hp_hers_sizing_no_setback_basic_enclosure`, `med_eff_hp_hers_sizing_no_setback`, `electric_resistance_dryer` | 
 **state** | [**List[str]**](str.md)| A list of two-letter state abbreviations to filter by. | [optional] [default to []]
 **county_fips** | [**List[str]**](str.md)| A list of three-digit county FIPS codes to filter by. See [here](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt) for a complete list. Inputting a `*` will return all counties. If a specific three-digit county FIPS is input, a specific two-letter state abbreviation must also be specified.| [optional] [default to []]
 **groupby** | [**List[GroupBy]**](GroupBy.md)| A list of housing characteristics by which to further disaggregate results. | [optional] [default to []]


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

