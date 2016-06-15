from sopel import module

@module.rule('(.*)has joined!?')
def welcome(bot, trigger):
    bot.say('Welcome back dumbass ' + trigger.nick)

@module.rule('Fuck')
def welcome(bot, trigger):
    bot.say('O_o ')