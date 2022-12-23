#******************************* Welcome to the PyPassword generator *****************
#************************************************************************************************************
#****************************** I'm payakan , Website nd game developer *****************************

#import required libraries
import random

print("Welcome to the password generator\n")

#list of alphabetics letters
albha = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

#list of numbers
num = ['1,','2','3','4','5','6','7','8','9','0']

#list of sysmbol
symbol = ['!','@','#','$','%','^','&','*','(',')']

nr_letters = int(input(f"How many letters did you want in your password \n "))

nr_num = int(input(f"\nhow many numbers did you want in your password \n"))

nr_sym = int(input(f"\nhow many symbols did you want in your password \n"))

user_choice = input(f"\nChoose your password's security level : \n For hard - H , For low - L\n")

user_choice = user_choice.lower()

if user_choice == 'h':
	pyPaasword = []
	password = ''

	for n in range(0,nr_letters):
		pyPaasword.append(random.choice(albha))
	for n in range(0,nr_num):
		pyPaasword.append(random.choice(num))
	for n in range(0,nr_sym):
		pyPaasword.append(random.choice(symbol))

	random.shuffle(pyPaasword)
	for n in range(0,len(pyPaasword)):
		password += pyPaasword[n]
	print(f"\nThe generated password is {password}")

elif user_choice == 'l':
	pyPaasword = []
	password = ''

	for n in range(0,nr_letters):
		pyPaasword.append(random.choice(albha))
	for n in range(0,nr_num):
		pyPaasword.append(random.choice(num))
	for n in range(0,nr_sym):
		pyPaasword.append(random.choice(symbol))
	for n in range(0,len(pyPaasword)):
		password += pyPaasword[n]
	print(f"\nThe generated password is {password}")

else:
	print("you enterthe wrong letter")




