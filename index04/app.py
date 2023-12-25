import pandas as pd
import json,urllib.request
from flask import Flask, render_template, request
app = Flask(__name__)


f = open('data.json')
dataf = json.load(f)

getAll={"Pname":[],"Paddress":[],"PositionLat":[],"PositionLon":[]}

Pname = {"name":[]}
Paddress={"address":[]}
PositionLat={"positionLat":[]}
PositionLon={"positionLon":[]}
bb=[]
RName=[]
Lon=[]
Lat=[]
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        dropdownval = request.form.get('Gcity')
        bb.append(dropdownval)
        for key, value in getAll.items():
            for i in value:
                if i == dropdownval:
                    print(value.index(i))
                    Lon.append(getAll['PositionLon'][value.index(i)])
                    Lat.append(getAll['PositionLat'][value.index(i)])
                    
        return render_template('index05.html', getAll=getAll,bb=bb,RName=RName,Lon=Lon,Lat=Lat)
    i = 0
    while i < 5:
        getAll['Pname'].append(dataf['results'][i]['poi']['name'])
        getAll['Paddress'].append(dataf['results'][i]['address']['freeformAddress'])
        getAll['PositionLat'].append(dataf['results'][i]['position']['lat'])
        getAll['PositionLon'].append(dataf['results'][i]['position']['lon'])
        RName.append(dataf['results'][i]['poi']['name']) 
        i += 1

    return render_template('index05.html', getAll=getAll,bb=bb,RName=RName,Lon=Lon,Lat=Lat)   



if __name__ == '__main__':
    app.run()
