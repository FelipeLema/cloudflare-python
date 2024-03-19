# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.devices.policies import DefaultPolicyGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefaultPolicy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        default_policy = client.zero_trust.devices.policies.default_policy.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DefaultPolicyGetResponse], default_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.default_policy.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        default_policy = response.parse()
        assert_matches_type(Optional[DefaultPolicyGetResponse], default_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.default_policy.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            default_policy = response.parse()
            assert_matches_type(Optional[DefaultPolicyGetResponse], default_policy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDefaultPolicy:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        default_policy = await async_client.zero_trust.devices.policies.default_policy.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DefaultPolicyGetResponse], default_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.default_policy.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        default_policy = await response.parse()
        assert_matches_type(Optional[DefaultPolicyGetResponse], default_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.default_policy.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            default_policy = await response.parse()
            assert_matches_type(Optional[DefaultPolicyGetResponse], default_policy, path=["response"])

        assert cast(Any, response.is_closed) is True
