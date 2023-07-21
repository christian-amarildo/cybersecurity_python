from socket import *

def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('[+] %s/tcp open' % tgtPort)
        connskt.close()
    except:
        print('[-] %s/tcp closed' % tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Cannot resolve %s ' % tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan result of: %s ' % tgtName[0])
    except:
        print('\n[+] Scan result of: %s ' % tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning Port: %d' % tgtPort)
        conScan(tgtHost, int(tgtPort))

if __name__ == '__main__':
    # Faz uma conexão ao endereço IP "216.58.207.238" na porta 80
    conScan('216.58.207.238', 80)
    
    # Escaneia o endereço "google.com" nas portas 80 e 22
    portScan('google.com', [80, 22])

