import socket
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad

# TripleDES Anahtarı (Hocanın verdiği anahtar)
KEY = b'Sixteen byte key'  # 16 bayt uzunluğunda olmalı

# Sunucuya bağlan
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))  # Sunucu IP ve Port

# Kullanıcıdan mesaj al
message = input("Gönderilecek mesaj: ").encode()

# TripleDES Şifreleyici oluştur
cipher = DES3.new(KEY, DES3.MODE_ECB)
ciphertext = cipher.encrypt(pad(message, DES3.block_size))

# Şifreli mesajı sunucuya gönder
client_socket.send(ciphertext)

print("Mesaj gönderildi!")

# Bağlantıyı kapat
client_socket.close()
