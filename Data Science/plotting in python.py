# from pandas import *
from ggplot import *

import pandas as pd
datafile = "/home/tiffany/lab/Udacity_Python/hr_year.csv"

def lineplot(hr_year_csv):
    # A csv file will be passed in as an argument which
    # contains two columns -- 'HR' (the number of homerun hits)
    # and 'yearID' (the year in which the homeruns were hit).
    #
    # Fill out the body of this function, lineplot, to use the
    # passed-in csv file, hr_year.csv, and create a
    # chart with points connected by lines, both colored 'red',
    # showing the number of HR by year.
    #
    # You will want to first load the csv file into a pandas dataframe
    # and use the pandas dataframe along with ggplot to create your visualization
    #
    # You can check out the data in the csv file at the link below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/hr_year.csv
    #
    # You can read more about ggplot at the following link:
    # https://github.com/yhat/ggplot/

    df = pd.read_csv(hr_year_csv)
    print (df)

    print (ggplot(df, aes("yearID", "HR")) +
                  geom_point(color = "red") +
                  geom_line(color = "red") +
                  ggtitle("Total HRs by year") +
                  xlab("Year")+
                  ylab("HR")

           )
    # gg =  # YOUR CODE GOES HERE
    # return gg

lineplot(datafile)

# df = pd.read_csv("/home/tiffany/lab/Udacity_Python/hr_year.csv")
# print (df)
#
# print (ggplot(df, aes("yearID", "HR"))+geom_point(color = 'red'))
# # + geom_point(color="red") + geom_line(color="red") + ggtitle("Total HRs by year") + xlab("Year") + ylab("HR"))