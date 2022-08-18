# 使用 xarray 处理 netCDF 栅格数据
### 1. xarray 库

#### 1.1 简介

xarray 库应该是目前用于处理 netCDF 数据最为方便的库了。

xarry 有两个核心数据结构：**DataArray** 和 **Dataset**。xarray 可以看作是对 numpy 和 pandas 的扩展，同时也借鉴了许多 pandas 的优点，具有良好的易用性。xarray 与 netCDF4 在使用上存在许多相似之处，但是从输出的结果我们可以发现，同样是 Dataset，但是 xarray 的结果显然有更好的可读性。

#### 1.2 官方文档

更多内容建议阅读 [xarray 官方文档](https://docs.xarray.dev/en/stable/index.html)。

#### 1.3 支持格式

| 格式 |         说明         |         兼容性         |
| :--: | :------------------: | :--------------------: |
|  nc  | netCDF 数据文件格式  |          支持          |
| nc4  | netCDF4 数据文件格式 |          支持          |
| hdf  |     卫星数据格式     | 官方说支持，但暂未跑通 |

### 2. 安装

[xarray](https://docs.xarray.dev/en/stable/getting-started-guide/installing.html) 库需要以下主要依赖：

- Python (3.8 or later)
- [numpy](https://www.numpy.org/) (1.18 or later)
- [packaging](https://packaging.pypa.io/en/latest/#) (20.0 or later)
- [pandas](https://pandas.pydata.org/) (1.1 or later)
- netCDF4

推荐安装的的依赖如下：

```shell
pip install numpy
pip install pandas
pip install packaging
pip install netcdf4
pip install xarray
pip install dask
```

### 3. 使用

#### 3.1 数据示例

本例采用 “[全球高分辨率（3小时，10公里）地表太阳辐射数据集（1983-2018）](http://data.tpdc.ac.cn/zh-hans/data/be562de3-6367-402f-956d-59f7c21ad294/)” 的部分数据作为演示，大家可以自行下载部分数据进行测试。

本例仅仅包含 2018 年 1 月 1 日的逐 3 小时数据，在 `2018/` 目录下即可看见：

```
├── 2018/
    ├── ISCCP_HXG_global_radiation_2018_01_01_00.nc
    ├── ISCCP_HXG_global_radiation_2018_01_01_03.nc
    ├── ISCCP_HXG_global_radiation_2018_01_01_06.nc
    ├── ISCCP_HXG_global_radiation_2018_01_01_09.nc
    ├── ISCCP_HXG_global_radiation_2018_01_01_12.nc
    ├── ISCCP_HXG_global_radiation_2018_01_01_15.nc
    ├── ISCCP_HXG_global_radiation_2018_01_01_18.nc
    ├── ISCCP_HXG_global_radiation_2018_01_01_21.nc
```

#### 3.2 运行代码

运行 `nc-逐时.py` 后，即可在当前目录输出 `out-逐时.csv` 文件。

#### 3.3 特别注意

```
💡 使用 xarray 库时，不支持中文路径，请确保路径为全英文。如果想要支持中文路径，请使用纯 netCDF4 库。
```
