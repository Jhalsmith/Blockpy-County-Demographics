#***Make sure to import County Demographics manually before you run the code, sometimes this code doesn't work
import county_demographics
import matplotlib.pyplot as plt

#Creating all of the functions

#Calculating the statistic for the County
def findCountyStat(State_Abbrev, County, Metric) :
    cntyList = county_demographics.get("County", "State", State_Abbrev)
    metricList = county_demographics.get(Metric, "State", State_Abbrev)
    cntyList.reverse()
    metricList.reverse()
    counter = 0
    #Returning the first vale of the list, since they are sorted alphabetically, and then by date
    for x in cntyList :
        if x == County :
            cntyAvg = metricList[counter]
            return cntyAvg
        else :
            counter += 1

#Creating a list with all of the counties in a state
def findAllCounties(State_Abbrev) :
    cntyList = county_demographics.get("County", 'State', State_Abbrev)
    cntyList.reverse()
    counter = 0
    #Making sure we don't index past the list length
    while counter < len(cntyList) - 1 :
        if cntyList[counter] == cntyList[counter + 1] :
            #Removing duplicate values
            cntyList.pop(counter)
        else :
            counter += 1
    cntyList.reverse()
    return cntyList

#Finding the average of all of the counties in the state
def findStateStat(State_Abbrev, Metric):
    cntyList = county_demographics.get("County", 'State', State_Abbrev)
    metricList = county_demographics.get(Metric, "State", State_Abbrev)
    cntyList.reverse()
    metricList.reverse()
    counter = 0
    cntyPopList = []
    while counter < len(cntyList) - 1:
        if cntyList[counter] == cntyList[counter + 1] :
            cntyPopList.append(counter)
            cntyList.pop(counter)
        else :
            counter += 1
    #Popping all of the duplicate values in the metric list as well to make the data accurate
    for x in cntyPopList :
        metricList.pop(x)
    stateAvg = round(sum(metricList) / len(metricList))
    return stateAvg

#Finding the National average by finding the averages of each state and then averaging those
def findNationalStat(metric) :
    stateAvgs = []
    for State in stateList :
        stateAvgs.append(findStateStat(State, metric))
    nationalAvg = round(sum(stateAvgs) / 50)
    return nationalAvg

#Talking to the user and asking for details
print("Hello! This program allows you to see how your choosen county compares")
print("to the state and country in a key demographic")
print(" ")
stateAbbrev = str(input("What state is your county in? (Input the abbreviation ex. SD) "))
stateAbbrev.upper()
print("Here are the counties in that state: " + str(findAllCounties(stateAbbrev)))
print(" ")
county = str(input("Which county do you want? Type it exactly as you see in the list."))
print("Here are all of the possible metrics to request: \n \n Population.Population Percent Change \n Population.2020 Population \n Population.Population per Square Mile \n \n Age.Percent Under 5 Years \n Age.Percent Under 18 Years \n Age.Percent 65 and Older \n \n Miscellaneous.Percent Female \n Miscellaneous.Veterans \n Miscellaneous.Foreign Born \n Miscellaneous.Living in Same House +1 Years \n Miscellaneous.Language Other than English at Home \n Miscellaneous.Manufacturers Shipments \n Miscellaneous.Mean Travel Time to Work \n Miscellaneous.Land Area \n \n Ethnicities.White Alone \n Ethnicities.Black Alone \n Ethnicities.American Indian and Alaskan Native Alone \n Ethnicities.Asian Alone \n Ethnicities.Native Hawaiian and Other Pacific Islander Alone \n Ethnicities.Two or More Races \n Ethnicities.Hispanic or Latino \n Ethnicities.White Alone, not Hispanics or Latino \n \n Housing.Homeownership Rate \n Housing.Median Value of Owner-Occupied Units \n Housing.Households \n Housing.Person per Household \n \n Education.High School or Higher \n Education.Bachelor's Degree or Higher \n \n Sales.Accommodation and Food Services Sales \n Sales.Retail Sales \n \n Income.Median Housold Income \n Income.Per Capita Income \n \n Employment.Nonemployer Establishments \n Employment.Firms.Total \n Employment.Firms.Men-Owned \n Employment.Firms.Women Owned \n Employment.Firms.Minority-Owned \n Employment.Firms.Nonminority-Owned \n Employment.Firms.Veteran-Owned \n Employment.Firms.Nonveteran-Owned") 
print("\n ^These are all of the possible metrics to request^ \n \n Visit https://corgis-edu.github.io/corgis/blockpy/county_demographics/ for descriptions of metrics")
print(" ")
metric = str(input("What metric are you looking for? Scroll up to see the options. Type it exactly as you see it, or copy and paste it in with no space at the beginning and end."))
print("If it returns an error, there might be a typo. Check the website for the correct metric names and try again if so.")
stateList = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#Making the calculated stats reusable
County_Stat = findCountyStat(stateAbbrev, county, metric)
State_Stat = findStateStat(stateAbbrev, metric)
National_Stat = findNationalStat(metric)

#Making a bar graph with proper labels based off the metric of choice
#Also I have no idea what ys = 10 does but blockpy wanted a value so I gave one and nothing seems to be wrong
print(" ")
plt.bar([County_Stat, State_Stat, National_Stat], ys = 10, tick_label = ["County Statistic: " + str(County_Stat), "State Average: " + str(State_Stat), "National Average: " + str(National_Stat)])
plt.ylabel(str(metric))
plt.xlabel("The county statisitc, the average for all counties in " + str(stateAbbrev) + ", and the average for all states in the country")
plt.title("Values of the " + str(metric) + "  metric at the County, State, and National Level")
#The most important line of code
plt.show()



