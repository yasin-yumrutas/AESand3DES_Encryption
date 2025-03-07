  AES & 3DES Şifreleme ile Client-Server İletişimi
Bu proje, AES (Advanced Encryption Standard) ve 3DES (Triple Data Encryption Standard) kullanarak şifreli bir istemci-sunucu (client-server) haberleşmesi gerçekleştirmek için geliştirilmiştir.

  Proje Hedefleri
  AES ve 3DES şifreleme algoritmalarını kullanarak güvenli mesaj iletimi sağlamak.
  TCP/IP tabanlı istemci-sunucu haberleşmesini gerçekleştirmek.
  İstemci tarafında mesajın şifrelenmesi, sunucu tarafında çözülmesini sağlamak.
  Şifreleme yöntemlerini uygulayarak veri güvenliğini artırmak.

  Proje Yapısı
Bu proje, AES ve 3DES şifreleme yöntemlerini ayrı ayrı test edebilmek için dört Python dosyasından oluşmaktadır:

|-- AES_client.py        # AES kullanarak istemci tarafında şifreleme yapar
|-- AES_server.py        # AES kullanarak sunucu tarafında şifre çözme işlemi yapar
|-- tripleDES_client.py  # 3DES kullanarak istemci tarafında şifreleme yapar
|-- tripleDES_server.py  # 3DES kullanarak sunucu tarafında şifre çözme işlemi yapar


  Gereksinimler
Bu projeyi çalıştırmadan önce aşağıdaki adımları takip edin:

1   Python 3.x yüklü olmalıdır.
2️   Gerekli kütüphanelerin yüklenmesi gerekmektedir.

Gerekli paketleri yüklemek için terminale şu komutu yazın:

sudo apt install python3-pycryptodome -y

Yüklemenin başarılı olup olmadığını kontrol etmek için:

python3 -c 'import Crypto; print("PyCryptodome başarıyla yüklendi!")'

Başarılı bir kurulum şu çıktıyı verecektir:

PyCryptodome başarıyla yüklendi!



  Projenin Çalıştırılması
Bu projede AES ve 3DES şifreleme yöntemleri ayrı dosyalarda çalıştırılmaktadır.
Öncelikle sunucu başlatılmalı, ardından istemci çalıştırılmalıdır.

1️  AES ile Şifrelenmiş Haberleşme
AES (Advanced Encryption Standard), simetrik anahtar şifreleme yöntemlerinden biridir.
AES ile şifreleme istemci tarafında yapılır, deşifreleme ise sunucu tarafından gerçekleştirilir.

  AES İstemci (Client) Çalıştırma
İstemci (client), kullanıcının girdiği mesajı AES algoritması ile şifreleyerek sunucuya gönderir.

python3 AES_client.py

İstemci çalıştırıldığında şu şekilde mesaj girişi yapabilirsiniz:

Göndermek istediğiniz mesaj: Merhaba Dünya!

Bu mesaj AES ile şifrelenerek sunucuya iletilir.


   AES Sunucu (Server) Çalıştırma
Sunucu (server), istemciden gelen şifreli mesajı çözer ve ekrana yazdırır.

python3 AES_server.py

Sunucu ekranında şu gibi bir çıktı alınır:

Bağlantı kabul edildi: ('127.0.0.1', 54321)
Çözülen Mesaj: Merhaba Dünya!






  2️  3DES ile Şifrelenmiş Haberleşme
3DES (Triple Data Encryption Standard), klasik DES algoritmasının geliştirilmiş bir versiyonudur.
AES ile benzer şekilde çalışır, ancak üç aşamada şifreleme yapar.

  3DES İstemci (Client) Çalıştırma

python3 tripleDES_client.py

İstemci mesaj girişi yapar:

Göndermek istediğiniz mesaj: Şifreli İletişim Testi!



Bu mesaj 3DES ile şifrelenerek sunucuya gönderilir.

  3DES Sunucu (Server) Çalıştırma

python3 tripleDES_server.py

Sunucu ekranında şu çıktı görüntülenir:

Bağlantı kabul edildi: ('127.0.0.1', 65432)
Çözülen Mesaj: Şifreli İletişim Testi!





  Çalışma Prensibi (Adım Adım)
1️ Sunucu dosyası başlatılır ve istemciden gelecek mesaj beklenir.
2️ İstemci dosyası başlatılır ve kullanıcıdan mesaj alınır.
3️ Mesaj, AES veya 3DES ile şifrelenir.
4️ Şifreli mesaj TCP/IP ile sunucuya gönderilir.
5️ Sunucu şifreli mesajı alır ve AES/3DES algoritması ile çözer.
6️ Şifre çözülerek düz metin halinde ekrana yazdırılır.