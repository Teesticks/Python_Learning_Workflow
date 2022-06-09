#DATASET - NISPUF17.csv

#Write a function called proportion_of_education which returns the #
#proportion of children in the dataset who had a mother with the 
#education levels equal to less than high school (<12), high school (12), 
#more than high school but not a college graduate (>12) and college degree.

#This function should return a dictionary in the form of (use the correct numbers, do not round numbers):

#{"less than high school":0.2,"high school":0.4,
# "more than high school but not college":0.2,"college":0.2}

def proportion_of_education():
    #tc = total count
    import pandas as pd
    import numpy as np
    education = pd.read_csv('NISPUF17.csv',index_col='Unnamed: 0')
    r = education.EDUC1.unique()
    np.sort(r)
    tc = education['EDUC1'].count()
    tc
    #lths = less than high school
    lths= education[education['EDUC1']==1]
    lths = lths['EDUC1'].count()
    #hs = high school
    hs = education[education['EDUC1']==2]
    hs = hs['EDUC1'].count()
    #mthsnc = more than high school not college
    mthsnc = education[education['EDUC1']==3]
    mthsnc = mthsnc['EDUC1'].count()
    #c = college
    c = education[education['EDUC1']==4]
    c = c['EDUC1'].count()
    
    d = {'less than high school':lths/tc,
        'high school':hs/tc,
        'more than high school but not college':mthsnc/tc,
        'college':c/tc}
    return d

proportion_of_education()

#Let's explore the relationship between being fed breastmilk as a child and
#getting a seasonal influenza vaccine from a healthcare provider. Return a 
#tuple of the average number of influenza vaccines for those children we 
#know received breastmilk as a child and those who know did not.
#This function should return a tuple in the form (2.5,0.1)


def average_influenza_doses():
    import pandas as pd
    education = pd.read_csv('NISPUF17.csv',index_col='Unnamed: 0')

    avg_yes0 =  (education['P_NUMFLU']==0) & (education['CBF_01']==1)
    ay0 = education[avg_yes0]['P_NUMFLU'].count()
    ay0
    #3466 children were breastfed without any dose

    avg_yes1 =  (education['P_NUMFLU']==1) & (education['CBF_01']==1)
    ay1 = education[avg_yes1]['P_NUMFLU'].count()
    ay1
    #1395 children were breastfed with 1 dose

    avg_yes2 =  (education['P_NUMFLU']==2) & (education['CBF_01']==1)
    ay2 = education[avg_yes2]['P_NUMFLU'].count()
    ay2
    #2917 children were breastfed with 2 doses

    avg_yes3 =  (education['P_NUMFLU']==3) & (education['CBF_01']==1)
    ay3 = education[avg_yes3]['P_NUMFLU'].count()
    ay3
    #4334 children were breastfed with 3 doses

    avg_yes4 =  (education['P_NUMFLU']==4) & (education['CBF_01']==1)
    ay4 = education[avg_yes4]['P_NUMFLU'].count()
    ay4
    #1143 children were breastfed with 4 doses

    avg_yes5 =  (education['P_NUMFLU']==5) & (education['CBF_01']==1)
    ay5 = education[avg_yes5]['P_NUMFLU'].count()
    ay5
    #33 children were breastfed with 5 doses

    avg_yes6 =  (education['P_NUMFLU']==6) & (education['CBF_01']==1)
    ay6 = education[avg_yes6]['P_NUMFLU'].count()
    ay6
    #3 children were breastfed with 6 doses

    avg_no0 =  (education['P_NUMFLU']==0) & (education['CBF_01']==2)
    an0 = education[avg_no0]['P_NUMFLU'].count()
    an0
    #656 children were not breastfed without any dose

    avg_no1 =  (education['P_NUMFLU']==1) & (education['CBF_01']==2)
    an1 = education[avg_no1]['P_NUMFLU'].count()
    an1
    #277 children were not breastfed with 1 dose

    avg_no2 =  (education['P_NUMFLU']==2) & (education['CBF_01']==2)
    an2 = education[avg_no2]['P_NUMFLU'].count()
    an2
    #422 children were not breastfed with 2 doses

    avg_no3 =  (education['P_NUMFLU']==3) & (education['CBF_01']==2)
    an3 = education[avg_no3]['P_NUMFLU'].count()
    an3
    #503 children were not breastfed with 3 doses

    avg_no4 =  (education['P_NUMFLU']==4) & (education['CBF_01']==2)
    an4 = education[avg_no4]['P_NUMFLU'].count()
    an4
    #137 children were not breastfed with 4 doses

    avg_no5 =  (education['P_NUMFLU']==5) & (education['CBF_01']==2)
    an5 = education[avg_no5]['P_NUMFLU'].count()
    an5
    #2 children were not breastfed with 5 doses

    avg_no6 =  (education['P_NUMFLU']==6) & (education['CBF_01']==2)
    an6 = education[avg_no6]['P_NUMFLU'].count()
    an6
    #0 children were not breastfed with 6 doses

    avg_yes = ((ay0*0)+(ay1*1)+(ay2*2)+(ay3*3)+(ay4*4)+(ay5*5)+(ay6*6))/(ay0+ay1+ay2+ay3+ay4+ay5+ay6)
    avg_yes

    avg_no = ((an0*0)+(an1*1)+(an2*2)+(an3*3)+(an4*4)+(an5*5)+(an6*6))/(an0+an1+an2+an3+an4+an5+an6)
    avg_no
    return (avg_yes,avg_no)

