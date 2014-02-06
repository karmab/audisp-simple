#!/usr/bin/env python

"""
parse audit events and sends them to syslog after changing uid to username
"""

__author__ = "Karim Boumedhel"                                                                                                                                 
__credits__ = ["Karim Boumedhel"]                                                                                                                              
__license__ = "GPL"                                                                                                                                            
__version__ = "1.0"
__maintainer__ = "Karim Boumedhel"
__email__ = "karimboumedhel@redhat.com"
__status__ = "Production"

import os
import signal
import sys
import auparse
import syslog
import simplejson as json


stop = 0
hup = 0
au = None

def term_handler(sig, msg):
        global stop 
        print 'received a term event'
        stop = 1
        sys.exit(0)                                                                                                                                           
                                                                                                                                                              
def hup_handler(sig, msg):
        global hup
        print 'received a hup event'
        hup = 1

def reload_config():
        global hup
        hup = 0

def none_to_null(s):
    'used so output matches C version'
    if s is None:
        return '(null)'
    else:
        return s

signal.signal(signal.SIGHUP, hup_handler)
signal.signal(signal.SIGTERM, term_handler)

programname = os.path.basename(sys.argv[0])

def coolparse(au):
    global serial
    global serials 
    global formatted
    result = {}
    event_cnt = 1
    au.reset()
    while True:
        if not au.first_record():
            sys.exit(1)

        record_cnt = 1
        while True:
            event = au.get_timestamp()
            serial = event.serial
            if event is None:
                print "Error getting timestamp - aborting"
                sys.exit(1)

            au.first_field()
            while True:
                result[au.get_field_name()] = au.interpret_field()
                if not au.next_field(): break
            record_cnt += 1
            if not au.next_record(): break
        event_cnt += 1
        if not serial in serials and len(serials) >0:
                syslog.openlog(programname)
                syslog.syslog(syslog.LOG_NOTICE, json.dumps(formatted) )
		formatted = {}
                serials.append(serial)
		formatted['serial'] = serial
		formatted['events'] = [result]
        else:
                if len(serials) == 0:
                        serials.append(serial)
			formatted['serial'] = serial
			formatted['events'] = [result]
		else:
			formatted['events'].append(result)
        if not au.parse_next_event(): break

def main():
        global serials 
        global stop
        global hup
	global formatted
        serials = []
	formatted = {}
        while stop == 0:
                try:
                        buf=sys.stdin
                        if hup == 1 :
                                reload_config()
                                continue
                        for line in buf:
                                au = auparse.AuParser(auparse.AUSOURCE_BUFFER, line)
                                coolparse(au)
                except IOError, e:
                        continue

if  __name__ =='__main__':
        main()
