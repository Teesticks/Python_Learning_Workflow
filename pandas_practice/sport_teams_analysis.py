#In this assignment you must read in a file of metropolitan regions and 
# associated sports teams from wikipedia_data.html and answer some 
# questions about each metropolitan region. Each of these regions may have
#  one or more teams from the "Big 4": NFL (football, in nfl.csv), 
# MLB (baseball, in mlb.csv), NBA (basketball, in nba.csv or 
# NHL (hockey, in nhl.csv). Please keep in mind that all questions 
# are from the perspective of the metropolitan region, and that this file 
# is the "source of authority" for the location of a given sports team. 
# Thus teams which are commonly known by a different area (e.g. "Oakland 
# Raiders") need to be mapped into the metropolitan region given (e.g. San 
# Francisco Bay Area). This will require some human data understanding 
# outside of the data you've been given (e.g. you will have to hand-code 
# some names, and might need to google to find out where teams are)!

#For each sport I would like you to answer the question: what is the 
# win/loss ratio's correlation with the population of the city it is in?
#  Win/Loss ratio refers to the number of wins over the number of wins 
# plus the number of losses. Remember that to calculate the correlation 
# with pearsonr, so you are going to send in two ordered lists of values, 
# the populations from the wikipedia_data.html file and the win/loss ratio
#  for a given sport in the same order. Average the win/loss ratios for 
# those cities which have multiple teams of a single sport. Each sport is 
# worth an equal amount in this assignment (20%*4=80%) of the grade for 
# this assignment. You should only use data from year 2018 for your 
# analysis -- this is important!

#Notes
#Do not include data about the MLS or CFL in any of the work you are doing,
# we're only interested in the Big 4 in this assignment.
#I highly suggest that you first tackle the four correlation questions in 
#order, as they are all similar and worth the majority of grades for this 
# assignment. This is by design!
#It's fair game to talk with peers about high level strategy as well as 
#the relationship between metropolitan areas and sports teams. However, 
# do not post code solving aspects of the assignment (including such as 
# dictionaries mapping areas to teams, or regexes which will clen up names).
#There may be more teams than the assert statements test, remember to 
#collapse multiple teams in one city into a single value!


#NHL question 1
#For this question, calculate the win/loss ratio's correlation with the 
# population of the city it is in for the NHL using 2018 data.
city = pd.read_html('wikipedia_data.html')[1]
city = city.iloc[:-1,[0,3,5,6,7,8]]
city.head()
city_nhl = city[city['NHL']!= '—'].drop(index=[15,18,19,21,49])
city_nhl['Population (2016 est.)[8]'] = city_nhl['Population (2016 est.)[8]'].astype(float)
city_nhl.head()
nhl = pd.read_csv('nhl.csv')
nhl = nhl[nhl['year']==2018]
nhl.drop(index=[0,9,18,26],inplace=True)
nhl['W'] = nhl['W'].astype(float)
nhl['L'] = nhl['L'].astype(float)
nhl.head()
nhl['W/L%'] = nhl['W']/(nhl['W']+nhl['L'])
nhl.team.replace({'Anaheim Ducks*':'Los Angeles Ducks','Arizona Coyotes':'Phoenix Coyotes','Carolina Hurricanes':'Raleigh Hurricanes',
                  'Colorado Avalanche*':'Denver Avalanche','Florida Panthers':'Miami Panthers',
                 'Vegas Golden Knights*':'Las Vegas Golden Knights'},value=None,inplace=True)
nhl = nhl.sort_values(by='team')
nhl = nhl.reset_index().drop('index',axis=1)
nhl['W/L%'].loc[18] = nhl['W/L%'].loc[16:18].mean()
nhl['W/L%'].loc[11] = nhl['W/L%'].loc[10:11].mean()
nhl = nhl.drop(index=[16,17,10])
nhl = nhl.reset_index().drop('index',axis=1)
city_nhl = city_nhl.sort_values(by='Metropolitan area')
q1 = city_nhl.iloc[:,:2]
q1 = q1.reset_index().drop('index',axis=1)
q1 = pd.merge(q1,nhl['W/L%'],how='inner',right_index=True,left_index=True)
stats.pearsonr(q1['Population (2016 est.)[8]'],q1['W/L%'])[0]

