def split():
    a = input("Copy text and paste it, then press ENTER ")
    b = a.split()
    print(b)
    
split()


# If you Join

def join():
    b = split()
    join2 = ' '.join(b)
    print(join2)

join()
