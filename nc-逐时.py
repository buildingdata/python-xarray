# -*- coding: utf-8 -*-

# 使用它们惯用的缩写导入 numpy、pandas 和 xarray
# import numpy as np
# import pandas as pd
# import netCDF4 as nc
import xarray as xr
import csv
import os

# 设定 nc 文件所在目录
# 数据来源：http://data.tpdc.ac.cn/zh-hans/data/be562de3-6367-402f-956d-59f7c21ad294/
path = "2018//"
files = os.listdir(path)

# 设定一个经纬度
loc_lat = -30
loc_lon = 110

# 保证只写入一次标头
header_added = False

# 提取 nc 文件名称中的日期信息
for file in files:
    # 这里要根据文件名修改
    file_year = file[27:31]
    file_month = file[32:34]
    file_day = file[35:37]
    file_hour = file[38:40]
    # print(file_year, file_month, file_day, file_hour)

    # 依次打开所有的 nc 文件
    ds = xr.open_dataset(path + file)
    this_ds = ds.sel(lat=loc_lat, lon=loc_lon)

    # 依次导出到 csv
    with open("out-逐时.csv", "a", newline="") as csvfile:

        # 标头要根据 nc 文件进行适当修改
        fieldnames = ["Year", "Month", "Day", "Hour", "Rs"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 保证只写入一次标头
        if not header_added:
            writer.writeheader()
            header_added = True

        # 写入每个 nc 文件的值
        writer.writerow(
            {
                "Year": file_year,
                "Month": file_month,
                "Day": file_day,
                "Hour": file_hour,
                "Rs": this_ds.global_radiation.data,
                # "temp": this_ds.temp.data,
            }
        )

    # 关闭 nc 文件
    print(file + "已经写入完成！")
    xr.Dataset.close(ds)
