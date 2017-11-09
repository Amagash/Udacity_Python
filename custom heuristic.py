import numpy
import pandas
import statsmodels.api as sm


# def custom_heuristic(file_path):
#     '''
#     You are given a list of Titantic passengers and their associated
#     information. More information about the data can be seen at the link below:
#     http://www.kaggle.com/c/titanic-gettingStarted/data
#
#     For this exercise, you need to write a custom heuristic that will take
#     in some combination of the passenger's attributes and predict if the passenger
#     survived the Titanic diaster.
#
#     Can your custom heuristic beat 80% accuracy?
#
#     The available attributes are:
#     Pclass          Passenger Class
#                     (1 = 1st; 2 = 2nd; 3 = 3rd)
#     Name            Name
#     Sex             Sex
#     Age             Age
#     SibSp           Number of Siblings/Spouses Aboard
#     Parch           Number of Parents/Children Aboard
#     Ticket          Ticket Number
#     Fare            Passenger Fare
#     Cabin           Cabin
#     Embarked        Port of Embarkation
#                     (C = Cherbourg; Q = Queenstown; S = Southampton)
#
#     SPECIAL NOTES:
#     Pclass is a proxy for socioeconomic status (SES)
#     1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower
#
#     Age is in years; fractional if age less than one
#     If the age is estimated, it is in the form xx.5
#
#     With respect to the family relation variables (i.e. SibSp and Parch)
#     some relations were ignored. The following are the definitions used
#     for SibSp and Parch.
#
#     Sibling:  brother, sister, stepbrother, or stepsister of passenger aboard Titanic
#     Spouse:   husband or wife of passenger aboard Titanic (mistresses and fiancees ignored)
#     Parent:   mother or father of passenger aboard Titanic
#     Child:    son, daughter, stepson, or stepdaughter of passenger aboard Titanic
#
#     Write your prediction back into the "predictions" dictionary. The
#     key of the dictionary should be the passenger's id (which can be accessed
#     via passenger["PassengerId"]) and the associating value should be 1 if the
#     passenger survvied or 0 otherwise.
#
#     For example, if a passenger is predicted to have survived:
#     passenger_id = passenger['PassengerId']
#     predictions[passenger_id] = 1
#
#     And if a passenger is predicted to have perished in the disaster:
#     passenger_id = passenger['PassengerId']
#     predictions[passenger_id] = 0
#
#     You can also look at the Titantic data that you will be working with
#     at the link below:
#     https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv
#     '''

predictions = {}
df = pandas.read_csv("/home/tiffany/lab/Udacity_Python/titanic-data.csv")
# print (len(df))
# print (df[(df.Sex == "female") & (df.Age > 18)])
# subdf = (df[(df.Survived == 1) & (df.Sex == "male") & (df.Age > 5)])
sub_survived = (df[(df.Survived == 1)])
sub_notsurvived = (df[(df.Survived == 0)])
sub_male = df[(df.Sex == "male")]
sub_male_survived = (sub_survived[(sub_survived.Sex == "male")])
sub_male_notsurvived = (sub_notsurvived[(sub_notsurvived.Sex == "male")])
sub_fem_survived = (sub_survived[(sub_survived.Sex == "female")])
sub_female_notsurvived = (sub_notsurvived[(sub_notsurvived.Sex == "female")])
print (sub_male_survived.describe())
print (sub_male_notsurvived.describe())
print ('')
print (sub_fem_survived.describe())
print (sub_female_notsurvived.describe())
# sub_female = (df[(df.Sex == "female")])

#
# sub_fem1 = sub_fem_survived[(sub_fem_survived.Pclass == 1)]
#
# sub_fem1_18 = sub_fem1[(sub_fem1.Age < 18)]
# print (sub_fem1_18)
# sub_fem2 = sub_fem_survived[(sub_fem_survived.Pclass == 2)]
# sub_fem3 = sub_fem_survived[(sub_fem_survived.Pclass == 3)]

print (len(sub_male_survived)*100/len(sub_survived))
# print (sub_fem1_18)
print (sub_male_survived[["Pclass", "Age", "Parch", "Embarked", "Fare"]])
# football[(football.wins > 10) & (football.team == "Packers")]

for passenger_index, passenger in df.iterrows():
    passenger_id = passenger['PassengerId']
    # if passenger['Sex'] == 'female':
    #     predictions[passenger_id] = 1
    # elif passenger['Age'] < 18:
    #     predictions[passenger_id] = 1
    # elif passenger['Pclass'] == 1 and passenger['Age'] < 18:
    #     predictions[passenger_id] = 1
    # elif passenger["SibSp"] > 1:
    #     predictions[passenger_id] = 1
    # else:
    #     predictions[passenger_id] = 0
# return predictions
