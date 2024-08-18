# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.types.donnees.batiment_groupe.complet import PolygonListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolygon:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        polygon = client.donnees.batiment_groupe.complet.polygon.list()
        assert_matches_type(PolygonListResponse, polygon, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        polygon = client.donnees.batiment_groupe.complet.polygon.list(
            limit="limit",
            coordinates=[
                [
                    [6.859622167, 47.640649011],
                    [6.859270505, 47.640339457],
                    [6.858969891, 47.639296131],
                    [6.859735606, 47.639192944],
                    [6.859928452, 47.639945824],
                    [6.860217723, 47.640243915],
                    [6.859622167, 47.640649011],
                ]
            ],
            type="Polygon",
        )
        assert_matches_type(PolygonListResponse, polygon, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.complet.polygon.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        polygon = response.parse()
        assert_matches_type(PolygonListResponse, polygon, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.complet.polygon.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            polygon = response.parse()
            assert_matches_type(PolygonListResponse, polygon, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPolygon:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        polygon = await async_client.donnees.batiment_groupe.complet.polygon.list()
        assert_matches_type(PolygonListResponse, polygon, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        polygon = await async_client.donnees.batiment_groupe.complet.polygon.list(
            limit="limit",
            coordinates=[
                [
                    [6.859622167, 47.640649011],
                    [6.859270505, 47.640339457],
                    [6.858969891, 47.639296131],
                    [6.859735606, 47.639192944],
                    [6.859928452, 47.639945824],
                    [6.860217723, 47.640243915],
                    [6.859622167, 47.640649011],
                ]
            ],
            type="Polygon",
        )
        assert_matches_type(PolygonListResponse, polygon, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.complet.polygon.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        polygon = await response.parse()
        assert_matches_type(PolygonListResponse, polygon, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.complet.polygon.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            polygon = await response.parse()
            assert_matches_type(PolygonListResponse, polygon, path=["response"])

        assert cast(Any, response.is_closed) is True
