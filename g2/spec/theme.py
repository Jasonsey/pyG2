# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 21:07
#
# =============================================================================
"""theme

G2 中主题（Theme） 是图表中图形的一些默认样式。
"""
from typing import *
from dataclasses import dataclass

from g2.common import number


ThemeTypes = Literal[
    'classic',
    'classicDark',
    'light',
    'dark',
    'academy',
]


@dataclass
class ThemeOptions:
    """主题关键配置

    TODO: 支持更多theme参数配置
    """
    padding: Union[Literal['auto'], number, None] = None
    inset: Union[Literal['auto'], number, None] = None
    margin: Optional[number] = None
    color: Optional[str] = None
    category10: Union[str, List[str], None] = None
    category20: Union[str, List[str], None] = None
    size: Optional[number] = None
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class ClassicTheme(ThemeOptions):
    type: str = 'classic'


@dataclass
class ClassicDarkTheme(ThemeOptions):
    type: str = 'classicDark'


@dataclass
class LightTheme(ThemeOptions):
    type: str = 'light'


@dataclass
class DarkTheme(ThemeOptions):
    type: str = 'dark'


@dataclass
class AcademyTheme(ThemeOptions):
    type: str = 'academy'


Theme = Union[
    ClassicTheme,
    ClassicDarkTheme,
    LightTheme,
    DarkTheme,
    AcademyTheme,
]
