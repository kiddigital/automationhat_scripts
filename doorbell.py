#!/usr/bin/env python

import time

import automationhat

automationhat.input.three.resistor(automationhat.PULL_DOWN)

if automationhat.is_automation_hat():
    automationhat.light.power.write(1)

while True:
    if(automationhat.input.three.is_on()):
        print("Bell pressed!")
    time.sleep(0.2)
