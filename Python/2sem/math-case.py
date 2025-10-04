op = 1
if op == 1:
    print('bomdia')
elif op == 2:
    print('tarde')
elif op == 3:
    print('noite')
else: 
    print('ta bom')

match op:
    case 1:
        print('bomdia')
    case 2: 
        print('tarde')
    case 3:
        print('noite')
    case _:
        print('tchau')
