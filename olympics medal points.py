import numpy
from pandas import DataFrame, Series


# def points():
#     '''
#     Imagine a point system in which each country is awarded 4 points for each
#     gold medal,  2 points for each silver medal, and one point for each
#     bronze medal.
#
#     Using the numpy.dot function, create a new dataframe called
#     'olympic_points_df' that includes:
#         a) a column called 'country_name' with the country name
#         b) a column called 'points' with the total number of points the country
#            earned at the Sochi olympics.
#
#     You do not need to call the function in your code when running it in the
#     browser - the grader will do that automatically when you submit or test it.
#     '''
#
#     countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
#                  'Netherlands', 'Germany', 'Switzerland', 'Belarus',
#                  'Austria', 'France', 'Poland', 'China', 'Korea',
#                  'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
#                  'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
#                  'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']
#
#     gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
#     silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
#     bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
#
#     # YOUR CODE HERE
#     olympic_medal_counts = {'country_name': Series(countries),
#                             'gold': Series(gold),
#                             'silver': Series(silver),
#                             'bronze': Series(bronze)}
#
#     olympic_medal_counts_df = DataFrame(olympic_medal_counts)
#     medal_counts = olympic_medal_counts_df[['gold', 'silver', 'bronze']]
#     points = numpy.dot(medal_counts, [4, 2, 1])
#     olympic_points = {'country_name': Series(countries), 'points': Series(points)}
#     olympic_points_df = DataFrame(olympic_points)
#
#     return olympic_points_df


countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
             'Netherlands', 'Germany', 'Switzerland', 'Belarus',
             'Austria', 'France', 'Poland', 'China', 'Korea',
             'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
             'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
             'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

# YOUR CODE HERE
olympic_medal_counts = {'country_name': Series(countries),
                        'gold': Series(gold),
                        'silver': Series(silver),
                        'bronze': Series(bronze)}
# print (olympic_medal_counts)
olympic_medal_counts_df = DataFrame(olympic_medal_counts)

print (olympic_medal_counts_df)

medal_counts = olympic_medal_counts_df[['gold', 'silver', 'bronze']]

print (medal_counts)
points = numpy.dot(medal_counts, [4, 2, 1])
print (points)
olympic_points = {'country_name': Series(countries), 'points': Series(points)}
print (olympic_points)
olympic_points_df = DataFrame(olympic_points)
print (olympic_points_df)
