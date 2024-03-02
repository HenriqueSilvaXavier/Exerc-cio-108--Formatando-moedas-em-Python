def metade(n):
    m=n/2
    m="{} ".format(m)
    f=m.replace(".", ",")
    f=f.replace(" ", "0")
    c="{} ".format(n)
    c=c.replace(".", ",")
    c=c.replace(" ", "0")
    print("A metade de R${} é R${}".format(c, f))
def dobro(n):
    m=n*2
    m="{} ".format(m)
    f=m.replace(".", ",")
    f=f.replace(" ", "0")
    c="{} ".format(n)
    c=c.replace(".", ",")
    c=c.replace(" ", "0")
    print("O dobro de R${} é {}".format(c, f))
def aumentar(n):
    m=n*1.1
    m="{} ".format(m)
    f=m.replace(".", ",")
    f=f.replace(" ", "0")
    print("Aumentando 10%, temos R${}".format(f))

n=input("Digite o preço: ")
if n.count(",")>0:
	n=n.replace(",", '.')
	n=float(n)
elif n.count(",")==0:
	n=float(n)
metade(n)
dobro(n)
aumentar(n)