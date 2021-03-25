import sys
import nmap


target = str(sys.argv[1])
ports = [80,21,443]

scan = nmap.PortScanner()


print("\n Scanning",target,"for the Ports")

for port in ports:
    portscan = scan.scan(target,str(port))
    print("Port",port,"is",scan['scan'][target]['tcp'][port]['state'])


