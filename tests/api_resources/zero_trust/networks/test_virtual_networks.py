# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.networks.virtual_network import VirtualNetwork
from cloudflare.types.zero_trust.networks.virtual_network_edit_response import VirtualNetworkEditResponse
from cloudflare.types.zero_trust.networks.virtual_network_create_response import VirtualNetworkCreateResponse
from cloudflare.types.zero_trust.networks.virtual_network_delete_response import VirtualNetworkDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVirtualNetworks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        virtual_network = client.zero_trust.networks.virtual_networks.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        )
        assert_matches_type(VirtualNetworkCreateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        virtual_network = client.zero_trust.networks.virtual_networks.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
            comment="Staging VPC for data science",
            is_default=True,
        )
        assert_matches_type(VirtualNetworkCreateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.virtual_networks.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = response.parse()
        assert_matches_type(VirtualNetworkCreateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.virtual_networks.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = response.parse()
            assert_matches_type(VirtualNetworkCreateResponse, virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.virtual_networks.with_raw_response.create(
                account_id="",
                name="us-east-1-vpc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        virtual_network = client.zero_trust.networks.virtual_networks.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[VirtualNetwork], virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        virtual_network = client.zero_trust.networks.virtual_networks.list(
            account_id="699d98642c564d2e855e9661899b7252",
            id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            is_default=True,
            is_deleted=True,
            name="us-east-1-vpc",
        )
        assert_matches_type(SyncSinglePage[VirtualNetwork], virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.virtual_networks.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = response.parse()
        assert_matches_type(SyncSinglePage[VirtualNetwork], virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.virtual_networks.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = response.parse()
            assert_matches_type(SyncSinglePage[VirtualNetwork], virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.virtual_networks.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        virtual_network = client.zero_trust.networks.virtual_networks.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.virtual_networks.with_raw_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = response.parse()
        assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.virtual_networks.with_streaming_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = response.parse()
            assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.virtual_networks.with_raw_response.delete(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `virtual_network_id` but received ''"):
            client.zero_trust.networks.virtual_networks.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        virtual_network = client.zero_trust.networks.virtual_networks.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(VirtualNetworkEditResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        virtual_network = client.zero_trust.networks.virtual_networks.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            comment="Staging VPC for data science",
            is_default_network=True,
            name="us-east-1-vpc",
        )
        assert_matches_type(VirtualNetworkEditResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.virtual_networks.with_raw_response.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = response.parse()
        assert_matches_type(VirtualNetworkEditResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.virtual_networks.with_streaming_response.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = response.parse()
            assert_matches_type(VirtualNetworkEditResponse, virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.virtual_networks.with_raw_response.edit(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `virtual_network_id` but received ''"):
            client.zero_trust.networks.virtual_networks.with_raw_response.edit(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncVirtualNetworks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.zero_trust.networks.virtual_networks.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        )
        assert_matches_type(VirtualNetworkCreateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.zero_trust.networks.virtual_networks.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
            comment="Staging VPC for data science",
            is_default=True,
        )
        assert_matches_type(VirtualNetworkCreateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.virtual_networks.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = await response.parse()
        assert_matches_type(VirtualNetworkCreateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.virtual_networks.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = await response.parse()
            assert_matches_type(VirtualNetworkCreateResponse, virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.virtual_networks.with_raw_response.create(
                account_id="",
                name="us-east-1-vpc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.zero_trust.networks.virtual_networks.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[VirtualNetwork], virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.zero_trust.networks.virtual_networks.list(
            account_id="699d98642c564d2e855e9661899b7252",
            id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            is_default=True,
            is_deleted=True,
            name="us-east-1-vpc",
        )
        assert_matches_type(AsyncSinglePage[VirtualNetwork], virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.virtual_networks.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = await response.parse()
        assert_matches_type(AsyncSinglePage[VirtualNetwork], virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.virtual_networks.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = await response.parse()
            assert_matches_type(AsyncSinglePage[VirtualNetwork], virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.virtual_networks.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.zero_trust.networks.virtual_networks.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.virtual_networks.with_raw_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = await response.parse()
        assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.virtual_networks.with_streaming_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = await response.parse()
            assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.virtual_networks.with_raw_response.delete(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `virtual_network_id` but received ''"):
            await async_client.zero_trust.networks.virtual_networks.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.zero_trust.networks.virtual_networks.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(VirtualNetworkEditResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.zero_trust.networks.virtual_networks.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            comment="Staging VPC for data science",
            is_default_network=True,
            name="us-east-1-vpc",
        )
        assert_matches_type(VirtualNetworkEditResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.virtual_networks.with_raw_response.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = await response.parse()
        assert_matches_type(VirtualNetworkEditResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.virtual_networks.with_streaming_response.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = await response.parse()
            assert_matches_type(VirtualNetworkEditResponse, virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.virtual_networks.with_raw_response.edit(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `virtual_network_id` but received ''"):
            await async_client.zero_trust.networks.virtual_networks.with_raw_response.edit(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )
