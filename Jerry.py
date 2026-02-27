import socket, time

HOST = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    print(f"[CONNECTING...]")
    time.sleep(1)
    print(f"[CONNECTED....]")

    while True:
        
        sock.settimeout(60.0)
        RECIEVE = sock.recv(1024)

        if RECIEVE.decode() == "DISCONNECT":
            print(f"[DISCONNECTED....]")
            break

        print(f"TOM: {RECIEVE.decode()}")
        JERRY = input("JERRY >> ")
        
        # CHAT
        file = open("CL_Chat.txt", 'a')
        file.write(f"TOM >> {RECIEVE}\n")
        file.close()

        sock.send(JERRY.encode("utf-8"))

    sock.close()