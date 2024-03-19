# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.devices.posture import (
    IntegrationListResponse,
    IntegrationDeleteResponse,
    TeamsDevicesDevicePostureIntegrations,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        integration = client.zero_trust.devices.posture.integrations.create(
            account_id="699d98642c564d2e855e9661899b7252",
            config={
                "api_url": "https://as123.awmdm.com/API",
                "auth_url": "https://na.uemauth.vmwservices.com/connect/token",
                "client_id": "example client id",
                "client_secret": "example client secret",
            },
            interval="10m",
            name="My Workspace One Integration",
            type="workspace_one",
        )
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        integration = client.zero_trust.devices.posture.integrations.create(
            account_id="699d98642c564d2e855e9661899b7252",
            config={
                "api_url": "https://as123.awmdm.com/API",
                "auth_url": "https://na.uemauth.vmwservices.com/connect/token",
                "client_id": "example client id",
                "client_secret": "example client secret",
            },
            interval="10m",
            name="My Workspace One Integration",
            type="workspace_one",
        )
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.posture.integrations.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            config={
                "api_url": "https://as123.awmdm.com/API",
                "auth_url": "https://na.uemauth.vmwservices.com/connect/token",
                "client_id": "example client id",
                "client_secret": "example client secret",
            },
            interval="10m",
            name="My Workspace One Integration",
            type="workspace_one",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.posture.integrations.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            config={
                "api_url": "https://as123.awmdm.com/API",
                "auth_url": "https://na.uemauth.vmwservices.com/connect/token",
                "client_id": "example client id",
                "client_secret": "example client secret",
            },
            interval="10m",
            name="My Workspace One Integration",
            type="workspace_one",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        integration = client.zero_trust.devices.posture.integrations.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.posture.integrations.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.posture.integrations.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Optional[IntegrationListResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        integration = client.zero_trust.devices.posture.integrations.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[IntegrationDeleteResponse], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.posture.integrations.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[IntegrationDeleteResponse], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.posture.integrations.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Optional[IntegrationDeleteResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.zero_trust.devices.posture.integrations.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        integration = client.zero_trust.devices.posture.integrations.edit(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        integration = client.zero_trust.devices.posture.integrations.edit(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            config={
                "api_url": "https://as123.awmdm.com/API",
                "auth_url": "https://na.uemauth.vmwservices.com/connect/token",
                "client_id": "example client id",
                "client_secret": "example client secret",
            },
            interval="10m",
            name="My Workspace One Integration",
            type="workspace_one",
        )
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.posture.integrations.with_raw_response.edit(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.posture.integrations.with_streaming_response.edit(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.zero_trust.devices.posture.integrations.with_raw_response.edit(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        integration = client.zero_trust.devices.posture.integrations.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.posture.integrations.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.posture.integrations.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.zero_trust.devices.posture.integrations.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncIntegrations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.devices.posture.integrations.create(
            account_id="699d98642c564d2e855e9661899b7252",
            config={
                "api_url": "https://as123.awmdm.com/API",
                "auth_url": "https://na.uemauth.vmwservices.com/connect/token",
                "client_id": "example client id",
                "client_secret": "example client secret",
            },
            interval="10m",
            name="My Workspace One Integration",
            type="workspace_one",
        )
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.devices.posture.integrations.create(
            account_id="699d98642c564d2e855e9661899b7252",
            config={
                "api_url": "https://as123.awmdm.com/API",
                "auth_url": "https://na.uemauth.vmwservices.com/connect/token",
                "client_id": "example client id",
                "client_secret": "example client secret",
            },
            interval="10m",
            name="My Workspace One Integration",
            type="workspace_one",
        )
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.posture.integrations.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            config={
                "api_url": "https://as123.awmdm.com/API",
                "auth_url": "https://na.uemauth.vmwservices.com/connect/token",
                "client_id": "example client id",
                "client_secret": "example client secret",
            },
            interval="10m",
            name="My Workspace One Integration",
            type="workspace_one",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.posture.integrations.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            config={
                "api_url": "https://as123.awmdm.com/API",
                "auth_url": "https://na.uemauth.vmwservices.com/connect/token",
                "client_id": "example client id",
                "client_secret": "example client secret",
            },
            interval="10m",
            name="My Workspace One Integration",
            type="workspace_one",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.devices.posture.integrations.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.posture.integrations.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.posture.integrations.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Optional[IntegrationListResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.devices.posture.integrations.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[IntegrationDeleteResponse], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.posture.integrations.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[IntegrationDeleteResponse], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.posture.integrations.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Optional[IntegrationDeleteResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.zero_trust.devices.posture.integrations.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.devices.posture.integrations.edit(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.devices.posture.integrations.edit(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            config={
                "api_url": "https://as123.awmdm.com/API",
                "auth_url": "https://na.uemauth.vmwservices.com/connect/token",
                "client_id": "example client id",
                "client_secret": "example client secret",
            },
            interval="10m",
            name="My Workspace One Integration",
            type="workspace_one",
        )
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.posture.integrations.with_raw_response.edit(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.posture.integrations.with_streaming_response.edit(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.zero_trust.devices.posture.integrations.with_raw_response.edit(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.devices.posture.integrations.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.posture.integrations.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.posture.integrations.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Optional[TeamsDevicesDevicePostureIntegrations], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.zero_trust.devices.posture.integrations.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )
