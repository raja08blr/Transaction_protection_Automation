import csv
def rr(t):
    return t + 3


def test_1(d, input_d):
    fun = input_d
    print(fun(d))
    tt="filename"+"_"+str(d)
    print(tt)


# test_1(0, rr)
test_1(1, rr)

# write data to csv file
path = '/root/dynamic_analysis_framework/results'
data = ['ecommerce','amazon',0,'/root/dynamic_analysis_framework/tcp_dump_files','xyz']
with open('result.csv', 'a', newline='', encoding="utf-8") as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow(data)
