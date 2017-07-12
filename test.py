import os
import glob
import cv2
import cv
import datetime
import base64
import requests
import urllib2
import httplib
import time
import sys
import subprocess

#===================================================Update FW Version================================

vercurrent = subprocess.check_output('git rev-parse --verify HEAD', shell=True)
print 'Cur ver ' + vercurrent

vergit =  subprocess.check_output('git ls-remote https://github.com/izemkung/gps_softbiz | head -1 | cut -f 1', shell=True)
print 'Git ver '+ vergit
if vergit == vercurrent :
    print "version FW Ok!!!"
if vergit != vercurrent and len(vercurrent) == len(vergit):
    print "Download FW "
if vergit == vercurrent and len(vercurrent) == len(vergit):
    print "version FW Ok!!! and len ok"


