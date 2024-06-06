from typing import *
from dataclasses import dataclass

from .data_transform import DataTransform


@dataclass
class FetchConnector:
    type: str = 'fetch'
    value: Optional[str] = None
    format: Optional[Literal['json', 'csv']] = None
    # Useful when format is 'csv'.
    delimiter: Optional[str] = None
    # /** Automatically infer the data to Javascript type  */
    autoType: Optional[bool] = None
    transform: Optional[List[DataTransform]] = None


@dataclass
class InlineConnector:
    type: str = 'inline'
    value: Optional[Any] = None
    transform: Optional[List[DataTransform]] = None


Data = Union[FetchConnector, InlineConnector]
