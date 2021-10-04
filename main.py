# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 01:41:53 2021

@author: gaspa
"""

import selenium
from selenium import webdriver
import keyboard
from time import sleep,monotonic

USERNAME = "JeVousBez"
bullying_offset = 1

driver = webdriver.Chrome()
driver.get("https://trex-runner.com/")

# Getting best_score
rows = driver.find_elements_by_xpath("//*[@id='records']/tbody/tr")
to_unpack = rows[0].text
lsi = 0 #Last space index
for i in range(len(to_unpack)):
    if to_unpack[i] == " ":
        lsi = i
best_score = int(to_unpack[lsi:])
print("Score to beat : {}".format(best_score))
# Setting username
driver.find_element_by_id("user").click()
sleep(1)
keyboard.write(USERNAME)
sleep(0.5)
keyboard.press_and_release('enter')
sleep(1)
# Executing invincibility script
driver.execute_script("Runner.instance_.gameOver = () => {}")
# Starting the game
keyboard.press_and_release("space")
# Wait till best score beaten
current_score = 0
while best_score*bullying_offset>=current_score:
    nf_score = driver.execute_script("return Runner.instance_.distanceRan")
    current_score = round(nf_score * 0.025)
t0 = monotonic()
# Restore death
driver.execute_script("Runner.instance_.gameOver = Runner.prototype.gameOver")
# Make sure we have the right score
while monotonic()<t0+1:
    driver.execute_script("Runner.instance_.distanceRan = {}".format(current_score/0.025))

print("CyberBullying complete !")

    
    

