import socket
import threading

def scan_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, port))
        print(f"[+] Port {port} is open")
        s.close()
    except:
        pass

def main():
    target = input("Target IP: ")
    ports = range(1, 1025)
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()

if __name__ == "__main__":
    main()
  
