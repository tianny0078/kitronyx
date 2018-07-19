#!/usr/bin/env python
import rospy
import serial
import struct
from std_msgs.msg import String
from kitronyx.msg import Force

def tactileSerial():
    pub = rospy.Publisher('tactile', Force, queue_size=10)
    rospy.init_node('tactileNode', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    # open the serial
    ser = serial.Serial()
    ser.baudrate = 1497600
    ser.port = '/dev/ttyUSB0'
    ser.open()
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
	msg_send = Force()
	# read from serial
	if ser.is_open:
		ser.write(b'A')
		for i in range(160):
			x = ser.read()
			msg_send.current[i] = struct.unpack('B',x)[0]
        #rospy.loginfo(hello_str)
        pub.publish(msg_send)
        rate.sleep()

if __name__ == '__main__':
    try:
        tactileSerial()
    except rospy.ROSInterruptException:
        pass
