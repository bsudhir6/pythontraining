import sys ##Module for system operations.

a = sys.argv[1] ##argv brings command line argument.
b = sys.argv[2]

a = int (a) #type conversion from String to Int
b = int (b) #type conversion from String to Int

print(a+b) #prints integer addition result
print(int(a) + int(b))
