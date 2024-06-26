# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 10:34
#
# =============================================================================
"""坐标系配置

G2 中坐标系（Coordinate） 会执行一系列点转换。在 G2 中，标记的位置通道 x 和 y 会经过比例尺的映射到 [0, 1] 的范围，这之后会使用坐标系将点转换为画布坐标，从而改变标记的空间展示形式。
"""
from .coordinate import *
from .coordinate_transform import *
