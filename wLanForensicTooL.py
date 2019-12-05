# -*- coding: utf-8 -*-
import os
from shellParser import shellParser
from WFTBanner import banner

def print_profile_list(profiles):
  for c,profile in enumerate(profiles):
    print(str(c+1) + " : " + profile)
  print("") # back again

if __name__ == "__main__":
  banner()
  shellParser = shellParser();
  print_profile_list(shellParser.commandExecute('getProfiles'))
  selection = int(input("Select Profile : (if you want find password of all profiles only enter zero[0])"))
  banner()
  if(selection != 0):
    print("SSID     : " + shellParser.commandExecute('getProfiles')[selection-1])
    print("Password : " + "n/a\n" if len(shellParser.commandExecute('getProfilesKey',SSID=shellParser.commandExecute('getProfiles')[selection-1])) != 1 else "Password : " + shellParser.commandExecute('getProfilesKey',SSID=shellParser.commandExecute('getProfiles')[selection-1])[0] + "\n")
  else:
    for profile in shellParser.commandExecute('getProfiles'):
      print("SSID     : " + profile)
      print("Password : " + "n/a\n" if len(shellParser.commandExecute('getProfilesKey',SSID=profile)) != 1 else "Password : " + shellParser.commandExecute('getProfilesKey',SSID=profile)[0] + "\n")
