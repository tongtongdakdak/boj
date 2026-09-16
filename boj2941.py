word = input()
alpahbet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in alpahbet:
    word = word.replace(i,'*')
print(len(word))