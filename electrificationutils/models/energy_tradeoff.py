# coding: utf-8

"""
    smallmodelsapi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from electrificationutils.models.energy_quantity import EnergyQuantity
from typing import Optional, Set
from typing_extensions import Self

class EnergyTradeoff(BaseModel):
    """
    The change in use of one or more types of energy.  This is a model object that gets exposed via OpenAPI.  This is typically the result of a home upgrade of some kind, such as replacing one or more appliances or adding insulation.  It also includes a usage level tag, as tradeoffs are typically different for different levels of use.
    """ # noqa: E501
    usage_level_tag: StrictStr
    time_period: Optional[StrictStr] = 'annual'
    delta: List[EnergyQuantity]
    __properties: ClassVar[List[str]] = ["usage_level_tag", "time_period", "delta"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EnergyTradeoff from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in delta (list)
        _items = []
        if self.delta:
            for _item_delta in self.delta:
                if _item_delta:
                    _items.append(_item_delta.to_dict())
            _dict['delta'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnergyTradeoff from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "usage_level_tag": obj.get("usage_level_tag"),
            "time_period": obj.get("time_period") if obj.get("time_period") is not None else 'annual',
            "delta": [EnergyQuantity.from_dict(_item) for _item in obj["delta"]] if obj.get("delta") is not None else None
        })
        return _obj


