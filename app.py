def find_top_confirmed(n = 15):
    import pandas as pd
    corona_df=pd.read_csv("dataset2.csv")
    by_country = corona_df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
    return cdf

cdf=find_top_confirmed()

pairs=[(country,confirmed) for country,confirmed in zip(cdf.index,cdf['Confirmed'])]

import folium
import pandas as pd
corona_df = pd.read_csv("dataset2.csv")
corona_df=corona_df[['Lat','Long_','Confirmed','Country_Region']]
corona_df=corona_df.dropna()
m=folium.Map(location=[52,1],
            max_bounds=True,
            tiles='cartodbpositron',
            min_zoom=2,
            zoom_start=3)

def circle_maker(x):
    folium.Circle(location=[x[0],x[1]],
                 radius=float(x[2]),
                 color="blue",
                 weight=1,
                 fill=True,
                 fill_color="blue",
                 fill_opacity=0.3,
                 tooltip='{}\n Confirmed Cases:{}'.format(x[3],x[2])).add_to(m)                 
corona_df.apply(lambda x:circle_maker(x),axis=1)
html_map=m._repr_html_()

def find_top_Active(n = 15):
    import pandas as pd
    corona_df=pd.read_csv("dataset2.csv")
    by_country = corona_df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    adf = by_country.nlargest(n, 'Active')[['Active']]
    return adf
adf=find_top_Active()

pairsActive=[(country,active) for country,active in zip(adf.index,adf['Active'])]
import folium
import pandas as pd
corona_df = pd.read_csv("dataset2.csv")
corona_df=corona_df[['Lat','Long_','Active','Country_Region']]
corona_df=corona_df.dropna()
a=folium.Map(location=[52,1],
            max_bounds=True,
            tiles='cartodbpositron',
            min_zoom=2,
            zoom_start=3)
def circle_maker(x):
    folium.Circle(location=[x[0],x[1]],
                 radius=float(x[2]),
                 color="blue",
                 weight=1,
                 fill=True,
                 fill_color="blue",
                 fill_opacity=0.3,
                 tooltip='{}\n Active Cases:{}'.format(x[3],x[2])).add_to(a)
corona_df.apply(lambda x:circle_maker(x),axis=1)
html_Activemap=a._repr_html_()


def find_top_Recovered(n = 15):
    import pandas as pd
    corona_df=pd.read_csv("dataset2.csv")
    by_country = corona_df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    rdf = by_country.nlargest(n, 'Recovered')[['Recovered']]
    return rdf
rdf=find_top_Recovered()

pairsRecovered=[(country,recovered) for country,recovered in zip(rdf.index,rdf['Recovered'])]
import folium
import pandas as pd
corona_df = pd.read_csv("dataset2.csv")
corona_df=corona_df[['Lat','Long_','Recovered','Country_Region']]
corona_df=corona_df.dropna()
r=folium.Map(location=[52,1],
            max_bounds=True,
            tiles='cartodbpositron',
            min_zoom=2,
            zoom_start=3)
def circle_maker(x):
    folium.Circle(location=[x[0],x[1]],
                 radius=float(x[2]),
                 color="blue",
                 weight=1,
                 fill=True,
                 fill_color="blue",
                 fill_opacity=0.3,
                 tooltip='{}\n Recoverd Cases:{}'.format(x[3],x[2])).add_to(r)
corona_df.apply(lambda x:circle_maker(x),axis=1)
html_Recovermap=r._repr_html_()


def find_top_Death(n = 15):
    import pandas as pd
    corona_df=pd.read_csv("dataset2.csv")
    by_country = corona_df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    ddf = by_country.nlargest(n, 'Deaths')[['Deaths']]
    return ddf

ddf=find_top_Death()

pairsDeaths=[(country,deaths) for country,deaths in zip(ddf.index,ddf['Deaths'])]
import folium
import pandas as pd
corona_df = pd.read_csv("dataset2.csv")
corona_df=corona_df[['Lat','Long_','Deaths','Country_Region']]
corona_df=corona_df.dropna()
d=folium.Map(location=[52,1],
            max_bounds=True,
            tiles='cartodbpositron',
            min_zoom=2,
            zoom_start=3)
def circle_maker(x):
    folium.Circle(location=[x[0],x[1]],
                 radius=float(x[2])*3,
                 color="blue",
                 weight=1,
                 fill=True,
                 fill_color="blue",
                 fill_opacity=0.3,
                 tooltip='{}\n Death Cases:{}'.format(x[3],x[2])).add_to(d)                 
corona_df.apply(lambda x:circle_maker(x),axis=1)
html_Deadmap=d._repr_html_()


from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html",table=cdf, cmap=html_map,amap=html_Activemap,rmap=html_Recovermap,dmap=html_Deadmap,pairs=pairs,pairsActive=pairsActive,pairsRecovered=pairsRecovered,pairsDeaths=pairsDeaths)
if __name__=="__main__":
    app.run(debug=True)