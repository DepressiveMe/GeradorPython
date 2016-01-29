# -*- coding: UTF-8 -*-
import random, time
def random_numbers():
	first_numbers = ''
	for number in range(9):
		random_number = random.randint(0,9)
		first_numbers += str(random_number)
	return first_numbers
def verifier(first_numbers, factor):
	sum_mult_results = 0
	mult_factor = factor
	for number in first_numbers:
		mult = int(number) * mult_factor
		sum_mult_results += mult
		mult_factor -= 1
	rest_sum_result = sum_mult_results % 11
	if(rest_sum_result < 2):
		verifier = 0
	else:
		verifier = 11 - rest_sum_result
	return str(verifier)
def cpf():
	option = ''
	while(option != '0'):
		print 'Aperte ENTER para gerar um CPF válido. Digite 0 para encerrar o programa.'
		option = raw_input()
		start = time.time()
		if(option != '0'):
			print '\n\n\n\n\n'*2
			cpf_number = random_numbers()
			first_verifier = verifier(cpf_number, 10)
			second_verifier = verifier(cpf_number + first_verifier, 11)
			cpf_number += first_verifier + second_verifier
			state = {'0':'Rio Grande do Sul', '1':'Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins', '2':'Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima', '3':'Ceará, Maranhão ou Piauí', '4':'Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas', '5':'Bahia ou Sergipe', '6':'Minas Gerais', '7':'Rio de Janeiro ou Espírito Santo', '8':'São Paulo', '9':'Paraná ou Santa Catarina'}
			print '\aCPF: %s.%s.%s-%s\n\n' %(cpf_number[0:3], cpf_number[3:6], cpf_number[6:9], cpf_number[9:])
			print 'Localização de registro do CPF: %s\n\n' %(state[cpf_number[8]])
			elapsed = (time.time() - start)
			print 'O CPF foi gerado em %s segundos\n\n\n\n\n' %(elapsed)
cpf()