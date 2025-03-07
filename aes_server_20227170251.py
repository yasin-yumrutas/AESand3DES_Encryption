import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# AES Anahtarı (Hocanın verdiği anahtar)
KEY = b'Sixteen byte key'  # 16 bayt uzunluğunda olmalı

# Sunucu bağlantısını oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 54321))  # Sunucu IP ve Port
server_socket.listen(1)

print("AES Sunucu çalışıyor... Bağlantı bekleniyor...")

# İstemciden bağlantıyı kabul et
conn, addr = server_socket.accept()
print(f"Bağlantı kabul edildi: {addr}")

# Şifreli mesajı al
ciphertext = conn.recv(1024)

# AES Çözücü oluştur
cipher = AES.new(KEY, AES.MODE_ECB)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print(f"Gelen mesaj: {plaintext.decode()}")

# Bağlantıyı kapat
conn.close()
server_socket.close()
