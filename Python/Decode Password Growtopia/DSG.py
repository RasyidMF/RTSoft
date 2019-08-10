# RTSoft Team
# Created by : RasyidMF
# Language used : Python 3.7
# Released : 24/7/2019 11:51 (WITA [Waktu Indonesia Tengah])

# Project name : Growtopia Save.dat Decoder
# Description :
#	This source code was free to used, also increase your knowledge about decoding a encrypted file
#	Please credits dont remove it :D
#	Any question or suggestion contact me on this below
#	Facebook	: https://www.facebook.com/RasyidMF
#	Instagram	: https://www.instagram.com/kochengs.oren
#	Youtube		: "RasyidMF GT"
#	GitHub		: https://github.com/RasyidMF
#	Email		: rasyidmfgt@gmail.com
#	Blog		: https://www.rtsoft.home.blog/
#	
#	Atleast we ever try rather than we never try it

# Re-copy our source code rules :
#	Input our Team / Creator on your source code
#	Atleast 2-4 Credits on your Re-copy code
#	We accepted if you using Credits as Link Source / Credits / Our Website / Creator Facebook
#	Also if you a developer, dont break the rule :)
#	Enjoy ::::>>>>
from colorama import init
from colorama import Fore, Back, Style
import sys
import io
import time

attr = ["tankid_name", "tankid_password", "lastworld"]
def read(FileLoc):
	try:
		if "\"" in FileLoc:
			FileLoc = FileLoc.replace("\"", "")
		f = io.open(FileLoc, errors='ignore')
		x = ""
		for o in f.readlines():
			x += o
		f.close()
		return x
	except (OSError, IOError) as ex:
		_p("{w}~ {r}Can't read file, probly File not found! Try again{w} Ex :{y} %s {w}~" % ex)
		return ""
def getData(Content, Name):
	try:
		c = Content.split(Name)
		m = c[1][0]
		r = ""
		for x in range(ord(m)):
			r += c[1][4 + x]
		return r
	except:
		_p("{w}~ {r}Getting %s failed, Invalid file ?{w} Please input Growtopia Save dat! ~" % Name)
		return ""
def verfchr(c):
	if c >= 48 and c <= 57 or c >= 65 and c <= 90 or c >= 97 and c <= 122 or c >= 43 and c <= 46 or c == 64 or c == 95 or c == 35 or c == 123 or c == 125:
		return True
	else: return False
def decodePass(passwd, maxbrute):
	for x in range(maxbrute):
		isOk = True
		pwd = ""		
		for w in range(len(passwd)):		
			_p("{bgm}{w}PROCESS{bgb} {g}" + str(x) + "{w} -> {w}" + pwd + "\r", True)
			sys.stdout.flush()

			trgt = ord(passwd[w])

			if trgt >= 1024:
				tmp = trgt
				while True:
					if tmp >= 1 and tmp <= 255:
						trgt = tmp
						break					
					tmp = (int(tmp / 2))
			c = trgt - w + x
			if verfchr(c):
				pwd += chr(c)
			else: 
				c = trgt - x + w
				if verfchr(c):
					pwd += chr(c)
				else:
					c = trgt - x - w
					if verfchr(c):
						pwd += chr(c)
					else:						
						isOk = False
		
		sys.stdout.flush()
				
		if isOk == True:			
			_p("{bgg}{w}S{bgb} -> {g}" + pwd + "{w}               ")
		else:
			if len(pwd) >= (len(passwd) / 2) and len(pwd) >= 3:
				if len(pwd) != (len(passwd)):
					while True:
						if len(pwd) != (len(passwd)):
							pwd += " "
						else: break
				_p("{bgr}{w}T{bgb} -> {y}" + pwd + "{w}               ")
def sig(string):
	r = ""
	for x in string:
		if ord(x) >= 255:
			_p("{w}~{r} We founded encoded Password was founded as Unknown ASCII Code, its kinda hard to Decode {y}Value : %s {w}({g}%s{w}){w} ~" % (ord(x), hex(ord(x))))
		r += "\\" + str(hex(ord(x)))
	return r
