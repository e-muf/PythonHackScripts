#!/usr/bin/env python

# Remote computer
# iptables -I FORWARD -j NFQUEUE --queue-num 0
# The number 0 in the previus command is the number of the queue

# My computer
# iptables -I OUTPUT -j NFQUEUE --queue-num 0
# iptables -I INPUT -j NFQUEUE --queue-num 0

# iptables --flush -> Delete the before iptables definition.

import netfilterqueue

def process_packet(packet):
    print(packet)
    # packet.accept() Accept the packets and forward to the client
    # packet.drop() Do not forward the packets, so the client don't have internet.

queue = netfilterqueue.NetfilterQueue()
# The function bind() parameters are the numberof the queue and a callback function
queue.bind(0, process_packet)
queue.run()
