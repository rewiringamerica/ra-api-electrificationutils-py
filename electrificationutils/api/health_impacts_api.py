# coding: utf-8

"""
    smallmodelsapi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated
from electrificationutils.models.group_by import GroupBy
from electrificationutils.models.metrics import Metrics
from electrificationutils.models.upgrade_option import UpgradeOption

from electrificationutils.api_client import ApiClient, RequestSerialized
from electrificationutils.api_response import ApiResponse
from electrificationutils.rest import RESTResponseType


class HealthImpactsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def query_health_impacts(
        self,
        metrics: Annotated[List[Metrics], Field(description="A list of pollutant emissions metrics or economic valuations to aggregate.")],
        upgrade: Annotated[List[UpgradeOption], Field(description="A list of upgrades to filter by.")],
        county_fips: Annotated[Optional[List[StrictStr]], Field(description="A list of three-digit county FIPS codes to filter by.")] = None,
        state: Annotated[Optional[List[StrictStr]], Field(description="A list of state abbreviations to filter by.")] = None,
        groupby: Annotated[Optional[List[GroupBy]], Field(description="A list of columns to group by.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """Query Health Impacts

        Query and aggregate results of Rewiring America's health impacts modeling data.  This endpoint allows users to filter data by county, state, and upgrade options. It aggregates data based on specified pollutant and health-related metrics and provides the option to group results by user-defined columns.  Parameters ---------- county_fips : List[str], optional     A list of county FIPS codes to filter the data by. Defaults to an empty list.     Example: ['001', '075'].  state : List[str], optional     A list of states to filter the data by. Defaults to an empty list.     Example: ['CA', 'TX'].  upgrade : List[str], required     A list of upgrade options to filter the data by. Defaults to an empty list.     Example: ['med_eff_hp_hers_sizing_no_setback', 'hp_dryer'].  metrics : List[str], required     A list of pollutant or economic valuation metrics to aggregate in the query.     This field is required.     Example: ['nh3_kg_delta', 'premature_mortality_incidence_delta'].  groupby : List[str], optional     A list of columns to group the query results by. Defaults to an empty list.     Example: ['in_sqft_bin', 'acs_housing_type'].  Returns ------- dict     A dictionary containing the aggregated health data, with results filtered and grouped     based on the provided parameters.

        :param metrics: A list of pollutant emissions metrics or economic valuations to aggregate. (required)
        :type metrics: List[Metrics]
        :param upgrade: A list of upgrades to filter by. (required)
        :type upgrade: List[UpgradeOption]
        :param county_fips: A list of three-digit county FIPS codes to filter by.
        :type county_fips: List[str]
        :param state: A list of state abbreviations to filter by.
        :type state: List[str]
        :param groupby: A list of columns to group by.
        :type groupby: List[GroupBy]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._query_health_impacts_serialize(
            metrics=metrics,
            upgrade=upgrade,
            county_fips=county_fips,
            state=state,
            groupby=groupby,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def query_health_impacts_with_http_info(
        self,
        metrics: Annotated[List[Metrics], Field(description="A list of pollutant emissions metrics or economic valuations to aggregate.")],
        upgrade: Annotated[List[UpgradeOption], Field(description="A list of upgrades to filter by.")],
        county_fips: Annotated[Optional[List[StrictStr]], Field(description="A list of three-digit county FIPS codes to filter by.")] = None,
        state: Annotated[Optional[List[StrictStr]], Field(description="A list of state abbreviations to filter by.")] = None,
        groupby: Annotated[Optional[List[GroupBy]], Field(description="A list of columns to group by.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """Query Health Impacts

        Query and aggregate results of Rewiring America's health impacts modeling data.  This endpoint allows users to filter data by county, state, and upgrade options. It aggregates data based on specified pollutant and health-related metrics and provides the option to group results by user-defined columns.  Parameters ---------- county_fips : List[str], optional     A list of county FIPS codes to filter the data by. Defaults to an empty list.     Example: ['001', '075'].  state : List[str], optional     A list of states to filter the data by. Defaults to an empty list.     Example: ['CA', 'TX'].  upgrade : List[str], required     A list of upgrade options to filter the data by. Defaults to an empty list.     Example: ['med_eff_hp_hers_sizing_no_setback', 'hp_dryer'].  metrics : List[str], required     A list of pollutant or economic valuation metrics to aggregate in the query.     This field is required.     Example: ['nh3_kg_delta', 'premature_mortality_incidence_delta'].  groupby : List[str], optional     A list of columns to group the query results by. Defaults to an empty list.     Example: ['in_sqft_bin', 'acs_housing_type'].  Returns ------- dict     A dictionary containing the aggregated health data, with results filtered and grouped     based on the provided parameters.

        :param metrics: A list of pollutant emissions metrics or economic valuations to aggregate. (required)
        :type metrics: List[Metrics]
        :param upgrade: A list of upgrades to filter by. (required)
        :type upgrade: List[UpgradeOption]
        :param county_fips: A list of three-digit county FIPS codes to filter by.
        :type county_fips: List[str]
        :param state: A list of state abbreviations to filter by.
        :type state: List[str]
        :param groupby: A list of columns to group by.
        :type groupby: List[GroupBy]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._query_health_impacts_serialize(
            metrics=metrics,
            upgrade=upgrade,
            county_fips=county_fips,
            state=state,
            groupby=groupby,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def query_health_impacts_without_preload_content(
        self,
        metrics: Annotated[List[Metrics], Field(description="A list of pollutant emissions metrics or economic valuations to aggregate.")],
        upgrade: Annotated[List[UpgradeOption], Field(description="A list of upgrades to filter by.")],
        county_fips: Annotated[Optional[List[StrictStr]], Field(description="A list of three-digit county FIPS codes to filter by.")] = None,
        state: Annotated[Optional[List[StrictStr]], Field(description="A list of state abbreviations to filter by.")] = None,
        groupby: Annotated[Optional[List[GroupBy]], Field(description="A list of columns to group by.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Query Health Impacts

        Query and aggregate results of Rewiring America's health impacts modeling data.  This endpoint allows users to filter data by county, state, and upgrade options. It aggregates data based on specified pollutant and health-related metrics and provides the option to group results by user-defined columns.  Parameters ---------- county_fips : List[str], optional     A list of county FIPS codes to filter the data by. Defaults to an empty list.     Example: ['001', '075'].  state : List[str], optional     A list of states to filter the data by. Defaults to an empty list.     Example: ['CA', 'TX'].  upgrade : List[str], required     A list of upgrade options to filter the data by. Defaults to an empty list.     Example: ['med_eff_hp_hers_sizing_no_setback', 'hp_dryer'].  metrics : List[str], required     A list of pollutant or economic valuation metrics to aggregate in the query.     This field is required.     Example: ['nh3_kg_delta', 'premature_mortality_incidence_delta'].  groupby : List[str], optional     A list of columns to group the query results by. Defaults to an empty list.     Example: ['in_sqft_bin', 'acs_housing_type'].  Returns ------- dict     A dictionary containing the aggregated health data, with results filtered and grouped     based on the provided parameters.

        :param metrics: A list of pollutant emissions metrics or economic valuations to aggregate. (required)
        :type metrics: List[Metrics]
        :param upgrade: A list of upgrades to filter by. (required)
        :type upgrade: List[UpgradeOption]
        :param county_fips: A list of three-digit county FIPS codes to filter by.
        :type county_fips: List[str]
        :param state: A list of state abbreviations to filter by.
        :type state: List[str]
        :param groupby: A list of columns to group by.
        :type groupby: List[GroupBy]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._query_health_impacts_serialize(
            metrics=metrics,
            upgrade=upgrade,
            county_fips=county_fips,
            state=state,
            groupby=groupby,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _query_health_impacts_serialize(
        self,
        metrics,
        upgrade,
        county_fips,
        state,
        groupby,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'metrics': 'multi',
            'upgrade': 'multi',
            'county_fips': 'multi',
            'state': 'multi',
            'groupby': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if metrics is not None:
            
            _query_params.append(('metrics', metrics))
            
        if upgrade is not None:
            
            _query_params.append(('upgrade', upgrade))
            
        if county_fips is not None:
            
            _query_params.append(('county_fips', county_fips))
            
        if state is not None:
            
            _query_params.append(('state', state))
            
        if groupby is not None:
            
            _query_params.append(('groupby', groupby))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/health_impacts/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


