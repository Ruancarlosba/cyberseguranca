try:
    a = float(input("digite o número A :"))
    b = float(input("digite o número B :"))
    
    print(a/b)
except ValueError as error:
    print("input ivalido, digite apenas numeros")

except ZeroDivisionError as error:
    print("naõ poder ser feita a divisaõ por zero") 
    
except Exception as error:
    print("algum error ocorreu")
    print(error)
    
finally:
    print("fim do programa")