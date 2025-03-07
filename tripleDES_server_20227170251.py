import socket
from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

# TripleDES Anahtarı (Hocanın verdiği anahtarı kullan)
KEY = b'Sixteen byte key'  # 16 bayt uzunluğunda olmalı

# Sunucu bağlantısını oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # Sunucu IP ve Port
server_socket.listen(1)

print("Sunucu çalışıyor... Bağlantı bekleniyor...")

# İstemciden bağlantıyı kabul et
conn, addr = server_socket.accept()
print(f"Bağlantı kabul edildi: {addr}")

# Şifreli mesajı al
ciphertext = conn.recv(1024)

# TripleDES Çözücü oluştur
cipher = DES3.new(KEY, DES3.MODE_ECB)
plaintext = unpad(cipher.decrypt(ciphertext), DES3.block_size)

print(f"Gelen mesaj: {plaintext.decode()}")

# Bağlantıyı kapat
conn.close()
server_socket.close()
