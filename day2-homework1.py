#way1
qyt = "QYTANG"
day = "day"
year = 2014
month = 9
date = 28
print(qyt + "'" + day + " " + str(year) + "-" + str(month) + "-" + str(date))

#way2
qyt = "QYTANG"
day = "day"
year = 2014
month = 9
date = 28

# 使用f-string格式化字符串，提高可读性
formatted_date = f"{year}-{month:02d}-{date:02d}"  # 确保月份和日期是两位数格式

print(f"{qyt}'{day} {formatted_date}")