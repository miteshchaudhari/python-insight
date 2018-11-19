a = "Hello, World! "
print(a[0:4])  # substring from 0 to 4 (not including 4 index)
print(len(a))  # length of string
print(a.split(",")) 
b=a.split(",")  # split string in array
print(b[0]) # print array element
print(b[1][0:6])

print(b[1].strip())  # strip will remove white space from both side of string

print(a.lower())  # convert to lower case
print(a.upper())  # convert to upper case
print(a.replace("H","J"))

