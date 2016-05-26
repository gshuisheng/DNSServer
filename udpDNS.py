import sys
import SocketServer
from dnslib import *

class DNSUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        packet = self.request[0].strip()
        packet.encode('hex')

        # Parse client's request
        dnsRequest = DNSRecord.parse(packet)
        qname = dnsRequest.q.qname

        # Response
        dnsResponse = DNSRecord(DNSHeader(id=dnsRequest.header.id, qr=0, aa=1, ra=1),
                q=DNSQuestion(qname),
                a=RR(qname,rdata=A("1.2.3.4")))

        socket = self.request[1]
        socket.sendto(dnsResponse.pack(), self.client_address)

if __name__ == "__main__":
    if  len(sys.argv) < 2:
        return

    HOST = sys.argv[1]
    PORT = 53
    server = SocketServer.UDPServer((HOST, PORT), DNSUDPHandler)
    server.serve_forever()
