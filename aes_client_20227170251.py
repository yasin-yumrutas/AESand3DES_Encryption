import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# AES Anahtarı (Hocanın verdiği anahtar)
KEY = b'Sixteen byte key'  # 16 bayt uzunluğunda olmalı

# Sunucuya bağlan
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 54321))  # Sunucu IP ve Port

# Kullanıcıdan mesaj al
message = input("Gönderilecek mesaj: ").encode()

# AES Şifreleyici oluştur
cipher = AES.new(KEY, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(message, AES.block_size))

# Şifreli mesajı sunucuya gönder
client_socket.send(ciphertext)

print("Mesaj gönderildi!")

# Bağlantıyı kapat
client_socket.close()
