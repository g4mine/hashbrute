import hashlib, os
os.system('clear') #linux
#os.system('cls') #windows

wd = raw_input('Wordlist que deseja utilizar: ')
hash = raw_input('Digite a hash para quebrar: ')
hasht = raw_input('Digite o tipo da hash: ')
acpt = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

if hasht not in acpt:
	print '[!] Hash nao suportada!'
	print '[*] Hashs suportadas: '
	print '[+] md5, sha1, sha224, sha256, sha384, sha512'
	exit()

list = open(wd)
text = list.readlines()
encontrado = 0
for word in text:

	if word.endswith('\n'):

		word = word[:-1]
	if hasht == 'md5':
		brute = hashlib.md5(word).hexdigest()
	elif hasht == 'sha1':
		brute = hashlib.sha1(word).hexdigest()
	elif hasht == 'sha224':
		brute = hashlib.sha224(word).hexdigest()
	elif hasht == 'sha256':
		brute = hashlib.sha256(word).hexdigest()
	elif hasht == 'sha384':
		brute = hashlib.sha384(word).hexdigest()
	elif hasht == 'sha512':
		brute = hashlib.sha512(word).hexdigest()

	if brute == hash:
		encontrado = 1
if encontrado == 1:
	print '[+] Hash encontrada!'
        print '[*] A hash e: '+word
else:
	print '[-] Hash nao encontrada'
