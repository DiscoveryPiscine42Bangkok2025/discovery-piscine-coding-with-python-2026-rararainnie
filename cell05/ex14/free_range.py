import sys

if len(sys.argv) != 3:
    print("none")
else:
    list = []
    for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        list.append(i)
    
    print(list)
    