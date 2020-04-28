#!/usr/bin/python3
i = 0
for i in range(99):
    print("{:02d},".format(i), end=" ")
i += 1
print(format(i))
