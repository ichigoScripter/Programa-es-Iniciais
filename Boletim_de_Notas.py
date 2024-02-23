print("====BOLETIM DE NOTAS====")
m = float(input("Qual sua nota em Matemática? "))
p = float(input("Qual sua nota em Português? "))
h = float(input('Qual sua nota em Historia? '))
g = float(input('Qual sua nota em Geografia? '))
f = float(input('Qual sua nota em Física? '))
s = m+p+h+g+f
me = (m+p+h+g+f) / 5
print(f"\n \n====SUAS NOTAS====\nSua nota em Matemática é: {m} \nSua nota em Português é: {p}  \nSua nota em História é: {h} \nSua nota em Geografia é: {g} \nSua nota em Física é: {f} \nA soma total de suas notas são: {s} \nSua Média foi de: {me}")
