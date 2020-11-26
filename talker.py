#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

# Simple talker demo that published std_msgs/Strings messages
# to the 'chatter' topic

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Temperature
import time
import board
import busio
import adafruit_mpl3115a2


def talker(sensor):
    pub = rospy.Publisher('temperature', Temperature, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        temperature = sensor.temperature
        rospy.loginfo(temperature)
        pub.publish(temperature)
        rate.sleep()


if __name__ == '__main__':
    rospy.sleep(1)
    rospy.loginfo("Here")
 
    try:
        # Initialize the I2C bus.
        i2c = busio.I2C(board.SCL, board.SDA)

        # Initialize the MPL3115A2.
        sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
        # Alternatively you can specify a different I2C address for the device:
        #sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)

        # You can configure the pressure at sealevel to get better altitude estimates.
        # This value has to be looked up from your local weather forecast or meteorlogical
        # reports.  It will change day by day and even hour by hour with weather
        # changes.  Remember altitude estimation from barometric pressure is not exact!
        # Set this to a value in pascals:
        sensor.sealevel_pressure = 102250
        rospy.loginfo("Starting temperature publisher...")
        talker(sensor)
    except rospy.ROSInterruptException:
        pass
