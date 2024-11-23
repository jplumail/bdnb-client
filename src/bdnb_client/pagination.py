# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import logging
from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Response

from ._utils import is_mapping
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncDefault", "AsyncDefault"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)

_T = TypeVar("_T")

log = logging.getLogger(__name__)


class SyncDefault(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        total_count: Optional[int] = None
        try:
            total_count = int(response.headers["content-range"].split("/")[-1])
        except ValueError:
            log.debug(f"Couldn't find total count in {response.headers['content-range']}")
            total_count = None
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                **{"total_count": total_count},
            },
        )


class AsyncDefault(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        total_count: Optional[int] = None
        try:
            total_count = int(response.headers["content-range"].split("/")[-1])
        except ValueError:
            log.debug(f"Couldn't find total count in {response.headers['content-range']}")
            total_count = None
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                **{"total_count": total_count},
            },
        )
