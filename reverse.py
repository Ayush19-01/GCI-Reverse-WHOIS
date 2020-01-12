import requests
from bs4 import BeautifulSoup as bs4
def prRed(skk): return str("\033[91m {}\033[00m" .format(skk)) 
def prYellow(skk): return str("\033[93m {}\033[00m" .format(skk)) 
def prPurple(skk): return str("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): return str("\033[96m {}\033[00m" .format(skk)) 
def main():
	print()
	query = input(prRed("Enter the name of individual person or a company:"))
	print()
	link = "https://viewdns.info/reversewhois/?q=" + query
	user = "Mozilla/5.0 (X11; Linux i586; rv:71.0) Gecko/20100101 Firefox/71.0"
	headers = {"User-Agent": user}
	request = requests.get(link, headers=headers)
	table1 = bs4(request.content, "html5lib")
	table1 = table1.findAll('table')[3].encode()
	try1 = bs4(table1, "html5lib")
	row = try1.findAll('tr')
	test=1
	mainlist=[]
	for i in row:
		if test==1:
			test+=1
			continue
		else:
			x=str(i)
			y=x.split("<td>")
			tmplist=[]
			for j in y:
				if j=='<tr>':
					continue
				else:
					z=j[:-5]
					if "</td>" in z:
						z=z[:-5]
					if z=="":
						z="N/A"
					tmplist.append(z)
			mainlist.append(tmplist)
	if len(mainlist)==0:
		print(prRed("Insufficient Data"))
	else:
		print("{:53}{:39}{}".format(prRed("Domain Name"),prRed("Creation Date"),prRed("Registrar")))
		print()
		for l in mainlist:
			tmpx=l[0]
			tmpy=l[1]
			tmpz=l[2]
			print("{:54}{:35}{}".format(prPurple(tmpx),prYellow(tmpy),prCyan(tmpz)))
			print()
	xt=input(prCyan("Do you wish to continue?[y/N]:"))
	print()
	if xt=="y":
		main()
	if xt=="N":
		print(prRed("Closing..."))
		return None
	else:
		return None
main()
