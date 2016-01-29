# -*- coding: UTF-8 -*-
import time, random
start = time.time()
def cc_issuer():
	global first_numbers
	first_numbers = []
	global issuing_network
	issuing_network = ''
	print 'Digite 1 para obter um cartão de crédito de bandeira Visa, 2 para MasterCard.'
	choice = raw_input()
	if(choice == '1'):
		first_numbers.append(4)
		issuing_network = 'Visa'
	elif(choice == '2'):
		issuer_one = 5
		issuer_two = random.randint(1,5)
		issuer = (issuer_one, issuer_two)
		first_numbers.extend(issuer)
		issuing_network = 'MasterCard'
	while(len(first_numbers) < 4):
		number = random.randint(0,9)
		first_numbers.append(number)
	print first_numbers
def random_eleven():
	global random_numbers
	random_numbers = []
	random_numbers += first_numbers
	while(len(random_numbers) < 15):
		number = random.randint(0,9)
		random_numbers.append(number)
	print random_numbers
def verified_numbers():
	new_numbers = []
	counter = 1
	for number in random_numbers:
		if(counter % 2 == 0):
			new_numbers.append(number)
		else:
			odd_result = number * 2
			if(odd_result > 9):
				odd_result -= 9
			new_numbers.append(odd_result)
		counter += 1
	sum_new_numbers = sum(new_numbers)
	print new_numbers
	print sum_new_numbers
	if((sum_new_numbers < 150) and (sum_new_numbers % 10 == 0)):
		random_numbers.append(0)
	else:
		rest = sum_new_numbers % 10
		last_number = 10 - rest
		random_numbers.append(last_number)
cc_issuer()
random_eleven()
verified_numbers()
elapsed = (time.time() - start)
print 'Seu cartão de crédito de bandeira %s foi gerado com o número %s em %s segundos' %(issuing_network, random_numbers, elapsed)
#UMA REFATORAÇÃO E UM APRIMORAMENTO DEIXARIA AS COISAS MAIS BACANAS :^)