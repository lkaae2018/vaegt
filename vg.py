import random

def maaling():
    print("Udf�re m�ling!!!")
    #m�le program skallige her
    global maal
    maal=random.randrange(1,50)
    return


while True:
    b=input('''Tryk p� en tast for at fortage m�ling?
    Der m� ikke v�re noget p� v�gten!!!''')
    maaling()
    nulmaal=maal
    print("Nulm�ling="+str(nulmaal))
    a=input("l�g emner p� v�gten!!")
    maaling()
    print("m�l="+str(maal))
    maal=maal-nulmaal
    print("Emnet vejer:"+str(maal)+"gram")
    a=int(input('Tryk p� 1 for at fors�tte ellers 0 for stoppe? '))
    if a==0:
        break
