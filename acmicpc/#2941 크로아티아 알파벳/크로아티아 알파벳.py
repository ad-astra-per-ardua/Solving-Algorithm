standard = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']
string = input()

for i in standard:
    string = string.replace(i, 'a')
print(len(string))