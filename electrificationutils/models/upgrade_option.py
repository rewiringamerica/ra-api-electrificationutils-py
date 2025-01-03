# coding: utf-8

"""
    smallmodelsapi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UpgradeOption(str, Enum):
    """
    Enum for valid electrification upgrade options.
    """

    """
    allowed enum values
    """
    HP_DRYER = 'hp_dryer'
    MED_EFF_HP_HERS_SIZING_NO_SETBACK_BASIC_ENCLOSURE = 'med_eff_hp_hers_sizing_no_setback_basic_enclosure'
    HP_WATER_HEATER = 'hp_water_heater'
    MED_EFF_HP_HERS_SIZING_NO_SETBACK = 'med_eff_hp_hers_sizing_no_setback'
    ELECTRIC_RESISTANCE_DRYER = 'electric_resistance_dryer'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UpgradeOption from a JSON string"""
        return cls(json.loads(json_str))


