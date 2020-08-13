import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.pyplot as plt

ds = xr.open_dataset('D:\python EXERCISE\mapmap\huatu_cartopy\MMEAN0080-03.nc', decode_times=False)

# 读取3D温度数据的经向和纬向数据
t = ds['ts'][0, 0]
temp = t

# 创建画图空间
proj = ccrs.PlateCarree()  # 创建投影
fig = plt.figure(figsize=(16, 9))  # 创建页面
ax = fig.subplots(1, 1, subplot_kw={'projection': proj})  # 子图
# 设置地图属性:加载国界、海岸线、河流、湖泊
ax.add_feature(cfeat.BORDERS.with_scale('50m'), linewidth=0.8, zorder=1)
ax.add_feature(cfeat.COASTLINE.with_scale('50m'), linewidth=0.6, zorder=1)
ax.add_feature(cfeat.RIVERS.with_scale('50m'), zorder=1)
ax.add_feature(cfeat.LAKES.with_scale('50m'), zorder=1)
# 设置网格点属性
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1.2, color='k', alpha=0.5, linestyle='--')
gl.top_labels = False  # 关闭顶端标签
gl.right_labels = False  # 关闭右侧标签
gl.xformatter = LONGITUDE_FORMATTER  # x轴设为经度格式
gl.yformatter = LATITUDE_FORMATTER  # y轴设为纬度格式
# 设置colorbar
cbar_kwargs = {
    'orientation': 'horizontal',
    'label': 'Potential',
    'shrink': 0.8,
}
# 画图
levels = np.arange(-5, 35, 2)
temp.plot.contourf(ax=ax, levels=levels, cmap='Spectral_r',
                   cbar_kwargs=cbar_kwargs, transform=ccrs.PlateCarree())
plt.show()

# plt.savefig('test.jpg')