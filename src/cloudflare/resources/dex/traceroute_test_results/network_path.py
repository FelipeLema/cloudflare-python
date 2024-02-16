# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.dex.traceroute_test_results import NetworkPathListResponse

from typing import Type

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["NetworkPath", "AsyncNetworkPath"]


class NetworkPath(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworkPathWithRawResponse:
        return NetworkPathWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkPathWithStreamingResponse:
        return NetworkPathWithStreamingResponse(self)

    def list(
        self,
        test_result_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkPathListResponse:
        """
        Get a breakdown of hops and performance metrics for a specific traceroute test
        run

        Args:
          test_result_id: API Resource UUID tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not test_result_id:
            raise ValueError(f"Expected a non-empty value for `test_result_id` but received {test_result_id!r}")
        return self._get(
            f"/accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[NetworkPathListResponse], ResultWrapper[NetworkPathListResponse]),
        )


class AsyncNetworkPath(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworkPathWithRawResponse:
        return AsyncNetworkPathWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkPathWithStreamingResponse:
        return AsyncNetworkPathWithStreamingResponse(self)

    async def list(
        self,
        test_result_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkPathListResponse:
        """
        Get a breakdown of hops and performance metrics for a specific traceroute test
        run

        Args:
          test_result_id: API Resource UUID tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not test_result_id:
            raise ValueError(f"Expected a non-empty value for `test_result_id` but received {test_result_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[NetworkPathListResponse], ResultWrapper[NetworkPathListResponse]),
        )


class NetworkPathWithRawResponse:
    def __init__(self, network_path: NetworkPath) -> None:
        self._network_path = network_path

        self.list = to_raw_response_wrapper(
            network_path.list,
        )


class AsyncNetworkPathWithRawResponse:
    def __init__(self, network_path: AsyncNetworkPath) -> None:
        self._network_path = network_path

        self.list = async_to_raw_response_wrapper(
            network_path.list,
        )


class NetworkPathWithStreamingResponse:
    def __init__(self, network_path: NetworkPath) -> None:
        self._network_path = network_path

        self.list = to_streamed_response_wrapper(
            network_path.list,
        )


class AsyncNetworkPathWithStreamingResponse:
    def __init__(self, network_path: AsyncNetworkPath) -> None:
        self._network_path = network_path

        self.list = async_to_streamed_response_wrapper(
            network_path.list,
        )
