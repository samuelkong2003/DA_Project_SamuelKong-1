#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: Samuel Kong
#Group Name: Python_underdog
#Class: PN2004J
#Date: 9 Feb 2021
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import matplotlib for pie chart
import matplotlib.pyplot as pit
#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthlyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)

  #Slicing
  c_df = df[['Year','Month'] + df.iloc[:, 20: 31].columns.tolist()]
  
  #Form a new database based on new index
  c_df = c_df.reset_index(drop=True)
  
  #Display selected countries
  print("The following new dataframe for Europe from 1996 - 2006 are read as follows: \n")
  print(c_df) 

  #Sort countries base on ascending order
  top3countries = c_df.iloc[:, 2:13].sum(axis=0).sort_values(ascending=False).nlargest(3).reset_index()

  #sort sum value output into columns based on country and visitors
  top3countries.columns = ['Country', 'Visitors']
  #change index to represent top 3
  top3countries.index = ['Most Visted →', 'Second Most Visted → ', 'Third Most Visted →']

  #Pie Chart
  Activities = ['United Kingdom', 'Germany', 'France']
  #Pie Chart information
  slices = [13507316, 6412786, 3386103]

  pit.pie(slices, 
          labels = Activities,
          startangle = 90,
          shadow = True,
          explode = (0.2, 0, 0),
          autopct = '%1.2f%%')
  pit.legend()
  
  #Display Pie Chart
  pit.show
  
  #Display most visitors from 1996 to 2016
  print("\nThe top 3 countries with the most visitors coming to Singapore listed in Europe from 1996 to 2016 are read as follows:\n")

  #display top 3
  print(top3countries)
  

  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################