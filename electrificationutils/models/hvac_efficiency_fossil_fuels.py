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


class HvacEfficiencyFossilFuels(str, Enum):
    """
    Standards for measuring efficiency for HVAC systems burning fossil fuels.  One difference from the GGRF spreadsheet is that we break out gas and propane here so that it does not have to be picked with a separate parameter.
    """

    """
    allowed enum values
    """
    EF_MINUS__OIL = 'EF - Oil'
    EF_MINUS__GAS = 'EF - Gas'
    AFUE_MINUS__OIL_FURNACE = 'AFUE - Oil Furnace'
    AFUE_MINUS__OIL_BOILER = 'AFUE - Oil Boiler'
    AFUE_MINUS__GAS_FURNACE = 'AFUE - Gas Furnace'
    AFUE_MINUS__GAS_BOILER = 'AFUE - Gas Boiler'
    AFUE_MINUS__PROPANE_FURNACE = 'AFUE - Propane Furnace'
    AFUE_MINUS__PROPANE_BOILER = 'AFUE - Propane Boiler'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HvacEfficiencyFossilFuels from a JSON string"""
        return cls(json.loads(json_str))

