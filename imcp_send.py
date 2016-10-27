#!/usr/bin/python

# This simple application used to send ICMP packet
# using scapy module
# Author : Muhammad Dzikri Ramdhani / kiddies
# Date : 27/Oct/2016

from scapy.all import *

def check_scapy():
    try:
        import scapy
    except ImportError:
        print "Please install scapy module"

def icmp_send(target, loop):

    packet = IP(dst=target)/ICMP()/"HELLO"
    send(packet,count=loop)

if __name__ == '__main__':
    if len(sys.argv) == 0:
       check_scapy()
    elif len(sys.argv) < 1:
       print 'icmp_send.py <target> <send_loop>'
    elif len(sys.argv) < 2:
       print 'icmp_send.py <target> <send_loop>'

    icmp_send(sys.argv[1],int(sys.argv[2]))

