import datetime
def summary(data):
    file=open("summary.txt", "a")
    file.write("DATE_TIME:  ")
    file.write(str(datetime.datetime.now().replace(microsecond=0)))
    file.write("\n")
    file.write(str(data).strip("{}"))
    file.write("\n")
    file.close()

