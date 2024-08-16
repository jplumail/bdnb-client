# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.meta_donnees import FournisseurRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFournisseur:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: BdnbAPI) -> None:
        fournisseur = client.meta_donnees.fournisseur.retrieve()
        assert_matches_type(FournisseurRetrieveResponse, fournisseur, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: BdnbAPI) -> None:
        fournisseur = client.meta_donnees.fournisseur.retrieve(
            acronyme="acronyme",
            denomination_fournisseur="denomination_fournisseur",
            description="description",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(FournisseurRetrieveResponse, fournisseur, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BdnbAPI) -> None:
        response = client.meta_donnees.fournisseur.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fournisseur = response.parse()
        assert_matches_type(FournisseurRetrieveResponse, fournisseur, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BdnbAPI) -> None:
        with client.meta_donnees.fournisseur.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fournisseur = response.parse()
            assert_matches_type(FournisseurRetrieveResponse, fournisseur, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFournisseur:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBdnbAPI) -> None:
        fournisseur = await async_client.meta_donnees.fournisseur.retrieve()
        assert_matches_type(FournisseurRetrieveResponse, fournisseur, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        fournisseur = await async_client.meta_donnees.fournisseur.retrieve(
            acronyme="acronyme",
            denomination_fournisseur="denomination_fournisseur",
            description="description",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(FournisseurRetrieveResponse, fournisseur, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.meta_donnees.fournisseur.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fournisseur = await response.parse()
        assert_matches_type(FournisseurRetrieveResponse, fournisseur, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.meta_donnees.fournisseur.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fournisseur = await response.parse()
            assert_matches_type(FournisseurRetrieveResponse, fournisseur, path=["response"])

        assert cast(Any, response.is_closed) is True