#Question 2
#For this question, calculate the win/loss ratio's correlation with the 
# population of the city it is in for the NBA using 2018 data.
city = pd.read_html('wikipedia_data.html')[1]
city = city.iloc[:-1,[0,3,5,6,7,8]]
nba = pd.read_csv('nba.csv')
nba = nba[nba['year']==2018]
city_nba = city[city['NBA']!='—'].drop(index=[17,19,20,21,22,23,29,31,40])
city_nba = city_nba.sort_values(by='Metropolitan area')
nba['W/L%'] = nba['W/L%'].astype(float)
city_nba['Population (2016 est.)[8]'] = city_nba['Population (2016 est.)[8]'].astype(float)
nba['team'].replace({'Brooklyn Nets\xa0(12)':'New York Nets','Utah Jazz*\xa0(5)':'Salt Lake City Jazz','Golden State Warriors*\xa0(2)':'San Francisco Warriors'},value=None,inplace=True)
nba = nba.sort_values(by='team')
nba = nba.reset_index().drop('index',axis=1)
nba['W/L%'].loc[11] = nba['W/L%'].loc[10:11].mean()
nba['W/L%'].loc[18] = nba['W/L%'].loc[17:18].mean()
nba.drop(index=[10,17],inplace=True)
city_nba = city_nba.reset_index().drop('index',axis=1)
nba = nba.reset_index().drop('index',axis=1)
q2 = city_nba.iloc[:,:2]
q2 = pd.merge(q2,nba['W/L%'],how='inner',right_index=True,left_index=True)
stats.pearsonr(q2['Population (2016 est.)[8]'],q2['W/L%'])[0]

#Question 3
#For this question, calculate the win/loss ratio's correlation with the 
#population of the city it is in for the MLB using 2018 data
city = pd.read_html('wikipedia_data.html')[1]
city = city.iloc[:-1,[0,3,5,6,7,8]]
mlb = pd.read_csv('mlb.csv')
mlb = mlb[mlb['year']==2018]
city_mlb = city[city['MLB']!='—'].drop(index=[25,29,30])
city_mlb['Population (2016 est.)[8]'] = city_mlb['Population (2016 est.)[8]'].astype(float)
city_mlb = city_mlb.sort_values(by='Metropolitan area')
city_mlb = city_mlb.reset_index().drop('index',axis=1)
mlb.team.replace({'Arizona Diamondbacks':'Phoenix Diamondbacks','Colorado Rockies':'Denver Rockies',
                 'Oakland Athletics':'San Francisco Athletics','Texas Rangers':'Dallas Forth Rangers'},value=None,inplace=True)
mlb = mlb.sort_values(by='team')
mlb = mlb.reset_index().drop('index',axis=1)
mlb['W-L%'].loc[4]  = mlb['W-L%'].loc[3:4].mean()
mlb['W-L%'].loc[13]  = mlb['W-L%'].loc[12:13].mean()
mlb['W-L%'].loc[18]  = mlb['W-L%'].loc[17:18].mean()
mlb['W-L%'].loc[24]  = mlb['W-L%'].loc[23:24].mean()
mlb.drop(index=[3,12,17,23],inplace=True)
mlb = mlb.reset_index().drop('index',axis=1)
q3 = city_mlb.iloc[:,:2]
q3 = pd.merge(q3,mlb['W-L%'],how='inner',left_index=True,right_index=True)
stats.pearsonr(q3['Population (2016 est.)[8]'],q3['W-L%'])[0]

