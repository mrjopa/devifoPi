import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)


count = 0
while (count < 3):
   print 'The count is:', count
   count = count + 1
   GPIO.output(14, True)
   print "Start : %s" % time.ctime()
   time.sleep(2)
   GPIO.output(14, False)
   time.sleep(2)
   print "End : %s" % time.ctime()

GPIO.cleanup()

print "Good bye!"
print "========="