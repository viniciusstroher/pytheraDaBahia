from check_csv_file import *

def call_menu():
	print("Cheking IPS\n\n")

	manual_arquivo = input("manual verification[m]\nautomatic using the CSV ips.csv [a]\n")

	if (manual_arquivo == 'm'):
		# ip = input('type the IP: ')
		# ip_list = [ip]
		# check_specific_ip(ip_list)
		print('Chama o check_specific_ip\n')
	elif (manual_arquivo == 'a'):
		print('Chama o check_csv_file\n')
		ip_list = load_csv_file() # carrega arquivo do csv para uma lista
		check_the_ip_list(ip_list) # envia a lista de ips carregas do csv para processar na funcao check_the_ip_list
	else:
		print('select a valid option\n')
		call_menu()