# 简单DNS服务器实现

## 说明

   对任意DNS请求，服务器解析返回特定地址

## 环境

  ubuntu 16.04 + python2.7 + dnslib 0.9.6

## 安装执行

1. 服务端  
  ```sh
  git clone https://github.com/gshuisheng/DNSServer.git
  cd DNSServer && sudo python udpDNS.py 192.168.31.116
  ```
2. 客户端  

  ```sh  
  nslookup example.com 192.168.31.116

  ```

## 参考
［1］ http://www.firewall.cx/networking-topics/protocols/domain-name-system-dns/160-protocols-dns-query.html
［2］https://en.wikipedia.org/wiki/Domain_Name_System
［3］https://bitbucket.org/paulc/dnslib
