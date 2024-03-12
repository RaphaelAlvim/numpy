import os # importando a biblioteca os

cpu_num = os.cpu_count() # obter o número de CPUs no sistema
print(f"Meu computador tem {cpu_num} núcleos de CPU") # imprimir o número de CPUs

