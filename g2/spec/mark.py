from typing import *
from dataclasses import dataclass

from .data import Data
from .transform import Transform
from .encode import Encode


@dataclass
class Mark:
    data: Data
    transform: List[Transform]
    encode: List[Encode]
    type: str


@dataclass
class Area(Mark):
    



