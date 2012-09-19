import re

# Kaikki botin asetukset
HOST = 'irc.xs4all.nl' # The server we want to connect to
PORT = 6667 # The connection port which is usually 6667
NICK = 'Hurtta' # The bot's nickname
IDENT = 'HurttaBot'
REALNAME = 'Hurtta'
OWNER = ['joosal@linux.utu.fi','romeri@linux.utu.fi', 'ejsuva@linux.utu.fi', 'njkang@linux.utu.fi'] # The bot owner's nick
CHANNELINIT = '#utu.tuntuma' # The default channel for the bot
CHANNELPASS = 'hurtta' # passwd for default channel
COMMAND = '%' # Treat all lines starting with this as command
QUITMSG = NICK + ' has left the building...'
JOINMSG = "I'm on watch, watch out."
UNKNOWNCOMMANDMSG = "Check your shit, I have no idea what that is supposed to mean."
URLSAVEDMSG = "I've saved your mother effing URL!"
JOKEFAILMSG = "Srry, couldn't get you a joke this time."
JOINED = False
URLREGEXPS = [
	re.compile("([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|(((news|telnet|nttp|file|http|ftp|https)://)|(www|ftp)[-A-Za-z0-9]*\\.)[-A-Za-z0-9\\.]+)(:[0-9]*)?/[-A-Za-z0-9_\\$\\.\\+\\!\\*\\(\\),;:@&=\\?/~\\#\\%]*[^]'\\.}>\\),\\\"]"),
	re.compile("([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|(((news|telnet|nttp|file|http|ftp|https)://)|(www|ftp)[-A-Za-z0-9]*\\.)[-A-Za-z0-9\\.]+)(:[0-9]*)?"),
	re.compile("(~/|/|\\./)([-A-Za-z0-9_\\$\\.\\+\\!\\*\\(\\),;:@&=\\?/~\\#\\%]|\\\\)+"),
	re.compile("'\\<((mailto:)|)[-A-Za-z0-9\\.]+@[-A-Za-z0-9\\.]+"), # mailto
	re.compile("(spotify:(?:(?:artist|album|track|user:[^:]+:playlist):[a-zA-Z0-9]+|user:[^:]+|search:(?:[-\\w$\\.+!*'(),]+|%[a-fA-F0-9]{2})+))"), #Spotify URL
]