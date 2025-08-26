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
date = 1

str1 = f"{qyt}'{day} {year}-{month:02d}-{date:02d}"

print(str1)

# print(f"{qyt}'{day} {year}-{month}-{date}")

# print(f"{qyt}'{day} {year}-{month:02d}-{date:02d}")

# #左填充
# formatted_date = f"{year}-{month:d}-{date:*>2d}"
# print(f"{qyt}'{day} {formatted_date}")

# #右填充
# formatted_date = f"{year}-{month:d}-{date:*<2d}"
# print(f"{qyt}'{day} {formatted_date}")