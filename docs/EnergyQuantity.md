# EnergyQuantity

A specific amount of a particular type of energy.  This is a model object that gets exposed via OpenAPI.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy_type** | **str** |  | 
**quantity** | **float** |  | 
**units** | **str** |  | 

## Example

```python
from electrificationutils.models.energy_quantity import EnergyQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of EnergyQuantity from a JSON string
energy_quantity_instance = EnergyQuantity.from_json(json)
# print the JSON string representation of the object
print(EnergyQuantity.to_json())

# convert the object into a dict
energy_quantity_dict = energy_quantity_instance.to_dict()
# create an instance of EnergyQuantity from a dict
energy_quantity_from_dict = EnergyQuantity.from_dict(energy_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


