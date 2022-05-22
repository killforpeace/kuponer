#kupon uygulamasina ait musteri hizmetleri bolumu

from ctypes import pointer
import random
import time
import sqlite3

vt = sqlite3.connect('cpndtbase.sqlite')

im = vt.cursor()

table = ("""CREATE TABLE IF NOT EXISTS coupons
(cpn, bckpcpn)""")

enter_value = """INSERT INTO coupons VALUES (198567631, 189192961)"""

im.execute("""SELECT * FROM coupons  """)
data = im.fetchall()


im.execute(enter_value)

im.execute(table)



vt.commit()
vt.close()





while True:
 
 print("Merhaba, satin alimlariniz uzerinden kupon kazandiginiz kuponer uygulamasina hosgeldiniz! Lutfen yapmak istediginiz islemi seciniz: \n")
 options = input("1-Kupon numarasi alma \n 2-Alinan kupon numarasi gecerliligi sorgulama \n 3-Musteri hizmetleri \n 4-Anket \n 5-Calisan girisi \n")
 customercomplist = []
 workerlist = []
 workerorder = []


 class services():
     passing = "Gecis yapiliyor..."
     logout = "Cikis yapiliyor..."
     goodday = "Iyi gunler dileriz..."
     unkownmis = "Beklenmedik hata."
     verify = "Olusturuluyor..."
     
 
 def couponcreater(number , replace):
     print(number * replace)
 
 def complaincreater(name,surname,seccode,complain):
     customercomp = print(name , "isimli" , surname , "soyisimli" , seccode , "gizlilik kodlu kisinin" , complain , "sikayeti alinmistir." )
     customercomplist.append(customercomp)



 try:
     options = int(options)
    
 except ValueError:
     print("Lutfen secili harflerden birini giriniz!")

 except:
     print(services.unkownmis)
     

 
 if options == 1:
     print("Kupon olusturma kismina hosgeldiniz. Bu bolumden elde edeceginiz kupon ile birlikte \n sonraki alisverisinizde %20 indirim saglayabilirsiniz! Unutmayin, kuponu kullanabilmeniz icin size verilen gizlilik kodunu da bize ulastirmaniz gerekmektedir. \n Gizlilik kodunu instagram uzerinden !gizlilik kodu yazarak alabilirsiniz. \n Her kupon kodu yalnizca bir sefer kullanilabilir. \n Alisverisiniz icin tesekkur ederiz.\n")
     print(services.passing)
     time.sleep(2)
     copname = input("Lutfen isminizi giriniz: \n")
     copsurname = input("Lutfen soy isminizi giriniz \n")
     copphone = int(input("Lutfen siparis verirken kullandiginiz telefon numaranizi giriniz."))
     copmail = input("Lutfen instagram kullanici adinizi giriniz. \n")
     print(services.verify)
     time.sleep(3)
     print(data)
     print("Kodunuzu basariyla aldiniz. Kontrollerden sonra instagram sayfasi uzerinden gecerli bir sekilde siparis verebilirsiniz. Tesekkur ederiz.")


     



    

 elif options == 2:
    personbook = {"elif123abfe" : "145 789 964","salim54cfa4": "544 398 234","ilyas9cef1e" : "789 943 366","eda94f8xc13" : "599 346 104", "sezen4ye78" : "103 313 875"}
    person = input("9 haneli kuponunuzu ogrenmek icin lutfen adinizla birlikte size verilen gizlilik kodunu bosluksuz giriniz. \n")
    if person in personbook:
      result = "{} adlı gizlilik kodu sahibinin kupon kodu: {}"
      print(result.format(person, personbook[person]))
    else:
     print("Aradığınız gizlilik koduna ait kupon bulunmamaktadir. Lutfen tekrar deneyiniz.")
     break

    



 elif options == 3:

    name = input("Musteri hizmetlerine hosgeldiniz,lutfen isminizi giriniz:")
    surname = input("Lutfen soyadinizi giriniz:")
    place = input("Alisverisinizi nereden yaptiniz? Lutfen seceneklerden birini seciniz:\n  1-Instagram \n 2-Website \n 3-Trendyol \n")

    if (place == "1"):
        instachose = input("Instagram uzerinden yapılan alisverislere sosyal platform uzerinden donus yapilmaktadir. Lutfen herhangi bir sorunla karsilastiginizda rekeycaps adresine DM uzerinden ulasiniz. Hala bir sorunla karsilasiyorsaniz lutfen 1'i, sistemden cikis yapmak istiyorsaniz 2'yi tuslayiniz.")
        if instachose == ("1"):
            print(services.passing)
            time.sleep(5)
            instausername = input("Lutfen instagram kullanici adinizi giriniz")
            print("Instagram uzerinden en kisa surede adiniza donus yapilacaktir.")
            break
        
        elif instachose == ("2"):
            print(services.goodday)
            break

    
    elif place == ("2"):
        webchose = input("Hicbir araciya gerek kalmadan websitesi uzerinden bize ulastiginiz icin tesekkur ederiz. Size telefon numaraniz uzerinden ulasmamizi istiyorsanız 1'i, sistemden cikis yapmak icin ise 2'yi tuslayiniz.")
        if webchose == ("1"):
            phone = input("Lutfen telefon numaranizi basinda 0 olmadan giriniz:")
            try:
                phone = int(phone)
            except ValueError:
                print("Telefon numarasi sayilardan olusmalidir!")
                break

            print("Ilginiz icin tesekkurler, size hizlica donus yapacagiz.")
            break
            

        elif webchose == ("2"):
            print(services.logout)
            time.sleep(5)
            break

    
    elif place == ("3"):
        print("Trendyol uzerinden yapilan alisverislerle trendyol ilgilenmektedir.Lutfen kuponunuz icin trendyol uzerinden giris yapip bize ulasiniz.Ilginiz icin tesekkur ederiz.")
        uptodown = input("Devam etmek icin 1'i, cikis yapmak icin 2'yi tuslayiniz:")
        if uptodown == ("1"):
            continue
        elif uptodown == ("2"):
            break
        try:
            uptodown != 1
            uptodown != 2

        except ValueError:
            print("Lutfen yalnizca 1 veya 2 giriniz!")

        else:
            print("Yanlis tuslama yaptiniz.")
            break
            

       
 elif options == 4:
     anketlist = []

     print("Ankete katildiginiz icin cok tesekkur ederiz! Bilgilerinizi guvenli bir ortamda degerlendirme ve pazarlama icin saklayacagimizi lutfen unutmayiniz.")
     name = input("Lutfen isminizi giriniz: \n")
     anketlist.append(name)
     surname = input("Lutfen soyadinizi giriniz \n")
     anketlist.append(surname)
     seccode = input("Lutfen gizlilik kodunuzu giriniz. \n")
     complain = input("Lutfen herhangi bir puan degerlendirmesi yapmadan once sikayet ve onerilerinizi giriniz. \n")
     complaincreater(name,surname,seccode,complain)
     pointrev = str(input("Kupon uygulamasindan aldiginiz hizmet kalitesini lutfen 1'den 5'e kadar degerlendiriniz \n"))
     anketlist.append(pointrev)

     try:
         pointrev = int(pointrev)
    

     except ValueError:
         print("Degerlendirmenizi lutfen harfler yerine sayilarla yapiniz.")


     

     if pointrev == 5:
         print("Biz de sizi cok seviyoruz! Ankete katildiginiz icin tesekkurler!\n")
         break

     elif pointrev <= "4":
         print("Eksiklerimiz oldugunu dusunmeniz bizi cok uzdu. En kisa surede kapatmaya calisacagiz. Lutfen nelerden sikayetci oldugunuzu birkac cumleyle bize ozetleyiniz. Ozur dileriz..\n")
         badrev = input()
         anketlist.append[badrev]
         print("Sikayetlerinizi en kisa surede ciddi bir bicimde degerlendirecegimize lutfen emin olun. Katildiginiz icin tesekkurler, sistemden cikis yapiliyor.")
         break
    
     elif (pointrev < 1 and pointrev > 5) :
         print("Yanlis rakam girdiniz. Cikis yapiliyor.\n")
         break
        

 elif options == 5:
     calisansifre = input("Lutfen calisan sifresini giriniz: \n")
     try:
         calisansifre = int(calisansifre)

     except ValueError:
         print("Lutfen rakamlari kullanin!")
     
     print("Haftalik mesai saatleri ve gunleri degismistir!")
     jobtime = {"Aysen Yilmaz": "Carsamba Saat 12.00 - 20.00 arasi ","Kadri Ersoy":"Pazartesi 18.00 - 00.00 arasi","Caner Kordu":"Cuma 08.00-20.00 arasi","Kamile Inan":"Tam zamanli"}

     for i in jobtime.keys():
      print(i,jobtime[i],"calismaktadır. Sistem haftaya degisecektir.") 



    



          

      




    





