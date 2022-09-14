pattern_width = int(input("Please enter pattern width: "))
for i in range(0, pattern_width):
    print("*" * (i+1))

for i in range(pattern_width-1, 0, -1):
    print("*" * i)