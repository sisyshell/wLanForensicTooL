# -*- coding: utf-8 -*-
import os

def banner():
  os.system("cls");
  print("          _        _______  _              _______  _______  _______  _______  _        _______ _________ _______ ")
  print("|\\     /|( \\      (  ___  )( (    /|      (  ____ \\(  ___  )(  ____ )(  ____ \\( (    /|(  ____ \\\\__   __/(  ____ \\")
  print("| )   ( || (      | (   ) ||  \\  ( |      | (    \\/| (   ) || (    )|| (    \\/|  \\  ( || (    \\/   ) (   | (    \\/")
  print("| | _ | || |      | (___) ||   \\ | |      | (__    | |   | || (____)|| (__    |   \\ | || (_____    | |   | |      ")
  print("| |( )| || |      |  ___  || (\\ \\) |      |  __)   | |   | ||     __)|  __)   | (\\ \\) |(_____  )   | |   | |      ")
  print("| || || || |      | (   ) || | \\   |      | (      | |   | || (\\ (   | (      | | \\   |      ) |   | |   | |      ")
  print("| () () || (____/\\| )   ( || )  \\  |      | )      | (___) || ) \\ \\__| (____/\\| )  \\  |/\\____) |___) (___| (____/\\")
  print("(_______)(_______/|/     \\||/    )_)      |/       (_______)|/   \\__/(_______/|/    )_)\\_______)\\_______/(_______/")
  print("")
  print("===================================================================================================================")
  print("")

def getProfiles():
  profiles = []
  for profile in os.popen('netsh wlan show profiles').read().split("\n"):
    profiles.append(profile.split(': ')[1]) if profile.find(': ') != -1 else ''
  return profiles
	
def print_profile_list(profiles):
  for c,profile in enumerate(profiles):
    print(str(c+1) + " : " + profile)
  print("")

def get_password(SSID):
  command_result = os.popen("netsh wlan show profiles name="+SSID+" key=clear").read()
  if(command_result.find("Security key           : Present") != -1):
    for key in command_result.split("\n"):
	  if(key.find("Key Content") != -1):
	    print("SSID     : " + SSID)
	    print("Password : " + key.split(': ')[1] + "\n")
  else:
	  print("SSID     : " + SSID)
	  print("Password : n/a\n")

if __name__ == "__main__":
  banner()
  print_profile_list(getProfiles())
  selection = int(input("Select Profile : (if you find all profiles password only enter zero(0))"))
  banner()
  if(selection != 0):
    get_password(getProfiles()[selection-1])
  else:
    for profile in getProfiles():
	  get_password(profile)