#question 4
#For this question, calculate the win/loss ratio's correlation with the 
# population of the city it is in for the **NFL** using **2018** data.
city = pd.read_html('wikipedia_data.html')[1]
city = city.iloc[:-1,[0,3,5,6,7,8]]
city_nfl = city[city['NFL']!='—'].drop(index=[13,22,27,40,41,43,46])
nfl = pd.read_csv('nfl.csv')
nfl = nfl[nfl['year']==2018].drop(index=[0,5,10,15,20,25,30,35])
nfl['W-L%'] = nfl['W-L%'].astype(float)
city_nfl['Population (2016 est.)[8]'] = city_nfl['Population (2016 est.)[8]'].astype(float)
city_nfl = city_nfl.sort_values(by='Metropolitan area')
city_nfl = city_nfl.reset_index().drop('index',axis=1)
nfl.team.replace({'Arizona Cardinals':'Phoenix Cardinals','Carolina Panthers':'Charlotte Panthers',
                  'Tennessee Titans':'Nashville Titans','New England Patriots*':'Boston Patriots',
                  'Oakland Raiders':'San Francisco Raiders'},value=None,inplace=True)
nfl = nfl.sort_values(by='team')
nfl = nfl.reset_index().drop('index',axis=1)
nfl['W-L%'].loc[17] = nfl['W-L%'].loc[16:17].mean()
nfl['W-L%'].loc[23] = nfl['W-L%'].loc[22:23].mean()
nfl['W-L%'].loc[28] = nfl['W-L%'].loc[27:28].mean()
nfl.drop(index=[16,22,27],inplace=True)
nfl = nfl.reset_index().drop('index',axis=1)
q4 = city_nfl.iloc[:,:2]
q4 = pd.merge(q4,nfl['W-L%'],how='inner',right_index=True,left_index=True)
stats.pearsonr(q4['Population (2016 est.)[8]'],q4['W-L%'])[0]



