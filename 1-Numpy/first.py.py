import sqlite3

connect=sqlite3.connect("my.db")

cursor=connect.cursor()

#cursor.execute("create table urunler (id int AUTO_INCREMENT,Model_No TEXT ,Urun_Adi varchar(255),Stok varchar(255),Fiyat int)")


def urun_ekleme():
   
    x=input(""" 
        musteri_kisisel => 1 
        siparisler => 2 
        urun_ozellik => 3 
        urunler =>4

        Eklemek istediğiniz girdiyi seçiniz..
    """)

    print("Seçilen işlem =>",x,"numaralı işlem ")
    connect.commit()    



urun_ekleme()

