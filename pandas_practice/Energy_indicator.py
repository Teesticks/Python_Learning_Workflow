#Make sure to exclude the footer and header information from the datafile. 
#The first two columns are unneccessary, so you should get rid of them, 
#and you should change the column labels so that the columns are:

#['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]

#Convert Energy Supply to gigajoules (Note: there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.

#Rename the following list of countries (for use in later questions):

#"Republic of Korea": "South Korea",
#"United States of America": "United States",
#"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
#"China, Hong Kong Special Administrative Region": "Hong Kong"

#There are also several countries with numbers and/or parenthesis in their
#name. Be sure to remove these, e.g. 'Bolivia (Plurinational State of)' 
#should be 'Bolivia'. 'Switzerland17' should be 'Switzerland'.

#Next, load the GDP data from the file assets/world_bank.csv, which is a 
#csv containing countries' GDP from 1960 to 2015 from World Bank. 
#Call this DataFrame GDP.

#Make sure to skip the header, and rename the following list of countries:

#"Korea, Rep.": "South Korea", 
#"Iran, Islamic Rep.": "Iran",
#"Hong Kong SAR, China": "Hong Kong"

#Finally, load the Sciamgo Journal and Country Rank data for Energy 
#Engineering and Power Technology from the file assets/scimagojr-3.xlsx, 
#which ranks countries based on their journal contributions in the 
#aforementioned area. Call this DataFrame ScimEn.


#Question1
#Join the three datasets: GDP, Energy, and ScimEn into a new dataset 
#(using the intersection of country names). Use only the last 10 years 
#(2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank'
#(Rank 1 through 15).

#The index of this DataFrame should be the name of the country, and the 
#columns should be ['Rank', 'Documents', 'Citable documents', 'Citations',
#'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 
#'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009',
#'2010', '2011', '2012', '2013', '2014', '2015'].

import numpy as np
import pandas as pd
Energy = pd.read_excel('Energy Indicators.xls')
Energy.head()

Energy.drop(['Unnamed: 0','Unnamed: 1'],axis=1,inplace=True)

Energy.rename({'Unnamed: 2':'Country','Unnamed: 3':'Energy Supply','Unnamed: 4':'Energy Supply per Capita',
               'Unnamed: 5':'% Renewable'},axis=1,inplace=True)

Energy['Energy Supply'] = Energy['Energy Supply']*1000000

Energy.dropna(axis=0,inplace=True)

Energy[Energy['Energy Supply per Capita']=='...']=np.nan

Energy.dropna(axis=0,inplace=True)

Energy.drop(index=8,inplace=True)

split =Energy['Country'].str.split('(\d+)',expand=True)
split = split.loc[:,[0]]
Energy['Country'] = split

parent = Energy['Country'].str.split('([()])',expand=True)
parent = parent.loc[:,[0]]
Energy['Country'] = parent

