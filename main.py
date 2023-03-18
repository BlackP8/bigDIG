from random2 import triangular as tr
import pandas as pd
import h3 

def point_gen():
    point_list = []
    for i in range(100):
        geo_lat = round(tr(51.947502, 76.850997), 6)
        geo_lon = round(tr(31.073241, 179.920635), 6)
        # point_list.append(h3.geo_to_h3(geo_lat, geo_lon, 6))
        point_list.append([geo_lat, geo_lon])
        point_list[i].append(h3.geo_to_h3(geo_lat, geo_lon, 4))
        # point_list[i].append(h3.geo_to_h3(geo_lon, geo_lat, 7)) 
        # point_list.append([h3.geo_to_h3(geo_lat, geo_lon, 6), i])
    # print(point_list)
    df = pd.DataFrame(point_list, columns=["Points_lat", "Points_lon", "hex1"])
    return df

# df = pd.DataFrame(point_gen(), columns=["Points_lat", "Points_lon", "hex1"])
# df = pd.DataFrame(point_gen(), columns=["hex", "cnt"])
# , "Points_lon", "hex"
# df.to_csv("out.csv")
# print(df.head())