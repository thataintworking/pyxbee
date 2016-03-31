# coding=utf-8
# Created by Ron Smith @ That Ain't Working


from xbee import ZigBee, BROADCAST_LONG_ADDR, BROADCAST_SHORT_ADDR
from serial import Serial
from examples.config import XBEE_PORT

with Serial(XBEE_PORT, 9600) as srl:
    zb = ZigBee(srl)
    zb.send('tx', data=b'Hello ZigBee!', dest_addr_long=BROADCAST_LONG_ADDR, dest_addr=BROADCAST_SHORT_ADDR)

    # TODO why doesn't the function below work when the function above does?
    #zb.tx(BROADCAST_LONG_ADDR, BROADCAST_SHORT_ADDR, b'Hello ZigBee!')

