# electrificationutils.GGRFHVACUpdateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ggrf_hvac_upgrade_btu_per_watt_hour_ggrf_hvac_upgrade_btu_per_watt_hour_v1_get**](GGRFHVACUpdateApi.md#ggrf_hvac_upgrade_btu_per_watt_hour_ggrf_hvac_upgrade_btu_per_watt_hour_v1_get) | **GET** /ggrf/hvac_upgrade/btu_per_watt_hour/v1/ | Ggrf Hvac Upgrade Btu Per Watt Hour
[**ggrf_hvac_upgrade_electric_to_electric_ggrf_hvac_upgrade_electric_to_electric_v1_get**](GGRFHVACUpdateApi.md#ggrf_hvac_upgrade_electric_to_electric_ggrf_hvac_upgrade_electric_to_electric_v1_get) | **GET** /ggrf/hvac_upgrade/electric-to-electric/v1/ | Ggrf Hvac Upgrade Electric To Electric
[**ggrf_hvac_upgrade_fossil_to_electric_ggrf_hvac_upgrade_fossil_to_electric_v1_get**](GGRFHVACUpdateApi.md#ggrf_hvac_upgrade_fossil_to_electric_ggrf_hvac_upgrade_fossil_to_electric_v1_get) | **GET** /ggrf/hvac_upgrade/fossil-to-electric/v1/ | Ggrf Hvac Upgrade Fossil To Electric


# **ggrf_hvac_upgrade_btu_per_watt_hour_ggrf_hvac_upgrade_btu_per_watt_hour_v1_get**
> float ggrf_hvac_upgrade_btu_per_watt_hour_ggrf_hvac_upgrade_btu_per_watt_hour_v1_get(electric_efficiency)

Ggrf Hvac Upgrade Btu Per Watt Hour

Look up the efficiency, in BTU/Wh for a given standard.  Parameters ---------- electric_efficiency     One of the standards-based measures of HVAC electrical efficiency.  Returns -------     The efficiency in BTU/wh for that standard.

### Example


```python
import electrificationutils
from electrificationutils.models.hvac_efficiency_electric_detailed import HvacEfficiencyElectricDetailed
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
    api_instance = electrificationutils.GGRFHVACUpdateApi(api_client)
    electric_efficiency = electrificationutils.HvacEfficiencyElectricDetailed() # HvacEfficiencyElectricDetailed | 

    try:
        # Ggrf Hvac Upgrade Btu Per Watt Hour
        api_response = api_instance.ggrf_hvac_upgrade_btu_per_watt_hour_ggrf_hvac_upgrade_btu_per_watt_hour_v1_get(electric_efficiency)
        print("The response of GGRFHVACUpdateApi->ggrf_hvac_upgrade_btu_per_watt_hour_ggrf_hvac_upgrade_btu_per_watt_hour_v1_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GGRFHVACUpdateApi->ggrf_hvac_upgrade_btu_per_watt_hour_ggrf_hvac_upgrade_btu_per_watt_hour_v1_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **electric_efficiency** | [**HvacEfficiencyElectricDetailed**](.md)|  | 

### Return type

**float**

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

# **ggrf_hvac_upgrade_electric_to_electric_ggrf_hvac_upgrade_electric_to_electric_v1_get**
> object ggrf_hvac_upgrade_electric_to_electric_ggrf_hvac_upgrade_electric_to_electric_v1_get(location_zip_code, new_unit_efficiency_percent, existing_efficiency_btu_per_watt_hour, annual_hvac_usage_kwh)

Ggrf Hvac Upgrade Electric To Electric

Calculate emissions savings for an HVAC update from and older electric technology to a newer one.  Replicate the calculation on the 'B1. HVAC update' tab of the 'Priority_Project_2_Net-Zero Building GGRF Calculator 10.18.24.xlsx' spreadsheet.  Parameters ---------- location_zip_code     The zip code where the upgrade is taking place. This is used to determine     how power is supplied and the emissions it generates. new_unit_efficiency_percent     The percent efficiency of the new electric HVAC unit. Value should be between     0 and 100 (not 0.0 and 1.0). existing_efficiency_btu_per_watt_hour     The efficiency of the existing unit that is being replaced. annual_hvac_usage_kwh     The annual usage of electricity by the previously existing electric HVAC equipment.  Returns -------     The old and new annual emissions of CO2e and their difference.

### Example


```python
import electrificationutils
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
    api_instance = electrificationutils.GGRFHVACUpdateApi(api_client)
    location_zip_code = 'location_zip_code_example' # str | 
    new_unit_efficiency_percent = 3.4 # float | 
    existing_efficiency_btu_per_watt_hour = 3.4 # float | 
    annual_hvac_usage_kwh = 3.4 # float | 

    try:
        # Ggrf Hvac Upgrade Electric To Electric
        api_response = api_instance.ggrf_hvac_upgrade_electric_to_electric_ggrf_hvac_upgrade_electric_to_electric_v1_get(location_zip_code, new_unit_efficiency_percent, existing_efficiency_btu_per_watt_hour, annual_hvac_usage_kwh)
        print("The response of GGRFHVACUpdateApi->ggrf_hvac_upgrade_electric_to_electric_ggrf_hvac_upgrade_electric_to_electric_v1_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GGRFHVACUpdateApi->ggrf_hvac_upgrade_electric_to_electric_ggrf_hvac_upgrade_electric_to_electric_v1_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_zip_code** | **str**|  | 
 **new_unit_efficiency_percent** | **float**|  | 
 **existing_efficiency_btu_per_watt_hour** | **float**|  | 
 **annual_hvac_usage_kwh** | **float**|  | 

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

# **ggrf_hvac_upgrade_fossil_to_electric_ggrf_hvac_upgrade_fossil_to_electric_v1_get**
> HvacUpdateResults ggrf_hvac_upgrade_fossil_to_electric_ggrf_hvac_upgrade_fossil_to_electric_v1_get(location_zip_code, existing_unit_efficiency_standard, new_unit_efficiency_percent, existing_efficiency_btu_per_watt_hour, existing_consumption_gallons_per_year=existing_consumption_gallons_per_year, existing_consumption_cubic_feet_per_year=existing_consumption_cubic_feet_per_year)

Ggrf Hvac Upgrade Fossil To Electric

Calculate emissions savings for an HVAC update from fossil fuel to electric.  Replicate the calculation on the 'B1. HVAC update' tab of the 'Priority_Project_2_Net-Zero Building GGRF Calculator 10.18.24.xlsx' spreadsheet.  The methodology taken from the spreadsheet is as follows: We start with the current fuel, efficiency, and annual usage of the current fuel. We then compute how many BTUs this corresponds to. We then go back in the other direction, assuming the same number of BTUs are used, then figure out based on the new equipment efficiency how many kWh of power is used. Now, using regionally adjusted lookup tables, we determine the amount of CO2e for the new system and the old, and take the difference.  Parameters ---------- location_zip_code     The zip code where the upgrade is taking place. This is used to determine     how power is supplied and the emissions it generates. existing_unit_efficiency_standard     The industry standard the machine being replaced is measured against. This     is used to determine the type of fuel the existing unit uses. new_unit_efficiency_percent     The percent efficiency of the new electric HVAC unit. Value should be between     0 and 100 (not 0.0 and 1.0). existing_efficiency_btu_per_watt_hour     The efficiency of the existing unit that is being replaced. existing_consumption_gallons_per_year     How much fuel the existing unit uses in gallons per year if it uses a fuel     that is measured in gallons (i.e. all fossil fuels except natural gas).     Either this value, or `existing_consumption_cubic_feet_per_year`, but not     both, should be specified. existing_consumption_cubic_feet_per_year     How much fuel the existing unit uses in cubic feet per year if it uses a fuel     that is measured in cubic feet (currently only natural gas).     Either this value, or `existing_consumption_gallons_per_year`, but not     both, should be specified.  Returns -------     The old and new annual emissions of CO2e and their difference.  Raises ------ ValueError     If an unacceptable combination of arguments are passed, for example,     `existing_unit_efficiency_standard=HvacEfficiencyFossilFuels.AFUE_GAS_FURNACE`     and `existing_consumption_gallons_per_year` is passed instead of     `existing_consumption_cubic_feet_per_year`.

### Example


```python
import electrificationutils
from electrificationutils.models.hvac_efficiency_fossil_fuels import HvacEfficiencyFossilFuels
from electrificationutils.models.hvac_update_results import HvacUpdateResults
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
    api_instance = electrificationutils.GGRFHVACUpdateApi(api_client)
    location_zip_code = 'location_zip_code_example' # str | 
    existing_unit_efficiency_standard = electrificationutils.HvacEfficiencyFossilFuels() # HvacEfficiencyFossilFuels | 
    new_unit_efficiency_percent = 3.4 # float | 
    existing_efficiency_btu_per_watt_hour = 3.4 # float | 
    existing_consumption_gallons_per_year = 3.4 # float |  (optional)
    existing_consumption_cubic_feet_per_year = 3.4 # float |  (optional)

    try:
        # Ggrf Hvac Upgrade Fossil To Electric
        api_response = api_instance.ggrf_hvac_upgrade_fossil_to_electric_ggrf_hvac_upgrade_fossil_to_electric_v1_get(location_zip_code, existing_unit_efficiency_standard, new_unit_efficiency_percent, existing_efficiency_btu_per_watt_hour, existing_consumption_gallons_per_year=existing_consumption_gallons_per_year, existing_consumption_cubic_feet_per_year=existing_consumption_cubic_feet_per_year)
        print("The response of GGRFHVACUpdateApi->ggrf_hvac_upgrade_fossil_to_electric_ggrf_hvac_upgrade_fossil_to_electric_v1_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GGRFHVACUpdateApi->ggrf_hvac_upgrade_fossil_to_electric_ggrf_hvac_upgrade_fossil_to_electric_v1_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_zip_code** | **str**|  | 
 **existing_unit_efficiency_standard** | [**HvacEfficiencyFossilFuels**](.md)|  | 
 **new_unit_efficiency_percent** | **float**|  | 
 **existing_efficiency_btu_per_watt_hour** | **float**|  | 
 **existing_consumption_gallons_per_year** | **float**|  | [optional] 
 **existing_consumption_cubic_feet_per_year** | **float**|  | [optional] 

### Return type

[**HvacUpdateResults**](HvacUpdateResults.md)

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