Energy['Country'] = Energy['Country'].replace({"Republic of Korea": "South Korea",
                                "United States of America": "United States",
                                "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                "China, Hong Kong Special Administrative Region": "Hong Kong"},value=None)
Energy['Country'] = Energy['Country'].str.strip()
Energy['Country'].unique()

GDPP = pd.read_csv('world_bank.csv',index_col=False)
GDPP.head()

GDPP = GDPP.drop(GDPP.columns[1:50],axis=1)

GDPP = GDPP.rename({'Data Source':'Country','Unnamed: 50':'2006','Unnamed: 51':'2007','Unnamed: 52':'2008','Unnamed: 53':'2009','Unnamed: 54':'2010','Unnamed: 55':'2011',
                  'Unnamed: 56':'2012','Unnamed: 57':'2013','Unnamed: 58':'2014','Unnamed: 59':'2015'},axis=1)

GDPP['Country'] = GDPP['Country'].replace({"Korea, Rep.": "South Korea", 
            "Iran, Islamic Rep.": "Iran",
            "Hong Kong SAR, China": "Hong Kong"},value=None)

ScimEn = pd.read_excel('scimagojr-3.xlsx')
ScimEn = ScimEn.head(15)
ScimEn

data = pd.merge(ScimEn,Energy,how='inner',on='Country')
data = pd.merge(data,GDPP,how='inner',on='Country')
data = data.set_index('Country')
data.head()

#Question 2
#The previous question joined three datasets then reduced this to just the
#top 15 entries. When you joined the datasets, but before you reduced this 
# to the top 15 items, how many entries did you lose?
import numpy as np
import pandas as pd
Energy = pd.read_excel('Energy Indicators.xls')
Energy.head()

Energy.drop(['Unnamed: 0','Unnamed: 1'],axis=1,inplace=True)

Energy.rename({'Unnamed: 2':'Country','Unnamed: 3':'Energy Supply','Unnamed: 4':'Energy Supply per Capita',
               'Unnamed: 5':'% Renewable'},axis=1,inplace=True)

Energy['Energy Supply'] = Energy['Energy Supply']*1000000
Energy.dropna(axis=0,inplace=True)
Energy.drop(index=8,inplace=True)
Energy.drop_duplicates(subset=None, keep='last', inplace=False)
split =Energy['Country'].str.split('(\d+)',expand=True)
split = split.loc[:,[0]]
Energy['Country'] = split

parent = Energy['Country'].str.split('([()])',expand=True)
parent = parent.loc[:,[0]]
Energy['Country'] = parent

Energy['Country'] = Energy['Country'].replace({"Republic of Korea": "South Korea",
                                "United States of America": "United States",
                                "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                "China, Hong Kong Special Administrative Region": "Hong Kong"},value=None)
Energy['Country'] = Energy['Country'].str.strip()
Energy['Country'].unique()

GDPP = pd.read_csv('world_bank.csv',index_col=False)
GDPP.head()
GDPP = GDPP.drop(GDPP.index[0:4])
GDPP = GDPP.drop(GDPP.columns[1:50],axis=1)

GDPP = GDPP.rename({'Data Source':'Country','Unnamed: 50':'2006','Unnamed: 51':'2007','Unnamed: 52':'2008','Unnamed: 53':'2009','Unnamed: 54':'2010','Unnamed: 55':'2011',
                  'Unnamed: 56':'2012','Unnamed: 57':'2013','Unnamed: 58':'2014','Unnamed: 59':'2015'},axis=1)

GDPP['Country'] = GDPP['Country'].replace({"Korea, Rep.": "South Korea", 
            "Iran, Islamic Rep.": "Iran",
            "Hong Kong SAR, China": "Hong Kong"},value=None)

ScimEn = pd.read_excel('scimagojr-3.xlsx')
ScimEn
data1 = pd.merge(Energy,GDPP,how='inner',on='Country')
data1 = pd.merge(data1,ScimEn,how='inner',on='Country')
data1 = data1.set_index('Country')
data2 = pd.merge(Energy,GDPP,how='outer',on='Country')
data2 = pd.merge(data2,ScimEn,how='outer',on='Country')
data2 = data2.set_index('Country')
(len(data2.index) - len(data1.index))

#Question3 
#What are the top 15 countries for average GDP over the last 10 years?

year = ['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
avgGDP = data[year].mean(axis=1)
avgGDP.sort_values(ascending=False)

#Question 4
#By how much had the GDP changed over the 10 year span for the country with
#the 6th largest average GDP?
avgGDP = avgGDP.sort_values(ascending=False)
avgGDP[5:6]

gdp_inc = (data['2015']['United Kingdom']) - (data['2006']['United Kingdom'])
gdp_inc

#Question 5
#What is the mean energy supply per capita?

espc = data['Energy Supply per Capita'].mean()
espc

#Question 6
#What country has the maximum % Renewable and what is the percentage?
data['% Renewable'] = data['% Renewable'].astype(float,errors='raise')
data['% Renewable'].idxmax()
data['% Renewable']['Brazil']
tupl = ((data['% Renewable'].idxmax()),(data['% Renewable']['Brazil']))
tupl

#Question 7
#Create a new column that is the ratio of Self-Citations to Total Citations.
#What is the maximum value for this new column, and what country has the 
#highest ratio?
data['ratio'] = data['Self-citations']/data['Citations']
tup = ((data['ratio'].idxmax()),(data['ratio']['China']))
tup

#Question 8
#Create a column that estimates the population using Energy Supply and 
#Energy Supply per capita. What is the third most populous country 
#according to this estimate?
data['Pop']=data['Energy Supply']/data['Energy Supply per Capita']
data['Pop'] = data['Pop'].astype(float)
data['Pop'].idxmax()

#Question 9
#Create a column that estimates the number of citable documents per person.
#What is the correlation between the number of citable documents per 
#capita and the energy supply per capita? Use the .corr() method, 
#(Pearson's correlation).
data['cpc'] = data['Citable documents']/data['Pop']
data['cpc']
data['Energy Supply per Capita']=data['Energy Supply per Capita'].astype(float,errors='raise')
data['Energy Supply per Capita'].corr(data['cpc'])

#Question 10
#Create a new column with a 1 if the country's % Renewable value is at or 
#above the median for all countries in the top 15, and a 0 if the country's
#% Renewable value is below the median.
data['% Renewable']=data['% Renewable'].astype(float,errors='raise')
data['% Renewable']

def renew(i):
    if i >= (data['% Renewable'].median()):
        return 1
    elif i < (data['% Renewable'].median()):
        return 0
    
data['ratio_1'] = data['% Renewable'].apply(renew)
data['ratio_1']

#Question 11
#Use the following dictionary to group the Countries by Continent, then 
#create a DataFrame that displays the sample size (the number of countries
#in each continent bin), and the sum, mean, and std deviation for the 
#estimated population of each country.

ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}


data['Continent'] = pd.Series(ContinentDict)
data['Continent']
w = data.groupby('Continent').agg({'Pop':(np.size,np.sum,np.mean,np.std)})
w.columns = ['size','sum','mean','std']
w

#Question 12
#Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as 
#these new % Renewable bins. How many countries are in each of these 
#groups?
data6 = data.copy()
data6 = data6.rename({'% Renewable':'Renewable'},axis=1)
data6['% Renewable'] = pd.cut(data6['Renewable'],5)
a = data6.groupby(['Continent','% Renewable']).size()
group = a[a!=0]
group

#Question 13
#Convert the Population Estimate series to a string with thousands 
#separator (using commas). Use all significant digits (do not round the 
#results).
#e.g. 12345678.90 -> 12,345,678.90
data['Pop'] =data['Energy Supply']/data['Energy Supply per Capita']
data['Pop'].apply(lambda x: '{:,}'.format(x))
