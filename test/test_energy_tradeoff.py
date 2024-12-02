# coding: utf-8

"""
    smallmodelsapi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from electrificationutils.models.energy_tradeoff import EnergyTradeoff

class TestEnergyTradeoff(unittest.TestCase):
    """EnergyTradeoff unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnergyTradeoff:
        """Test EnergyTradeoff
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnergyTradeoff`
        """
        model = EnergyTradeoff()
        if include_optional:
            return EnergyTradeoff(
                usage_level_tag = '',
                time_period = 'annual',
                changes = [
                    electrificationutils.models.energy_quantity.EnergyQuantity(
                        energy_type = '', 
                        quantity = 1.337, 
                        units = '', )
                    ]
            )
        else:
            return EnergyTradeoff(
                usage_level_tag = '',
                changes = [
                    electrificationutils.models.energy_quantity.EnergyQuantity(
                        energy_type = '', 
                        quantity = 1.337, 
                        units = '', )
                    ],
        )
        """

    def testEnergyTradeoff(self):
        """Test EnergyTradeoff"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()