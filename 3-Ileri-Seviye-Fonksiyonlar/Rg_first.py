#nested Function (iç içe fonksiyonlar)

def topla(x):
    print("dışarıdaki fonksiyon")
    def ekleme_yap(y):
        print("içerideki fonskiyon")
        return x+y
    return ekleme_yap


a=topla(20)(3)
print(a) #output:23

# *args,**kwargs

def sayi_gir(*args): #Birçok girdi almak için kullanılır.
    print(*args)

sayi_gir(1,2,3,4,5,20,20,20)


def dict_gir(**kwargs):
    for key, value in kwargs.items(): 
        print ("{} ==> {}".format(key, value))
dict_gir(bir ='1', iki ='2', uc='3')

