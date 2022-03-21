import rospy
from sensor_msgs.msg import Image
from odom_to_position.msg import Odom
from nav_msgs.msg import Odometry

ODOM_PUBLISHER = None


def callback(data):
        odom = Odom()
        odom.x = data.pose.pose.position.x
        odom.y = data.pose.pose.position.y
        odom.z = data.pose.pose.position.z
        odom.pose_x = data.pose.pose.orientation.x
        odom.pose_y = data.pose.pose.orientation.y
        odom.pose_z = data.pose.pose.orientation.z
        odom.pose_w = data.pose.pose.orientation.w
        ODOM_PUBLISHER.publish(odom)


def init_subscribers():
    rospy.Subscriber('robot/robotnik_base_control/odom', Odometry, callback)


def init_publishers():
    global ODOM_PUBLISHER
    ODOM_PUBLISHER = rospy.Publisher('/robot/robotnik_base_control/position', Odom, queue_size=10)


def init():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('odom_to_position', anonymous=True)

    init_publishers()
    init_subscribers()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

