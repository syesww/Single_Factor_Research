# Single_Factor_Research
## 1. 简介
这是我自己的一个单因子研究框架，从数据处理、因子计算...到回测绩效评估，整个框架比较简单，适合拿来做一些简单的验证

## 2. 项目框架
![示例图片](./structure.jpg)

如图，整个框架可以分成五个部分
- 数据收集
- 因子定义与计算
- 因子有效性检验
- 绩效评估

数据以HDF5保存在本地，同时提供了一个新版本的alphalens(解决原版不支持新pandas的问题）  
回测框架用的是backtrader

## 3. 研究方法
- 使用data获取数据
- 使用factor_def_and _calc定义因子与计算
- 使用factor_validation完成因子有效性检验
- 使用performance_analyse运行分层回测框架
