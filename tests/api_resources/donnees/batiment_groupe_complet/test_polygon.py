# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.donnees.batiment_groupe_complet import PolygonCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolygon:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: BdnbAPI) -> None:
        polygon = client.donnees.batiment_groupe_complet.polygon.create()
        assert_matches_type(PolygonCreateResponse, polygon, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: BdnbAPI) -> None:
        polygon = client.donnees.batiment_groupe_complet.polygon.create(
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
        assert_matches_type(PolygonCreateResponse, polygon, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: BdnbAPI) -> None:
        response = client.donnees.batiment_groupe_complet.polygon.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        polygon = response.parse()
        assert_matches_type(PolygonCreateResponse, polygon, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: BdnbAPI) -> None:
        with client.donnees.batiment_groupe_complet.polygon.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            polygon = response.parse()
            assert_matches_type(PolygonCreateResponse, polygon, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPolygon:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBdnbAPI) -> None:
        polygon = await async_client.donnees.batiment_groupe_complet.polygon.create()
        assert_matches_type(PolygonCreateResponse, polygon, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        polygon = await async_client.donnees.batiment_groupe_complet.polygon.create(
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
        assert_matches_type(PolygonCreateResponse, polygon, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.batiment_groupe_complet.polygon.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        polygon = await response.parse()
        assert_matches_type(PolygonCreateResponse, polygon, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.batiment_groupe_complet.polygon.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            polygon = await response.parse()
            assert_matches_type(PolygonCreateResponse, polygon, path=["response"])

        assert cast(Any, response.is_closed) is True
