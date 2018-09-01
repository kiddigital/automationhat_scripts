#!/usr/bin/env python3

import time

import automationhat

x = 0
bel = False

if automationhat.is_automation_hat():
    automationhat.light.power.write(1)
    automationhat.analog.three.auto_light(False)

while True:
    if automationhat.analog.three.read() > 4.8:
        time.sleep(0.15)
        if automationhat.analog.three.read() > 4.8:
            automationhat.analog.three.light.on()
            time.sleep(0.15)
            if automationhat.analog.three.read() > 4.8:
                print(str(x) + ' Bell!')
                bel = True
            else:
                automationhat.analog.three.light.off()
    else:
        if bel:
            bel = False
            automationhat.analog.three.light.off()
            print(str(x) + ' Bell released!')
    time.sleep(0.2)
    #print(x)
    x = x + 1
