while True:
    inp = input(' введите команду: ')
    
    # условие выхода из цикла — должно вычислиться как True для прерывания очередной итерации цикла
    if inp != 'quit':
        break
    
    print('\tконец итерации')

print('конец цикла')
