from sopel.module import rule, priority, rate
import random
import time
@rule('yes|no')
@rate(15)
def yesno(bot, trigger):
	bot.say ("hi " + trigger.nick)
	rand = random.uniform(0, 5)
	text = trigger.group()
	text = text.split(":")
	time.sleep(rand)
	if text[0] == 'yes':
		bot.reply("no")
	elif text[0] == 'no':
		bot.reply("yes")
