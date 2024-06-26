from typing import *
from dataclasses import dataclass

from .data_transform import DataTransform

__all__ = [
    'FetchConnector',
    'InlineConnector',
    'Data',
]


@dataclass
class FetchConnector:
    type: str = 'fetch'
    value: Optional[str] = None
    format: Optional[Literal['json', 'csv']] = None
    delimiter: Optional[str] = None
    """Useful when format is 'csv'."""
    autoType: Optional[bool] = None
    """Automatically infer the data to Javascript type"""
    transform: Optional[List[DataTransform]] = None


@dataclass
class InlineConnector:
    type: str = 'inline'
    value: Optional[Any] = None
    transform: Optional[List[DataTransform]] = None


Data = Union[FetchConnector, InlineConnector]
