# encoding: utf-8

from datetime import datetime
import subprocess
from time import sleep


def take_picture():
    filename = datetime.now().strftime('%d.%m.%Y_%H.%M.%S')
    filename = 'photos/%s.jpg' % filename
    filename_arg =  '--filename'
    capture = '--capture-image-and-download'
    programm = 'gphoto2'
    args = [programm, capture, filename_arg, filename]
    # gphoto2 --capture-image-and-download --filename photos/1.jpg
    p = subprocess.Popen(args)

def take_series(count, delay):
    for i in range(count):
        try:
            take_picture()
            sleep(delay)
        except:
            print "Something wrong"


if __name__ == '__main__':
    take_series(100, 5)
