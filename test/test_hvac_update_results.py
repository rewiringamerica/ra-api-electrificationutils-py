# coding: utf-8

"""
    smallmodelsapi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from electrificationutils.models.hvac_update_results import HvacUpdateResults

class TestHvacUpdateResults(unittest.TestCase):
    """HvacUpdateResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HvacUpdateResults:
        """Test HvacUpdateResults
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HvacUpdateResults`
        """
        model = HvacUpdateResults()
        if include_optional:
            return HvacUpdateResults(
                existing_emissions_tons_co2e = 1.337,
                new_unit_emissions_metric_tons_co2e = 1.337,
                emissions_reduced_metric_tons_co2e = 1.337
            )
        else:
            return HvacUpdateResults(
                existing_emissions_tons_co2e = 1.337,
                new_unit_emissions_metric_tons_co2e = 1.337,
                emissions_reduced_metric_tons_co2e = 1.337,
        )
        """

    def testHvacUpdateResults(self):
        """Test HvacUpdateResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()