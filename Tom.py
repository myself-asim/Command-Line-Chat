import socket, time

HOST = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()

    conn, addr = sock.accept()

    print(f"[CONNECTING...]")
    time.sleep(1)
    print("[CONNECTED]")
    
    while True:

        TOM = input("TOM >> ")
        conn.send(TOM.encode("utf-8"))

        sock.settimeout(60.0)
        RECIEVE = conn.recv(1024)
        
        if RECIEVE.decode() == "DISCONNECT":
            print(f"[DISCONNECTED....]")
            break

        print(f"{RECIEVE.decode()}")

        # CHAT
        file = open("CL_Chat.txt", 'a')
        file.write(f"JERRY >> {RECIEVE.decode()}\n")
        file.close()

    sock.close