import pandas
import pandasql


def aggregate_query(filename):
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.

    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns=lambda x: x.replace(' ', '_').lower(), inplace=True)
    print (aadhaar_data.head())

    # Write a query that will select from the aadhaar_data table how many men and how
    # many women over the age of 50 have had aadhaar generated for them in each district.
    # aadhaar_generated is a column in the Aadhaar Data that denotes the number who have had
    # aadhaar generated in each row of the table.
    #
    # Note that in this quiz, the SQL query keywords are case sensitive.
    # For example, if you want to do a sum make sure you type 'sum' rather than 'SUM'.
    #

    # The possible columns to select from aadhaar data are:
    #     1) registrar
    #     2) enrolment_agency
    #     3) state
    #     4) district
    #     5) sub_district
    #     6) pin_code
    #     7) gender
    #     8) age
    #     9) aadhaar_generated
    #     10) enrolment_rejected
    #     11) residents_providing_email,
    #     12) residents_providing_mobile_number
    #
    # You can download a copy of the aadhaar data that we are passing
    # into this exercise below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/aadhaar_data.csv

    q = """
    SELECT
    gender, district, sum(aadhaar_generated)
    FROM
    aadhaar_data
    WHERE
    age > 50
    GROUP BY
    gender, district
    
    """ # your code here

    # Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    print (aadhaar_solution)
    return aadhaar_solution

aggregate_query("/home/tiffany/lab/Udacity_Python/aadhaar_data.csv")