def _p(text, stdout = False):
	text = text.replace("{b}", "\033[30m")
	text = text.replace("{r}", "\033[31m")
	text = text.replace("{g}", "\033[32m")
	text = text.replace("{y}", "\033[33m")
	text = text.replace("{bl}", "\033[34m")
	text = text.replace("{m}", "\033[35m")
	text = text.replace("{c}", "\033[36m")
	text = text.replace("{w}", "\033[37m")
	text = text.replace("{rs}", "\033[39m")
	text = text.replace("{bgb}", "\033[40m")
	text = text.replace("{bgr}", "\033[41m")
	text = text.replace("{bgg}", "\033[42m")
	text = text.replace("{bgy}", "\033[43m")
	text = text.replace("{bgbl}", "\033[44m")
	text = text.replace("{bgm}", "\033[45m")
	text = text.replace("{bgc}", "\033[46m")
	text = text.replace("{bgw}", "\033[47m")
	if stdout == True:
		sys.stdout.write(text)
	else: print(text)


# Main
init()

_p("")
_p("~ Growtopia Save.dat Decoder {y}Python{w} by : {g}RTSoft V.1.0{w} ~")
_p("~ Created by : {g}RasyidMF{w} ~")
_p("~ Released at {g}24/07/2019{w} ~")
_p("~ Visit our blogger : {g}https://www.rtsoft.home.blog/{w} ~")
_p("~ Visit our GitHub : {g}https://www.github.com/RasyidMF/RTSoft{w} ~")
_p("\n{bgb}{b}#######{bgr}{r}######################{bgw}{w}######################{bgb}{b}#")
_p("{bgb}{b}#######{bgr}{r}######################{bgw}{w}######################{bgb}{b}#")
_p("{bgb}{b}#######{bgr}{r}######################{bgw}{w}######################{bgb}{b}#")
_p("{bgb}{b}#######{bgr}{r}######################{bgw}{w}######################{bgb}{b}#")
_p("{bgb}{b}#######{bgr}{r}######################{bgw}{w}######################{bgb}{b}#")
_p("{bgb}{b}#######{bgr}{r}######################{bgw}{w}######################{bgb}{b}#")
_p("{bgb}{b}#######{bgr}{r}######################{bgw}{w}######################{bgb}{b}#")
_p("")
_p("{bgb}{b}######################{bgr}{bgb}{w}RTSoft Team")


_p("")

_p("{bgr}{w}T{bgb} -> {w} Mean this password length was not equals on the file save.dat")
_p("{bgg}{w}S{bgb} -> {w} Mean this password length was equals on the file save.dat")

_p("")

alwaysYes = False
while True:
	_p("Enter your save.dat file :{g}")
	f = raw_input()
	mySD = read(f)
	if mySD != "":
		mySD = mySD.replace("tankid_password_chk2", "")
		_p("{r}######################{w}######################{bgb}")
		_p("Enter maximum bruteforce {g}Recommended (255){w} : {g}")

		m = input()
		if m == "":
			_p("~ {r}You must input the maximum {w}~")					
		else:
			growID		= getData(mySD, attr[0])
			lastWorld	= getData(mySD, attr[2])
			passwd		= getData(mySD, attr[1])
			_p("{r}######################{w}######################{bgb}")

			if growID != "" or lastWorld != "" or passwd != "":		
				_p("GrowID : {g}%s{w} ({y}%s{w})" % (growID, sig(growID)))
				_p("Last World : {g}%s{w} ({y}%s{w})" % (lastWorld, sig(lastWorld)))
				_p("Password (Encode) : {y}%s{w}" % sig(passwd))
				_p("Password (Bruteforce) :")
				decodePass(passwd, int(m))

			_p("{r}######################{w}######################{bgb}")

			if alwaysYes == False:
				_p("Are you want to try decode again ? {g}Yes/No/Always Yes {w}:{y}")
				o = raw_input()
				if o == "":
					break
				elif o == "Always Yes":
					alwaysYes = True
					_p("{r}######################{w}######################{bgb}")
				elif o == "No" or o == "no": 
					_p("~ {r}Okay byee{w} ~")
					break		
				else: _p("{r}######################{w}######################{bgb}")