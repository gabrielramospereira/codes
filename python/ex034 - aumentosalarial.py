salary = float(input("Informe seu salário: "))
if salary <= 1250:
    novo = (salary*0.15)+salary
else:
    novo = (salary*0.15)+salary

print("Seu novo salario eh: {}".format(novo))