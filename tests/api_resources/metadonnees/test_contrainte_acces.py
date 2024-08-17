# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.metadonnees import ContrainteAcceRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContrainteAcces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: BdnbAPI) -> None:
        contrainte_acce = client.metadonnees.contrainte_acces.retrieve()
        assert_matches_type(ContrainteAcceRetrieveResponse, contrainte_acce, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: BdnbAPI) -> None:
        contrainte_acce = client.metadonnees.contrainte_acces.retrieve(
            contrainte_acces="contrainte_acces",
            description="description",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(ContrainteAcceRetrieveResponse, contrainte_acce, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BdnbAPI) -> None:
        response = client.metadonnees.contrainte_acces.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contrainte_acce = response.parse()
        assert_matches_type(ContrainteAcceRetrieveResponse, contrainte_acce, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BdnbAPI) -> None:
        with client.metadonnees.contrainte_acces.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contrainte_acce = response.parse()
            assert_matches_type(ContrainteAcceRetrieveResponse, contrainte_acce, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContrainteAcces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBdnbAPI) -> None:
        contrainte_acce = await async_client.metadonnees.contrainte_acces.retrieve()
        assert_matches_type(ContrainteAcceRetrieveResponse, contrainte_acce, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        contrainte_acce = await async_client.metadonnees.contrainte_acces.retrieve(
            contrainte_acces="contrainte_acces",
            description="description",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(ContrainteAcceRetrieveResponse, contrainte_acce, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.metadonnees.contrainte_acces.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contrainte_acce = await response.parse()
        assert_matches_type(ContrainteAcceRetrieveResponse, contrainte_acce, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.metadonnees.contrainte_acces.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contrainte_acce = await response.parse()
            assert_matches_type(ContrainteAcceRetrieveResponse, contrainte_acce, path=["response"])

        assert cast(Any, response.is_closed) is True
