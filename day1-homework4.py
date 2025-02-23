import random

#way1
section1=random.randint(1,255)
section2=random.randint(1,255)
section3=random.randint(1,255)
section4=random.randint(1,255)

random_ipv4=str(section1)+'.'+str(section2)+'.'+str(section3)+'.'+str(section4)

print(random_ipv4)

#way2
# random_ipv4 = ".".join(str(random.randint(1, 255)) for _ in range(4))
# print(random_ipv4)