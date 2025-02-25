# #way1
# qyt = "QYTANG"
# day = "day"
# year = 2014
# month = 9
# date = 28
# print(qyt + "'" + day + " " + str(year) + "-" + str(month) + "-" + str(date))

#way2
qyt = "QYTANG"
day = "day"
year = 2014
month = 9
date = 28

formatted_date = f"{year}-{month:d}-{date:02d}"

print(f"{qyt}'{day} {formatted_date}")