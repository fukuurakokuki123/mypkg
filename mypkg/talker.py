import rclpy
from rclpy.node import Node
from person_msgs.msg import Person
from std_msgs.msg import Int16 

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)
n = 0

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Int16, "countup" , 10)
        self.n = 0
        self.create_timer(0.5,self.cb)
    

def cb():
    global n
    msg = Person()
    msg.name = "福浦功己"
    msg.age = n
    pub.publish(msg)
    n += 1
    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1


def main():
    node.create_timer(0.5, cb)
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
