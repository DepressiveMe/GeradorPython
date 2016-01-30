# -*- coding: UTF-8 -*-
import random, time 
def cc_issuer(choice):
	issuer_choice = {'1':'Visa', '2':'MasterCard'}
	issuer_choice_number = {'1':'4', '2':str(random.randint(1,5))}
	return issuer_choice[choice], issuer_choice_number[choice]
def random_eleven():
	random_numbers = ''
	for number in range(14):
		rand_number = random.randint(0,9)
		random_numbers += str(rand_number)
	return random_numbers
def verified_numbers(cc_number):
	new_numbers = 0
	counter = 0
	for number in cc_number:
		if(counter % 2 == 0):
			odd_result = int(number) * 2
			if(odd_result > 9):
				odd_result -= 9
			new_numbers += odd_result
		else:
			new_numbers += int(number)
		counter += 1
	if((new_numbers < 150) and (new_numbers % 10 == 0)):
		verifier_number = '0'
	else:
		rest = new_numbers % 10
		last_number = 10 - rest
		verifier_number = str(last_number)
	return verifier_number
def cc():
	option = ''
	while(option != '0'):
		print 'Digite 1 para obter um cartão de crédito de bandeira Visa, 2 para MasterCard. Digite 0 para encerrar o programa.'
		option = raw_input()
		start = time.time()
		if(option != '0'):
			print '\n\n\n\n\n'*2
			issuer, cc_number = cc_issuer(option)
			random_nums = random_eleven()
			cc_number += random_nums
			vf_n = verified_numbers(cc_number)
			cc_number += vf_n
			print '\aNúmero do Cartão de Crédito: %s\n\n' %(cc_number)
			print 'Bandeira: %s\n\n' %(issuer)
			elapsed = (time.time() - start)
			print 'Seu Cartão de Crédito foi gerado em %s segundos.\n\n\n\n\n' %(elapsed)
cc()