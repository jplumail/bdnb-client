# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types import AutocompletionEntitesTexteListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutocompletionEntitesTextes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        autocompletion_entites_texte = client.autocompletion_entites_textes.list()
        assert_matches_type(AutocompletionEntitesTexteListResponse, autocompletion_entites_texte, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        autocompletion_entites_texte = client.autocompletion_entites_textes.list(
            code="code",
            geom="geom",
            limit="limit",
            nom="nom",
            nom_unaccent="nom_unaccent",
            offset="offset",
            order="order",
            origine_code="origine_code",
            origine_nom="origine_nom",
            select="select",
            type_entite="type_entite",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AutocompletionEntitesTexteListResponse, autocompletion_entites_texte, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.autocompletion_entites_textes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocompletion_entites_texte = response.parse()
        assert_matches_type(AutocompletionEntitesTexteListResponse, autocompletion_entites_texte, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.autocompletion_entites_textes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocompletion_entites_texte = response.parse()
            assert_matches_type(AutocompletionEntitesTexteListResponse, autocompletion_entites_texte, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutocompletionEntitesTextes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        autocompletion_entites_texte = await async_client.autocompletion_entites_textes.list()
        assert_matches_type(AutocompletionEntitesTexteListResponse, autocompletion_entites_texte, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        autocompletion_entites_texte = await async_client.autocompletion_entites_textes.list(
            code="code",
            geom="geom",
            limit="limit",
            nom="nom",
            nom_unaccent="nom_unaccent",
            offset="offset",
            order="order",
            origine_code="origine_code",
            origine_nom="origine_nom",
            select="select",
            type_entite="type_entite",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AutocompletionEntitesTexteListResponse, autocompletion_entites_texte, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.autocompletion_entites_textes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocompletion_entites_texte = await response.parse()
        assert_matches_type(AutocompletionEntitesTexteListResponse, autocompletion_entites_texte, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.autocompletion_entites_textes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocompletion_entites_texte = await response.parse()
            assert_matches_type(AutocompletionEntitesTexteListResponse, autocompletion_entites_texte, path=["response"])

        assert cast(Any, response.is_closed) is True
