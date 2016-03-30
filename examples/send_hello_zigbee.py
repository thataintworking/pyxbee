# coding=utf-8
# Created by Ron Smith @ That Ain't Working


from xbee import ZigBee
from serial import Serial
from examples.config import XBEE_PORT, ZIGBEE_BROADCAST_LONG_ADDR, ZIGBEE_BROADCAST_SHORT_ADDR

with Serial(XBEE_PORT, 9600) as srl:
    zb = ZigBee(srl)
    zb.send('tx', data='Hello ZigBee!', dest_addr_long=ZIGBEE_BROADCAST_LONG_ADDR, dest_addr=ZIGBEE_BROADCAST_SHORT_ADDR)

