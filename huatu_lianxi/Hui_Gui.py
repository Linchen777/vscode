## 加载必要的库
import numpy as np
import xarray as xr
import os, cmaps

from sklearn.feature_selection import f_regression

import matplotlib.pyplot as plt

import cartopy.crs as crs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.io.shapereader as shpreader
from cartopy.util import add_cyclic_point

##-----------------------------------------------------------------------------------------------------------------##
## 读数据
with xr.open_dataset('/mnt/e/research/data/seasonal/DJF/2.5x2.5/sst.DJF.mean.anom.nc') as f1:
    pre = f1['sst_anom'][:-1, :, :]
    lat, lon = f1['lat'], f1['lon']
pre2d = np.array(pre).reshape(pre.shape[0], pre.shape[1] * pre.shape[2])
del pre

with xr.open_dataset('/mnt/e/research/data/seasonal/DJF/2.5x2.5/pc.DJF.sst.nc') as f2:
    pc = f2['pc'][0, :]

del f1, f2

##-----------------------------------------------------------------------------------------------------------------##
## 回归系数
A = np.vstack([pc, np.ones(len(pc))]).T
pre_reg = np.linalg.lstsq(A, pre2d)[0][0].reshape(len(lat), len(lon))

## 相关系数
pre_cor = np.corrcoef(pre2d.T, pc)[:-1, -1].reshape(len(lat), len(lon))

## 显著性检验
pre_cor_sig = f_regression(np.nan_to_num(pre2d), pc)[1].reshape(len(lat), len(lon))
area = np.where(pre_cor_sig < 0.01)

del pre2d, pc, A, pre_cor_sig

##-----------------------------------------------------------------------------------------------------------------##
## 生成地图网格
pre_reg_cyc, lon_cyc = add_cyclic_point(pre_reg, coord=lon)
pre_cor_cyc = add_cyclic_point(pre_cor)
nx, ny = np.meshgrid(lon_cyc, lat)

del pre_reg, pre_cor, lat, lon, lon_cyc

##-----------------------------------------------------------------------------------------------------------------##
## 绘图
plt.figure(figsize=(12, 10))
plt.subplots_adjust(hspace=0.3)

ax1 = plt.subplot(211, projection=crs.PlateCarree(central_longitude=180))
ax1.coastlines(lw=0.6)
ax1.set_global()

c1 = ax1.contourf(nx, ny, pre_reg_cyc, np.arange(-1.5, 1.6, 0.1), cmap=cmaps.BlWhRe, transform=crs.PlateCarree())
plt.colorbar(c1, shrink=1.0, pad=0.01)

## 显著性打点
sig1 = ax1.scatter(nx[area], ny[area], marker='.', s=1, c='k', alpha=0.6, transform=crs.PlateCarree())

plt.title('Reg.', fontsize=20)

ax1.set_xticks(np.arange(0, 361, 30), crs=crs.PlateCarree())
ax1.set_yticks(np.arange(-90, 90, 15), crs=crs.PlateCarree())
ax1.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label=False))
ax1.yaxis.set_major_formatter(LatitudeFormatter())

ax1.set_extent([0, 361, -40, 85], crs=crs.PlateCarree())

##-----------------------------------------------------------------------------------------------------------------##
ax2 = plt.subplot(212, projection=crs.PlateCarree(central_longitude=180))
ax2.coastlines(lw=0.6)
ax2.set_global()

c2 = ax2.contourf(nx, ny, pre_cor_cyc, np.arange(-1.0, 1.1, 0.1), cmap=cmaps.BlWhRe, transform=crs.PlateCarree())
plt.colorbar(c2, shrink=1.0, pad=0.01)

## 显著性打点
sig2 = ax2.scatter(nx[area], ny[area], marker='.', s=1, c='k', alpha=0.6, transform=crs.PlateCarree())

plt.title('Cor.', fontsize=20)

ax2.set_xticks(np.arange(0, 361, 30), crs=crs.PlateCarree())
ax2.set_yticks(np.arange(-90, 90, 15), crs=crs.PlateCarree())
ax2.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label=False))
ax2.yaxis.set_major_formatter(LatitudeFormatter())

ax2.set_extent([0, 361, -40, 85], crs=crs.PlateCarree())

##-----------------------------------------------------------------------------------------------------------------##

plt.show()

##-----------------------------------------------------------------------------------------------------------------##
