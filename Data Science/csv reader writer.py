import csv
import pandas as pd

df = pd.read_csv("/home/tiffany/lab/Udacity_Python/Choco.csv")
print df

data_in = open("/home/tiffany/lab/Udacity_Python/Choco.csv", 'r')
data_out = open("/home/tiffany/lab/Udacity_Python/outChoco.csv", 'w')
# print data_in

for line in data_in:
    # print line
    # print type(line)
    line_out = []
    i = 0
    for entry in line:
        if i == 0:
            line_out.append(entry)
        elif (i % 4 != 0):
            line_out.append(entry)
        else:
            line_out.append(entry)
            print(line_out)


# reader_in = csv.reader(data_in, delimiter=',')
# writer_out = csv.writer(data_out, delimiter=',')
# reader_in.next()

# for line in reader_in:
#     line_1 = []
#     line_2 = []
#     i = 0
#     for entry in line:
#         if i == 0:
#             line_1.append(entry)
#         elif (i % 4 != 0):
#             line_1.append(entry)
#         else:
#             line_1.append(entry)
#             print(line_1)


        # if i == 0 :
        #     line_1.append(entry)
        #     line_2.append(entry)
        # elif 1 <= i <= 4:
        #     line_1.append(entry)
        # else:
        #     line_2.append(entry)

            # line_2 = [line[0], line[5], line[6], line[7], line[8]]
#     writer_out.writerow(line_1)
#     writer_out.writerow(line_2)
#
#
# data_in.close()
# data_out.close()