CSI = '\033['
OSC = '\033]'
BEL = '\a'
#  Spectating !!!
def code_to_chars(code):
    return CSI + str(code) + 'm'
def set_title(title):
    return OSC + '2;' + title + BEL
def clear_screen(mode=2):
    return CSI + str(mode) + 'J'
def clear_line(mode=2):
    return CSI + str(mode) + 'K'
class AnsiCodes(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))
class MainColor(AnsiCodes):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39
    LIGHTBLACK_EX   = 90
    LIGHTRED_EX     = 91
    LIGHTGREEN_EX   = 92
    LIGHTYELLOW_EX  = 93
    LIGHTBLUE_EX    = 94
    LIGHTMAGENTA_EX = 95
    LIGHTCYAN_EX    = 96
    LIGHTWHITE_EX   = 97
class BackColor(AnsiCodes):
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49
    LIGHTBLACK_EX   = 100
    LIGHTRED_EX     = 101
    LIGHTGREEN_EX   = 102
    LIGHTYELLOW_EX  = 103
    LIGHTBLUE_EX    = 104
    LIGHTMAGENTA_EX = 105
    LIGHTCYAN_EX    = 106
    LIGHTWHITE_EX   = 107
class Style(AnsiCodes):
    BRIGHT    = 1
    DIM       = 2
    NORMAL    = 22
    RESET_ALL = 0
m  = MainColor()
b   = BackColor()
s  = Style()
class Help:
	def help():
		print(
		"""Colors List Back and Main:
	BLACK 
    RED 
    GREEN 
    YELLOW 
    BLUE   
    MAGENTA  
    CYAN 
    WHITE  
    RESET   
    LIGHTBLACK_EX
    LIGHTRED_EX
    LIGHTGREEN_EX 
    LIGHTYELLOW_EX 
    LIGHTBLUE_EX
    LIGHTMAGENTA_EX
    LIGHTCYAN_EX
    LIGHTWHITE_EX
    
    Styles List:
    1. BRIGHT : bright text
    2. DIM : bold text
    3. NORMAL : normal 
    4. RESET_ALL : reset to main""")
	def UpdaterInfo():
		print(
	"Extracted Lib From (colorama) module , by Aymen : @Unpacket on Telegram .")
