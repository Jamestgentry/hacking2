from bottle import route, run, template, request
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
CONTROL_PIN = 18

@route('/') 
def index():
    return template('home.tpl')
    
@route('/on')
def index():
    GPIO.setup(CONTROL_PIN, GPIO.OUT)
    GPIO.output(CONTROL_PIN, False) 
    return template('home.tpl')
    
@route('/off')
def index():
    GPIO.setup(CONTROL_PIN, GPIO.IN)
    return template('home.tpl')    
        

try: 
    run(host='0.0.0.0', port=80)
finally:  
    print('Cleaning up GPIO')
    GPIO.cleanup()
