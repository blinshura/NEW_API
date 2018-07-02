with open('logins.txt', 'r') as logins:
    LOGIN = logins.read().split('\n')


LOGINs = []
PASSWORDs = []
a=0
for i in LOGIN[::2]:
    print(LOGIN[a] + ' ' + LOGIN[a+1])
    a+=2

# myfile = open("logins.txt", "rU") #чтение из файла
# for line in myfile.xreadlines(): #построчно читаем файл и выводим на экран
#     print (line)
#     print(str(LOGIN) + ' ' + str(PASSWORD))