import math
x = [2, -3, 5, 4, 7]
y = [10, 13, 15, 10]
print len (x)
print x [0]

#calculate the mean of a dataset
def mean(dataset):
    sum = 0
    for i in range (0, len(dataset)):
        sum = dataset[i] + sum
    return sum/len(dataset)
print mean(x)

#calculate the degrees of freedom of a dataset
def df_dataset(dataset):
    return len(dataset)-1

print df_dataset(x)

#calculate the degrees of freedom of the difference of two datasets
def df_xy(dataset1, dataset2):
    return df_dataset(dataset1) + df_dataset(dataset2)
print df_xy(x, y)

#calculate the deviation from the mean for each value of a dataset and return a table of each deviations from the mean
def dev_from_mean (dataset):
    new_table = []
    for i in range (0, len(dataset)):
        new_table.append(dataset[i] - mean (dataset))
    return new_table

print dev_from_mean(x)

#square each deviation from the mean of a dataset and return a table
def squared_deviation(dataset):
    new_dataset = []
    dev_dataset = dev_from_mean(dataset)
    for i in range (0, len(dev_dataset)):
        new_dataset.append((dev_dataset[i]**2))
    return new_dataset
print squared_deviation(x)

#calculate the sum of the squared deviations of a dataset
def sum_squared_dev(dataset):
    squared_dataset = squared_deviation(dataset)
    sum = 0
    for i in range (0, len(squared_dataset)):
        sum = sum + squared_dataset[i]
    return sum
print sum_squared_dev(x)

#calculate the pooled variance of two datasets
def pooled_variance(dataset1, dataset2):
    return (sum_squared_dev(dataset1)+sum_squared_dev(dataset2))/(df_xy(dataset1, dataset2)*1.0)
print pooled_variance(x, y)

#calculate the standard error when comparing two datasets
def standard_error_xy (dataset1, dataset2):
    return math.sqrt(pooled_variance(dataset1, dataset2)/len(dataset1)+pooled_variance(dataset1, dataset2)/len(dataset2))
print standard_error_xy(x, y)

#calculate the t-statistics when comparing two datasets
def t_stat(dataset1, dataset2, mu1, mu2):
    return ((mean(dataset1)-mean(dataset2)-(mu1-mu2))/standard_error_xy(dataset1, dataset2))
print t_stat(x, y, 0, 0)