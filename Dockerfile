From ubuntu:latest
RUN apt-get -y update && apt-get install -y python2.7 
RUN apt-get install -y curl && curl https://bootstrap.pypa.io/get-pip.py > /home/get-pip.py
RUN python /home/get-pip.py 
RUN pip install dnslib 
RUN apt-get install -y git
RUN cd /home && git clone https://github.com/gshuisheng/DNSServer.git 
CMD python udpDNS.py 192.168.31.116
