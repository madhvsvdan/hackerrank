# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phonebook = dict()

for i in range(n):
    contacts = input()
    contacts = contacts.split()
    phonebook[contacts[0]] = phonebook.get(contacts[0],contacts[1])

while True:
    try:
        j = input()
        if j in phonebook:
            print(f'{str(j)}={str(phonebook[j])}')
        else:
            print('Not found')
    except:
        break
