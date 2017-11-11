import pandas
import pandasql
import csv


def num_rainy_days(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data.  The SQL query should return one column and
    one row - a count of the number of days in the dataframe where
    the rain column is equal to 1 (i.e., the number of days it
    rained).  The dataframe will be titled 'weather_data'. You'll
    need to provide the SQL query.  You might find SQL's count function
    useful for this exercise.  You can read more about it here:

    https://dev.mysql.com/doc/refman/5.1/en/counting-rows.html

    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be useful to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply
    where maxtempi = 76.

    You can see the weather data that we are passing in below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)
    # print (weather_data)
    print (weather_data.columns.values)
    print (weather_data[['date','rain']])

    q = """
    SELECT COUNT (*) FROM weather_data WHERE rain == 1;
    """

    # Execute your SQL command against the pandas frame
    rainy_days = pandasql.sqldf(q.lower(), locals())
    print (rainy_days)
    return rainy_days

# num_rainy_days("/home/tiffany/lab/Udacity_Python/weather_underground.csv")


def max_temp_aggregate_by_fog(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data.  The SQL query should return two columns and
    two rows - whether it was foggy or not (0 or 1) and the max
    maxtempi for that fog value (i.e., the maximum max temperature
    for both foggy and non-foggy days).  The dataframe will be
    titled 'weather_data'. You'll need to provide the SQL query.

    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be useful to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply
    where maxtempi = 76.

    You can see the weather data that we are passing in below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)
    print (weather_data.columns.values)
    print (weather_data[['date','fog', 'maxtempi']])

    q = """
    SELECT fog, MAX(maxtempi) FROM weather_data GROUP BY fog
    """

    # Execute your SQL command against the pandas frame
    foggy_days = pandasql.sqldf(q.lower(), locals())
    print (foggy_days)
    return foggy_days

# max_temp_aggregate_by_fog("/home/tiffany/lab/Udacity_Python/weather_underground.csv")

import pandas
import pandasql


def avg_weekend_temperature(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data.  The SQL query should return one column and
    one row - the average meantempi on days that are a Saturday
    or Sunday (i.e., the the average mean temperature on weekends).
    The dataframe will be titled 'weather_data' and you can access
    the date in the dataframe via the 'date' column.

    You'll need to provide  the SQL query.

    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be useful to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply
    where maxtempi = 76.

    Also, you can convert dates to days of the week via the 'strftime' keyword in SQL.
    For example, cast (strftime('%w', date) as integer) will return 0 if the date
    is a Sunday or 6 if the date is a Saturday.

    You can see the weather data that we are passing in below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)
    print (weather_data.columns.values)
    print (weather_data[['date', 'meantempi']])

    q = """
    SELECT AVG(cast (meantempi as integer)) 
    FROM weather_data 
    WHERE (cast (strftime('%w', date) as integer) == 0) 
    OR (cast (strftime('%w', date) as integer) == 6)
    """

    # Execute your SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    print mean_temp_weekends
    return mean_temp_weekends

# avg_weekend_temperature("/home/tiffany/lab/Udacity_Python/weather_underground.csv")

def avg_min_temperature(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data. More specifically you want to find the average
    minimum temperature (mintempi column of the weather dataframe) on
    rainy days where the minimum temperature is greater than 55 degrees.

    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be useful to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply
    where maxtempi = 76.

    You can see the weather data that we are passing in below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)
    print (weather_data.columns.values)
    print (weather_data[['rain', 'mintempi']])

    q = """
    SELECT AVG(mintempi)
    FROM weather_data
    WHERE rain == 1 AND mintempi > 55
    """

    # Execute your SQL command against the pandas frame
    avg_min_temp_rainy = pandasql.sqldf(q.lower(), locals())
    print (avg_min_temp_rainy)
    return avg_min_temp_rainy

# avg_min_temperature("/home/tiffany/lab/Udacity_Python/weather_underground.csv")

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file.

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the
    Instructor Notes below for more details on the task.

    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy

    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:

    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    # for name in filenames:

    txt = pandas.read_csv(filenames)
    # print txt.head()

    f_in = open("/home/tiffany/lab/Udacity_Python/turnstile_110507.txt", 'r')
    f_out = open("/home/tiffany/lab/Udacity_Python/updated_turnstile_110507.txt", 'w')


    reader_in = csv.reader(f_in, delimiter=',')
    writer_out = csv.writer(f_out, delimiter=',')
    # reader_in.next()

    for line in reader_in:
        for entry in line:





        # print (line)
        # line_1 = [line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7]]
        #
        # writer_out.writerow(line_1)

    print (writer_out)

    # f_in.close()
    # f_out.close()
    #
    # f_in = open(filenames, 'r')
    # f_out = open("updated_" + filenames, 'w')
    #
    # reader_in = csv.reader(f_in, delimiter=',')
    # writer_out = csv.writer(f_out, delimiter=',')
    #
    # for nane in filenames:
    #     writer_out.writerow([nane[0], nane[1], nane[2], nane[3], nane[4], nane[5], nane[6], nane[7]])
    #
    # f_in.close()
    # f_out.close()

    # Create file input object f_in to work with turnstile data
    f_in = open(filenames, 'r')
    # Create file output object f_out to write to the new output turnstile data
    f_out = open("updated_" + filenames, 'w')
    # create csv reader and writer based on our file objects
    reader_in = csv.reader(f_in, delimiter=',')
    writer_out = csv.writer(f_out, delimiter=',')
    for line in reader_in:
        control_area = line[0]
        remote_unit = line[1]
        scp = line[2]
        line_1 = [control_area, remote_unit, scp, line[3], line[4], line[5],
                  line[6], line[7]]
        # Write the new lines into the updated turnstile file
        writer_out.writerow(line_1)
    # Close the input and output object files
    f_in.close()
    f_out.close()

    for filename in filenames:
        name_in = open(filename)
        reader_in = csv.reader(name_in, delimiter=',')
        updated_filename = "updated_" + filename
        name_out = open(updated_filename)
        reader_out = csv.writer(name_out, delimiter=',')
        for line in name_in:
            control_area = line[0]
            remote_unit = line[1]
            scp = line[2]
            line_1 = [control_area, remote_unit, scp, line[3], line[4], line[5],
                      line[6], line[7]]
            reader_out.writerow(line_1)
        name_in.close()
    name_out.close()



fix_turnstile_data("/home/tiffany/lab/Udacity_Python/turnstile_110507.txt")