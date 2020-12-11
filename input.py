# Sample 1
# name = input('What is your name : ')
# color = input('What is your favorite color : ')
# print('Your name ' + name + ' and your favorite color is ' + color)

# # Sample 2
# import datetime
# n = datetime.datetime.now() #print(n.year)
# birth_year = input('birth year : ')
# birth = int(birth_year)
# age = n.year - birth
# age = str(age)
# print('Your Age is ' + age)

# Sample 3
jk = input('Jenis Kelamin P/W : ')
tinggi = input('Tinggi Badan : ')
berat = input('Berat Badan : ')
bmi = int(berat) / ((int(tinggi)/100) * (int(tinggi)/100))
# print('Body Mass Index anda : ' + str(bmi))    

if jk == 'P':
    jk = 'Pria'
    if bmi < 18:
        infobmi = 'Kurus'
    elif bmi >= 18 and bmi < 25:
        infobmi = 'Normal'
    elif bmi >= 25 and bmi <= 27:
        infobmi = 'Kegemukan'
    elif bmi > 27:
        infobmi = 'Obesitas'  

elif jk == 'W':
    jk = 'Wanita'
    if bmi < 17:
        infobmi = 'Kurus'
    elif bmi >= 17 and bmi < 23:
        infobmi = 'Normal'
    elif bmi >= 23 and bmi <= 27:
        infobmi = 'Kegemukan'
    elif bmi > 27:
        infobmi = 'Obesitas'

print('Berdasarkan kemkes.go.id \nJenis Kelamin ' + jk + 
'\ndimana BMI anda adalah ' + str(bmi) + ',\nmaka anda kategori ' + infobmi)        