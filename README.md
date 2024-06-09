# pyG2
 Python3 binding for `@AntV/G2` Plotting Library .


## Reference

1. [@AntV/G2官方文档](https://g2.antv.antgroup.com/)
2. [@AntV/G2官方代码仓库](https://github.com/antvis/g2)

## Attention

1. 暂时不支持自定义js函数，因此参数中包含lambda函数的参数都暂时无法使用, 例如各种callback
2. 参数里面如果传输component也暂时不支持，例如custom palette中的type. 主要影响各种custom组件

## TODO

1. dataclass自动转换
2. kwargs自动处理
3. xxx_ 参数名自动转 xxx
4. Tuple类型转转json时自动转List
5. extend参数自动展开