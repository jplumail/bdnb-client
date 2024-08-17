# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncDefault", "AsyncDefault"]

_T = TypeVar("_T")


class SyncDefault(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    range: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        range = self.range
        if range is None:
            return None

        if current_count < range:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncDefault(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    range: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        range = self.range
        if range is None:
            return None

        if current_count < range:
            return PageInfo(params={"offset": current_count})

        return None
