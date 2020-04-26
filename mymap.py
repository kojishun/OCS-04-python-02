def mymap():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    import cartopy.io.shapereader as shapereader
    
    df = pd.read_csv("population_ratio_prefecture.csv", usecols=[1,2,3,4,5], index_col=0)
    df.index.name="都道府県名"

    shpfilename = shapereader.natural_earth(resolution='10m',
                                            category='cultural',
                                            name='admin_1_states_provinces')

    reader = shapereader.Reader(shpfilename)

    provinces = []
    for province in reader.records():
        if(province.attributes["admin"] == "Japan"):
            provinces.append(province)
    provinces[30].attributes["name_local"] = "静岡県" 

    plt.figure(figsize=[10,10])
    ax = plt.axes(projection=ccrs.PlateCarree())

    cmap = plt.cm.bwr
    cnorm = max(df["difference"]) - min(df["difference"])
    coff = min(df["difference"])

    for province in provinces:
        geometry = province.geometry
        color = cmap((df["difference"][province.attributes["name_local"]] - coff) / cnorm)
        ax.add_geometries(geometry, ccrs.PlateCarree(), edgecolor="black", linestyle=":",
                            facecolor=color)

    ax.set_title("Differences in the raito of the number of older people and children (2019)")
    ax.set_extent([125, 146, 25, 47])
    sm = plt.cm.ScalarMappable(cmap=cmap,norm=plt.Normalize((cnorm+coff)/100,coff/100))
    sm._A = []
    plt.colorbar(sm,ax=ax)

    plt.show()
    return

mymap()