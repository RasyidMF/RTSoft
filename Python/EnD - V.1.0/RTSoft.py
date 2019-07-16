
# RTSoft Team
# Created by : RasyidMF
# Language used : Python 3.7
# Released : 17/7/2019 01:46 (WITA [Waktu Indonesia Tengah])

# Project name : "Encrypt & Decrypt Your password" using Odd & Even
# Description :
#	This source code was free to used, also increase your knowledge about securing passwords
#	Please credits dont remove it :D
#	Any question or suggestion contact me on this below
#	Facebook	: https://www.facebook.com/RasyidMF
#	Instagram	: https://www.instagram.com/kochengs.oren
#	Youtube		: "RasyidMF GT"
#	GitHub		: https://github.com/RasyidMF
#	Email		: rasyidmfgt@gmail.com
#	
#
#	Atleast we ever try rather than we never try it

# How to use (Command Line)
#	1. Open CMD
#	2. Directed to the folder which one you save this file
#	3. Type :
#		(Encrypt) [ThisFileName].py -enc "yourtextinhere"
#		(Decrypt) [ThisFileName].py -dec "yourencryptedhere"
#	4. Result will be print on Console

# Change Hashing Password
#	Its "ONLY" will effected on Decrypt

import random
import sys

# Edit this hashing password for Encrypt & Decrypt
ev = "*" # 1 Character only
od = " " # 1 Character only
# Dont duplicated which one same character it will broke the encrypted! also hard to decrypt

def _Check(num):
	if (num % 2) == 0: return "e"
	else: return "o"
def Encrypt(Character, Fix):
	res = ""
	for i in range(len(Character)):
		isDone = False
		chr = ord(Character[i])
		r = ""
		while True:
			if chr == 1: break
			t = chr
			if (_Check(t)) == "e":
				r += ev
				chr = chr / 2
			elif (_Check(t)) == "o":
				r += od
				chr = chr + 1
		if Fix == True: res += r + "\\n"
		else: res += r + "\n"
	return res
def Decrypt(Encrypted, Fix):
	res = ""
	max = len(Encrypted.split('\n')) - 1
	enc = Encrypted.split('\n')
	if Fix == True: 
		max = len(Encrypted.split("\\n")) - 1
		enc = Encrypted.split("\\n")
	for i in range(max):
		co = enc[i]
		nm = 1
		for a in range(len(co)):
			if co[(len(co) - 1) - a] == ev:
				nm = nm * 2
			elif co[(len(co) - 1) - a] == od:
				nm = nm - 1
		res += chr(nm)
	return res
def isOnCmd():
	if len(sys.argv) > 1:
		if len(sys.argv) < 3: 
			print("Unknown arguments! Exited") 
			exit()
		ar1 = sys.argv[1]
		ar2 = sys.argv[2]
		if ar1 == "-enc":
			print("\nEncrypted : \n")
			print(Encrypt(ar2, True))
			print("\nEncrypted (Without \\n) : \n")
			print(Encrypt(ar2, False))

		elif ar1 == "-dec":
			print("\nDecrypted : \n")
			print("-> " + Decrypt(ar2, True))
		else: print("Unknown arguments! Exited")
		exit()
		

isOnCmd()

print("See this star :O")
print("Well its not the star :P its only the Encrypt Password\n")
print("############### ~ RasyidMF - CEO RTSoft ~ ###############\n")

print("Command line Properties :\n-> (Encrypt) [ThisFileName].py -enc \"yourtextinhere\"\n-> (Decrypt) [ThisFileName].py -dec \"yourencryptedhere\"")

print("\nFirst character using : \"" + ev + "\"")
print("Second character using : \"" + od + "\"\n\n")

print("Encrypted Text :")
print(Encrypt("RasyidMF", False))
print("Encrypted Text (With \\n) [For Decrypt] :")
print(Encrypt("RasyidMF", True))

print("\nDecrypted Text :")
print(Decrypt("* * * ** **\n * * * * ***\n ** * ****\n * * *****\n * * ** ***\n** * * ***\n * *** * **\n* ** * * **\n", False))

print("\n")