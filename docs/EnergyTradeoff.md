# EnergyTradeoff

The change in use of one or more types of energy.  This is a model object that gets exposed via OpenAPI.  This is typically the result of a home upgrade of some kind, such as replacing one or more appliances or adding insulation.  It also includes a usage level tag, as tradeoffs are typically different for different levels of use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_level_tag** | **str** |  | 
**time_period** | **str** |  | [optional] [default to 'annual']
**changes** | [**List[EnergyQuantity]**](EnergyQuantity.md) |  | 

## Example

```python
from electrificationutils.models.energy_tradeoff import EnergyTradeoff

# TODO update the JSON string below
json = "{}"
# create an instance of EnergyTradeoff from a JSON string
energy_tradeoff_instance = EnergyTradeoff.from_json(json)
# print the JSON string representation of the object
print(EnergyTradeoff.to_json())

# convert the object into a dict
energy_tradeoff_dict = energy_tradeoff_instance.to_dict()
# create an instance of EnergyTradeoff from a dict
energy_tradeoff_from_dict = EnergyTradeoff.from_dict(energy_tradeoff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


