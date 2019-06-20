#!/usr/bin/python

# Created by: Jeremiah Roe and Bryan Taylor

import os
import requests
import json

banner = open("banner.txt", "r")
print banner.read()

# Setting the nmap command up in multiple stages to accept raw input and then tie it all together.
nm_command1 = 'nmap -p- -Pn --open -iL '
nm_command2 = ' | grep "report for" | cut -d " " -f5 > nmap_scan.txt'

#def Tool1():
#   tool 1 code here
#Tool1()

def Sonic():
  print "Type the number for the option you want, then, press 'Enter'."
  print "1. Run All Tools."
  print "2. Advanced (choose your tool)"
  answer = raw_input("==>")
  if answer == "1":
    print "Running all tools, this might take a minute... Results will be saved to a file in your current working directory."
  elif answer == "2":
    print "Choose the tool you would like to specifically get results back from."
    print "1. Nmap"
    print "2. Masscan"
    print "3. Amass"
    print "4. Metabigor?"
    print "5. AppEnum? (what I created)"
    print "6. Etc..."
    answer = raw_input("==>")
    if answer == "1":
      print "Please enter filename for hosts to scan."
      nm_answer = raw_input("==>")
      print "Scanning hosts listed in file... This may take a minute."
      #Tool1(nm_answer)
      nm = nm_command1 + nm_answer + nm_command2 #Combining all seperate nmap pieces into one variable
      os.system(nm)
    elif answer == "2":
      print "this needs to be coded"
      #Tool2()
    elif answer == "3":
      print "This needs to be coded"
      #Tool3()
    elif answer == "4":
      print "This needs to be coded"
      #Tool4()
    elif answer == "5":
      print "This needs to be coded"
      #Tool5()
    elif answer == "6":
      print "This needs to be coded"
      #Tool6()
Sonic()
