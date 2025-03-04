#kimi
port_list = ['eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7', 'eth 1/101/2/46', 'eth 1/101/1/34', 'eth 1/101/1/18', 'eth 1/101/1/13', 'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8']

sorted_port_list = sorted(port_list, key=lambda x: (int(x.split('/')[2]), int(x.split('/')[3])))

print(sorted_port_list)

#deepseek
# port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
#
# sorted_port_list = sorted(port_list, key=lambda x: tuple(map(int, x.split()[1].split('/'))))
#
# print(sorted_port_list)

#(int(x.split('/')[2]), int(x.split('/')[3])))
# x = 'eth 1/101/1/42'
# temp_strx = x.split('/')
# print(temp_strx)
# print(temp_strx[2])
# print(temp_strx[3],"\n")

#tuple(map(int, x.split()[1].split('/')))
# y = 'eth 1/101/1/42'
# print(y.split())
# print(y.split()[1])
# print(y.split()[1].split('/'))
# print(map(int,y.split()[1].split('/')))
