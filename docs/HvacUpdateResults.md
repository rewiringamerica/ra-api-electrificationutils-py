# HvacUpdateResults

The results of a GGRF HVAC upgrade calculation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_emissions_tons_co2e** | **float** |  | 
**new_unit_emissions_metric_tons_co2e** | **float** |  | 
**emissions_reduced_metric_tons_co2e** | **float** |  | 

## Example

```python
from electrificationutils.models.hvac_update_results import HvacUpdateResults

# TODO update the JSON string below
json = "{}"
# create an instance of HvacUpdateResults from a JSON string
hvac_update_results_instance = HvacUpdateResults.from_json(json)
# print the JSON string representation of the object
print(HvacUpdateResults.to_json())

# convert the object into a dict
hvac_update_results_dict = hvac_update_results_instance.to_dict()
# create an instance of HvacUpdateResults from a dict
hvac_update_results_from_dict = HvacUpdateResults.from_dict(hvac_update_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


