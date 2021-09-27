import ipaddress
import csv

def load_csv_file():
	with open('ips.csv', newline='') as file:
		reader = csv.reader(file)
		ip_list = list(reader)
		return ip_list

def check_the_ip_list(ip_list):
	linhasDoArquivoLido = len(ip_list) # retorna o numero de linhas do csv (o ip_list é uma variavel do tipo lista)

	print(ip_list[0][2])

	for indiceDaLInha in range(linhasDoArquivoLido):
		linhaDoArquivo = ip_list[indiceDaLInha] # lista contendo subnets
		quantidadeDeSubnets = len(linhaDoArquivo) # quandidade de subnets da linha

		print('linha: '+str(indiceDaLInha)+' - '+str(linhaDoArquivo)+' - '+str(quantidadeDeSubnets)+'\n')

		for ip in ip_list[indiceDaLInha]:
			print('IP: '+ip+'\n')
			check_ip(ip)

def check_ip(ip):
	if (ipaddress.ip_address(ip) in ipaddress.ip_network('13.107.136.0/22')):
		print('SharePoint ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('13.107.18.10/31')):
		print('Exchange ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('40.104.0.0/15')):
		print('Exchange ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('40.118.128.0/17')):
		print('SharePoint ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('40.96.0.0/13')):
		print('Exchange ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('52.104.0.0/14')):
		print('SharePoint ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('104.146.128.0/17')):
		print('SharePoint ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('150.171.40.0/22')):
		print('SharePoint ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('13.107.6.152/31')):
		print('Exchange ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('13.107.128.0/22')):
		print('Exchange ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('23.103.160.0/20')):
		print('Exchange ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('52.96.0.0/14')):
		print('Exchange ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('131.253.33.215/32')):
		print('Exchange ' + ip)	
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('132.254.0.0/16')):
		print('Exchange ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('150.171.32.0/22')):
		print('Exchange ' + ip)
	elif (ipaddress.ip_address(ip) in ipaddress.ip_network('204.79.197.215/32')):
		print('Exchange ' + ip)														
	else:
		print('it is not in any of the ranges')