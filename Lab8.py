#Tyler Johnston

def main():
    n = int(input('What is the size of the table :')) 


    for i in range(n+1):
        print('------', end='')

    print('\n     ', end='')

    for i in range(1, n+1):
        print(' %3d ' % i, end='')

    print()

    for i in range(n+1):
        print('------', end='')
    print()

    for i in range(1, n+1):
        print('%2d ' % i, end='| ')

        for j in range(1, n+1):
            print(' %3d ' % (i*j), end='')
            
        print()
main()
print("Thank you :)")