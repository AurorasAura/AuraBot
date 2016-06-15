from sopel.module import rule, priority, rate
import random
import time

@rule('^\s*[Ww]([Bb]|elcome\s*back)[\s:,].*$nickname')
def wb(bot, trigger):
    set1 = ['Thank you', 'thanks']
    set2 = ['!', ' :)', ' :D']
    respond = [ str1 + str2 for str1 in set1 for str2 in set2]
    randtime = random.uniform(0, 7)
    time.sleep(randtime)
    bot.reply(random.choice(respond))


@rule('\s*([Xx]+[dD]+|([Hh]+[Aa]+)+)')
@rate(100)
def xd(bot, trigger):
    respond = ['xDDDDD', 'XD', 'XDDDD', 'haha']
    randtime = random.uniform(0, 3)
    time.sleep(randtime)
    bot.say(random.choice(respond))


@rule('(?i)$nickname\:\s+(bye|goodbye|gtg|seeya|cya|ttyl|g2g|gnight|goodnight)')
@rate(30)
def goodbye(bot, trigger):
    byemsg = random.choice(('Bye', 'Goodbye', 'Seeya', 'Auf Wiedersehen', 'Au revoir', 'Ttyl'))
    punctuation = random.choice(('!', ' '))
    bot.say(byemsg + ' ' + trigger.nick + punctuation)
	

@rule('hello there')
def test(bot, trigger):
	bot.say("Hi " + trigger.nick)
	reply1 = ("I am a test")
	resp1 = ("How are you?")
	if ("good"):
		bot.say(resp1)