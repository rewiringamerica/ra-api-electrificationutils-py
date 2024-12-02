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


class Metrics(str, Enum):
    """
    Enum for valid pollutant or health-related metrics.
    """

    """
    allowed enum values
    """
    PM25_MINUS_PRI_KG_DELTA = 'pm25-pri_kg_delta'
    NH3_KG_DELTA = 'nh3_kg_delta'
    NOX_KG_DELTA = 'nox_kg_delta'
    VOC_KG_DELTA = 'voc_kg_delta'
    SO2_KG_DELTA = 'so2_kg_delta'
    PREMATURE_MORTALITY_INCIDENCE_DELTA = 'premature_mortality_incidence_delta'
    PREMATURE_MORTALITY_VALUATION_DOLLARS_DELTA = 'premature_mortality_valuation_dollars_delta'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Metrics from a JSON string"""
        return cls(json.loads(json_str))