#Question 5
#In this question I would like you to explore the hypothesis that given 
# that an area has two sports teams in different sports, those teams will 
# perform the same within their respective sports. 
# How I would like to see this explored is with a series of paired t-tests 
# (so use ttest_rel) between all pairs of sports. Are there any sports 
# where we can reject the null hypothesis? Again, average values where a
#  sport has multiple teams in one region. Remember, you will only be 
# including, for each sport, cities which have teams engaged in that sport,
#  drop others as appropriate. 
mlb =pd.read_csv("mlb.csv")
nhl =pd.read_csv("nhl.csv")
nba =pd.read_csv("nba.csv")
nfl =pd.read_csv("nfl.csv")
cities=pd.read_html("wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
city_nhl = city[city['NHL']!= '—'].drop(index=[15,18,19,21,49])
city_nhl['Population (2016 est.)[8]'] = city_nhl['Population (2016 est.)[8]'].astype(float)
city_nhl.head()
nhl = nhl[nhl['year']==2018]
nhl.drop(index=[0,9,18,26],inplace=True)
nhl['W'] = nhl['W'].astype(float)
nhl['L'] = nhl['L'].astype(float)
nhl['W/L%'] = nhl['W']/(nhl['W']+nhl['L'])
nhl.team.replace({'Anaheim Ducks*':'Los Angeles Ducks','Arizona Coyotes':'Phoenix Coyotes','Carolina Hurricanes':'Raleigh Hurricanes',
                  'Colorado Avalanche*':'Denver Avalanche','Florida Panthers':'Miami Panthers',
                 'Vegas Golden Knights*':'Las Vegas Golden Knights'},value=None,inplace=True)
nhl = nhl.sort_values(by='team')
nhl = nhl.reset_index().drop('index',axis=1)
nhl['W/L%'].loc[18] = nhl['W/L%'].loc[16:18].mean()
nhl['W/L%'].loc[11] = nhl['W/L%'].loc[10:11].mean()
nhl = nhl.drop(index=[16,17,10])
nhl = nhl.reset_index().drop('index',axis=1)
city_nhl = city_nhl.sort_values(by='Metropolitan area')
q1 = city_nhl.iloc[:,:2]
q1 = q1.reset_index().drop('index',axis=1)
q1 = pd.merge(q1,nhl['W/L%'],how='inner',right_index=True,left_index=True)
nba = nba[nba['year']==2018]
city_nba = city[city['NBA']!='—'].drop(index=[17,19,20,21,22,23,29,31,40])
city_nba = city_nba.sort_values(by='Metropolitan area')
nba['W/L%'] = nba['W/L%'].astype(float)
city_nba['Population (2016 est.)[8]'] = city_nba['Population (2016 est.)[8]'].astype(float)
nba['team'].replace({'Brooklyn Nets\xa0(12)':'New York Nets','Utah Jazz*\xa0(5)':'Salt Lake City Jazz','Golden State Warriors*\xa0(2)':'San Francisco Warriors'},value=None,inplace=True)
nba = nba.sort_values(by='team')
nba = nba.reset_index().drop('index',axis=1)
nba['W/L%'].loc[11] = nba['W/L%'].loc[10:11].mean()
nba['W/L%'].loc[18] = nba['W/L%'].loc[17:18].mean()
nba.drop(index=[10,17],inplace=True)
city_nba = city_nba.reset_index().drop('index',axis=1)
nba = nba.reset_index().drop('index',axis=1)
q2 = city_nba.iloc[:,:2]
q2 = pd.merge(q2,nba['W/L%'],how='inner',right_index=True,left_index=True)
mlb = mlb[mlb['year']==2018]
city_mlb = city[city['MLB']!='—'].drop(index=[25,29,30])
city_mlb['Population (2016 est.)[8]'] = city_mlb['Population (2016 est.)[8]'].astype(float)
city_mlb = city_mlb.sort_values(by='Metropolitan area')
city_mlb = city_mlb.reset_index().drop('index',axis=1)
mlb.team.replace({'Arizona Diamondbacks':'Phoenix Diamondbacks','Colorado Rockies':'Denver Rockies',
                 'Oakland Athletics':'San Francisco Athletics','Texas Rangers':'Dallas Forth Rangers'},value=None,inplace=True)
mlb = mlb.sort_values(by='team')
mlb = mlb.reset_index().drop('index',axis=1)
mlb['W-L%'].loc[4]  = mlb['W-L%'].loc[3:4].mean()
mlb['W-L%'].loc[13]  = mlb['W-L%'].loc[12:13].mean()
mlb['W-L%'].loc[18]  = mlb['W-L%'].loc[17:18].mean()
mlb['W-L%'].loc[24]  = mlb['W-L%'].loc[23:24].mean()
mlb.drop(index=[3,12,17,23],inplace=True)
mlb = mlb.reset_index().drop('index',axis=1)
q3 = city_mlb.iloc[:,:2]
q3 = pd.merge(q3,mlb['W-L%'],how='inner',left_index=True,right_index=True)
city_nfl = city[city['NFL']!='—'].drop(index=[13,22,27,40,41,43,46])
nfl = nfl[nfl['year']==2018].drop(index=[0,5,10,15,20,25,30,35])
nfl['W-L%'] = nfl['W-L%'].astype(float)
city_nfl['Population (2016 est.)[8]'] = city_nfl['Population (2016 est.)[8]'].astype(float)
city_nfl = city_nfl.sort_values(by='Metropolitan area')
city_nfl = city_nfl.reset_index().drop('index',axis=1)
nfl.team.replace({'Arizona Cardinals':'Phoenix Cardinals','Carolina Panthers':'Charlotte Panthers',
                  'Tennessee Titans':'Nashville Titans','New England Patriots*':'Boston Patriots',
                  'Oakland Raiders':'San Francisco Raiders'},value=None,inplace=True)
nfl = nfl.sort_values(by='team')
nfl = nfl.reset_index().drop('index',axis=1)
nfl['W-L%'].loc[17] = nfl['W-L%'].loc[16:17].mean()
nfl['W-L%'].loc[23] = nfl['W-L%'].loc[22:23].mean()
nfl['W-L%'].loc[28] = nfl['W-L%'].loc[27:28].mean()
nfl.drop(index=[16,22,27],inplace=True)
nfl = nfl.reset_index().drop('index',axis=1)
q4 = city_nfl.iloc[:,:2]
q4 = pd.merge(q4,nfl['W-L%'],how='inner',right_index=True,left_index=True)

nhl_nhl = pd.merge(q1,q1,how='inner',on='Metropolitan area')
nhl_nba = pd.merge(q1,q2,how='inner',on='Metropolitan area')
nhl_mlb = pd.merge(q1,q3,how='inner',on='Metropolitan area')
nhl_nfl = pd.merge(q1,q4,how='inner',on='Metropolitan area')
nba_nba = pd.merge(q2,q2,how='inner',on='Metropolitan area')
nba_nhl = pd.merge(q2,q1,how='inner',on='Metropolitan area')
nba_mlb = pd.merge(q2,q3,how='inner',on='Metropolitan area')
nba_nfl = pd.merge(q2,q4,how='inner',on='Metropolitan area')
mlb_mlb = pd.merge(q3,q3,how='inner',on='Metropolitan area')
mlb_nhl = pd.merge(q3,q1,how='inner',on='Metropolitan area')
mlb_nba = pd.merge(q3,q2,how='inner',on='Metropolitan area')
mlb_nfl = pd.merge(q3,q4,how='inner',on='Metropolitan area')
nfl_nfl = pd.merge(q4,q4,how='inner',on='Metropolitan area')
nfl_nhl = pd.merge(q4,q1,how='inner',on='Metropolitan area')
nfl_nba = pd.merge(q4,q2,how='inner',on='Metropolitan area')
nfl_mlb = pd.merge(q4,q3,how='inner',on='Metropolitan area')

a=stats.ttest_rel(nhl_nhl['W/L%_x'],nhl_nhl['W/L%_y'])[1]
b=stats.ttest_rel(nhl_nba['W/L%_x'],nhl_nba['W/L%_y'])[1]
c=stats.ttest_rel(nhl_mlb['W/L%'],nhl_mlb['W-L%'])[1]
d=stats.ttest_rel(nhl_nfl['W/L%'],nhl_nfl['W-L%'])[1]
e=stats.ttest_rel(nba_nba['W/L%_x'],nba_nba['W/L%_y'])[1]
f=stats.ttest_rel(nba_nhl['W/L%_x'],nba_nhl['W/L%_y'])[1]
g=stats.ttest_rel(nba_mlb['W/L%'],nba_mlb['W-L%'])[1]
h=stats.ttest_rel(nba_nfl['W/L%'],nba_nfl['W-L%'])[1]
i=stats.ttest_rel(mlb_mlb['W-L%_x'],mlb_mlb['W-L%_y'])[1]
j=stats.ttest_rel(mlb_nhl['W-L%'],mlb_nhl['W/L%'])[1]
k=stats.ttest_rel(mlb_nba['W-L%'],mlb_nba['W/L%'])[1]
l=stats.ttest_rel(mlb_nfl['W-L%_x'],mlb_nfl['W-L%_y'])[1]
m=stats.ttest_rel(nfl_nfl['W-L%_x'],nfl_nfl['W-L%_y'])[1]
n=stats.ttest_rel(nfl_nhl['W-L%'],nfl_nhl['W/L%'])[1]
o=stats.ttest_rel(nfl_nba['W-L%'],nfl_nba['W/L%'])[1]
p=stats.ttest_rel(nfl_mlb['W-L%_x'],nfl_mlb['W-L%_y'])[1]

sports = ['NFL', 'NBA', 'NHL', 'MLB']
s = {'NFL':[m,o,n,p],
     'NBA':[h,e,f,g],
     'NHL':[d,b,a,c],
     'MLB':[l,k,j,i]}
p_values = pd.DataFrame(s,index=sports)
p_values
