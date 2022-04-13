import csv
import requests

# test small size file
# with open('C:\Harvard\CS50AIpython\pastebin\chirps20GlobalPentadP05_e550_7f72_583d.csv') as csv_file:

with open('C:\Harvard\CS50AIpython\pastebin\chirps20GlobalPentadP05_eeb4_6722_98a3.csv') as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')    
    line_count = 0
    rain_data=list() 
    for row in csv_reader:    
        if line_count == 0:    
            print(f'Column names are {", ".join(row)}')    
            line_count += 1
        elif line_count >=10e9:
            break
        line_count += 1
        rain_data.append(row)
        
print(line_count)        
print(rain_data[:10])    

val ="San Jose"
response=requests.get("https://nominatim.openstreetmap.org/search.php?city="+val+"&format=jsonv2&namedetails=0&addressdetails=0&limit=1")
city_data=response.json()
print(city_data)
c_lat=city_data[0]['lat']
c_lon=city_data[0]['lon']

print(c_lat)
print(c_lon)
 
dist_thresh=0.05
rain_thresh=8.0
dates=list()
for row in rain_data[2:]: #remove 2 lines
    t,lat,lon,rain=row
    t=t[:10]
    # print(t,lat,lon,rain)
    lat_diff=abs(float(lat)-float(c_lat))
    lon_diff=abs(float(lon)-float(c_lon))
    
    # print(lat_diff)
    # print(lon_diff)
    if rain != "NaN": 
       if float(rain) >= rain_thresh:
           if lat_diff<dist_thresh:
              if lon_diff<dist_thresh:
                   dates.append((t,rain))
print(dates)           
dates=sorted(list(set(dates)))
for item in dates:
  print(item)
print("number of rainy 5-days: "+str(len(dates)))