average_influenza_doses()

#It would be interesting to see if there is any evidence of a link between
#vaccine effectiveness and sex of the child. Calculate the ratio of the 
#number of children who contracted chickenpox but were vaccinated against
#it (at least one varicella dose) versus those who were vaccinated but did
#not contract chicken pox. Return results by sex.

#This function should return a dictionary in the form of (use the correct numbers):
#{"male":0.2,"female":0.4}

def chickenpox_by_sex():
    import pandas as pd
    import numpy as np
    education = pd.read_csv('NISPUF17.csv',index_col='Unnamed: 0')

    c_p = education['HAD_CPOX']
    cp = education['HAD_CPOX'].unique()
    np.sort(cp)
    have_cp = c_p[c_p==1].count()
    nothave_cp = c_p[c_p == 2].count()

    v = education['P_NUMVRC'].dropna()
    vac = education['P_NUMVRC'].dropna().unique()
    vac = np.sort(vac)
    v[v!=0].count()

    male = education[education['SEX']==1]["SEX"].count()
    female = education[education['SEX']==2]['SEX'].count()

    malehcp = (education['SEX']==1) & (education['HAD_CPOX']==1) & (v!=0)
    malenhcp = (education['SEX']==1) & (education['HAD_CPOX']==2) & (v!=0)
    male_hcp = malehcp[malehcp].count()
    male_nhcp = malenhcp[malenhcp].count()

    femalehcp = (education['SEX']==2) & (education['HAD_CPOX']==1) & (v!=0)
    femalenhcp = (education['SEX']==2) & (education['HAD_CPOX']==2) & (v!=0)
    female_hcp = femalehcp[femalehcp].count()
    female_nhcp = femalenhcp[femalenhcp].count()

    ratio_male = male_hcp/male_nhcp
    ratio_female = female_hcp/female_nhcp
    ratio = {'male':ratio_male,
            'female':ratio_female}
    return ratio

chickenpox_by_sex()

 #In this question, you are to see if there is a correlation between having
 #had the chicken pox and the number of chickenpox vaccine doses given 
 #(varicella).

def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    education = pd.read_csv('assets/NISPUF17.csv',index_col='Unnamed: 0')
    cp = education[(education['HAD_CPOX']==1)|(education['HAD_CPOX']==2)]['HAD_CPOX']
    v = education['P_NUMVRC'].dropna()

    
    # this is just an example dataframe
    dff=pd.DataFrame({"had_chickenpox_column":cp,
                   "num_chickenpox_vaccine_column":v})
    dff = dff.dropna()

    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(dff["had_chickenpox_column"],dff["num_chickenpox_vaccine_column"])
    return corr

corr_chickenpox()
