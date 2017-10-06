from re import *  # Loads the regular expression module.
import random
from conda._vendor.auxlib._vendor.five import string
from ctypes.wintypes import WORD

cycleCount = 0

def RunMyAgent():
    print(introduce())
    while True:
        the_input = input('TYPE HERE:>> ')
        wordlist = split(' ', remove_punctuation(the_input).strip())
        # Remove any initial capitalization:
        wordlist[0] = wordlist[0].lower()
        if 'bye' in wordlist:
            print('Goodbye! Take Care.')
            return
        mapped_wordlist = you_me_map(wordlist)
        mapped_wordlist[0] = mapped_wordlist[0]
        respond(the_input, wordlist, mapped_wordlist)

def respond(the_input, wordlist, mapped_wordlist):
    global cycleCount
    
    # This production rule gets triggered when the 
    # user just presses enter without typing anything.
    if wordlist[0] == '':
        cycleCount += 1
        if cycleCount % 3 == 0:
            print("How can I help you?")
        elif cycleCount % 3 == 1:
            print("Please say something.")
        else:
            print("I didn't get you.")
        return
    
    # This rule gets triggered when the user types
    # a greeting message like Good Morning or Good Night.
    if (len(wordlist) == 2 
        and wordlist[0] == 'good' 
        and check_time_of_day(wordlist[1])):
        print(stringify(wordlist[0:2]) + '! ' + 'Do you need health and fitness advice?')
        return
    
    if 'no' in wordlist or 'No' in wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            print("I am sorry, but I am programmed to give health and fitness advice")
        elif cycleCount % 3 == 1:
            print("Try squats or leg press instead.")
        else:
            print("Don't be so negative.")
        return
    
    if verbp(wordlist[0]):
        cycleCount += 1
        if cycleCount % 3 == 0:
            message = 'Why do you want me to ' + stringify(mapped_wordlist) + '?'
            print(message)
        elif cycleCount % 3 == 1:
            message = 'Pilates can help you ' + wordlist[0]
            print(message)
        else:
            message = 'Zumba can help you ' + wordlist[0]
            print(message)
        return
    
    if 'dislike' in wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            print('I will give you a work-out plan that will help you like ' 
                  + stringify(mapped_wordlist[mapped_wordlist.index('dislike') + 1:]) + '.') 
        elif cycleCount % 3 == 1:
            print('Meditation will ensure that you like ' 
                  + stringify(mapped_wordlist[mapped_wordlist.index('dislike') + 1:]) + '.')
        else:
            print(stringify(mapped_wordlist[mapped_wordlist.index('dislike') + 1:]) + 
                  'are not good for health. It is great that you dislike them')
        return 
    
    if 'hate' in wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            print('I will give you a work-out plan that will help you like ' 
                  + stringify(mapped_wordlist[mapped_wordlist.index('hate') + 1:]) + '.')
        elif cycleCount % 3 == 1:
            print('Meditation will ensure that you like ' 
                  + stringify(mapped_wordlist[mapped_wordlist.index('hate') + 1:]) + '.')
        else:
            print(stringify(mapped_wordlist[mapped_wordlist.index('hate') + 1:]) + 
                  ' is not good for your health. It is great that you dislike them')
        return

    if 'yes' in wordlist or 'Yes' in wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            print('That sounds awesome!')
        elif cycleCount % 3 == 1:
            print('How can you be so sure?')
        else:
            print('If you like it then please follow the workout plan for the next three weeks to see results.')
        return
    
    if 'love' in wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            print('Glad you love it!')
        elif cycleCount % 3 == 1:
            print('I love ' + stringify(wordlist[wordlist.index('love') + 1]) + ' too.')
        else:
            print('I like ' + stringify(wordlist[wordlist.index('love') + 1]) + ' too.')
        return
    
    if 'like' in wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            print('Glad you like it!')
        elif cycleCount % 3 == 1:
            print('I like ' + stringify(wordlist[wordlist.index('like') + 1]) + ' too.')
        else:
            print('I love ' + stringify(wordlist[wordlist.index('like') + 1]) + ' too.')
        return    
    
    if wpred(wordlist[0]):
        if('your' in wordlist and 'name' in wordlist):
            print('My name is ' + agentName() + ". How can I help you?")
            return
        else:
            print("You tell me " + stringify(mapped_wordlist) + ".")
            return

    if 'ok' in wordlist or ("got" in wordlist and 'it' in wordlist) or 'thank' in wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            print('Glad you like it')
        elif cycleCount % 3 == 1:
            print('Cool. Do you need more fitness tips?')
        else:
            print('Awesome. Do you need more health advice?')
        return        

    if 'because' in wordlist or 'as' in wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            message = 'Is that really the reason?'
            print(message)
            return
        elif cycleCount % 3 == 1:
            message = 'Hmm. Are you sure?'
            print(message)
        else:
            message = 'Did you think of alternatives?'
            print(message)
        return
    
    if "can't" in wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            message = 'Yes you can ' + stringify(mapped_wordlist[mapped_wordlist.index("can't") + 1:]) + '.'
            print(message)
        elif cycleCount % 3 == 1:
            message = 'I am with you. You can ' + stringify(mapped_wordlist[mapped_wordlist.index("can't") + 1:]) + '.'
            print(message)
        else:
            message = 'Meditation can help you ' + stringify(mapped_wordlist[mapped_wordlist.index("can't") + 1:]) + '.'
            print(message)
        return
    
    if "cannot" in wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            message = 'Yes you can ' + stringify(mapped_wordlist[mapped_wordlist.index("cannot") + 1:]) + '.'
            print(message)
        elif cycleCount % 3 == 1:
            message = 'I am with you. You can ' + stringify(mapped_wordlist[mapped_wordlist.index("cannot") + 1:]) + '.'
            print(message)
        else:
            message = 'Meditation can help you ' + stringify(mapped_wordlist[mapped_wordlist.index("cannot") + 1:]) + '.'
            print(message)
        return
    
    if wordlist[0:2] == ['can', 'you'] or wordlist[0:2] == ['could', 'you']:
        cycleCount += 1
        message = wordlist[0] + ' ' + stringify(mapped_wordlist[2:]) + '.'
        if cycleCount % 3 == 0:
            print("Perhaps I " + message)
        elif cycleCount % 3 == 1:
            print('I guess I can ' + message)
        else:
            print('Yes, I can ' + message)
        return
    
    if 'you' in mapped_wordlist or 'You' in mapped_wordlist:
        cycleCount += 1
        if cycleCount % 3 == 0:
            print('Drinking two glasses of water in the morning will ensure that ' + stringify(mapped_wordlist) + '.')
        elif cycleCount % 3 == 1:
            print('You should have a cup of green tea before ' + stringify(mapped_wordlist) + '.')
        else:
            print('Try a protein shake before ' + stringify(mapped_wordlist) + '.')
        return
        
    print(punt())

def introduce():
    message = """My name is HealthyBot, and I am here to take care of your health and fitness. 
I was programmed by Karan Murthy. If you don't like my behaviour, contact him at karan7@uw.edu. 
Do you want to live a healthy life?"""
    return message

def agentName():
    return "HealthyBot"

def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

punctuation_pattern = compile(r'\,|\.|\?|\!|\;|\:|\"')    

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern, '', text)

def wpred(w):
    'Returns True if w is one of the question words.'
    return (w in ['when', 'why', 'where', 'how', 'what'])

def dpred(w):
    'Returns True if w is an auxiliary verb.'
    return (w in ['do', 'can', 'should', 'would'])

def check_time_of_day(time):
    'Returns True if time is one of the following options.'
    return (time.lower() in ['morning', 'evening', 'day', 'night'])
    return
 
PUNTS = ['Eating well is a habit. Cultivate it.',
         'Exercise is therapy',
         'Manage your stress levels to live a healthy life.',
         "Don't just train for summer. Train for life.",
         'The body achieves what the mind believes.',
         'I hope you like my fitness tips.']

punt_count = 0
def punt():
    'Returns one from a list of default responses.'
    global punt_count
    punt_count += 1
    return PUNTS[punt_count % 6]



CASE_MAP = {'i':'you', 'I':'you', 'me':'you', 'you':'me',
            'my':'your', 'your':'my',
            'yours':'mine', 'mine':'yours', 'am':'are'}

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

def verbp(w):
    'Returns True if w is one of these known verbs.'
    return (w in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',
                  'make', 'get', 'jump', 'write', 'type', 'fill',
                  'put', 'turn', 'compute', 'think', 'drink',
                  'blink', 'crash', 'crunch', 'add'])

if __name__ == '__main__':
    RunMyAgent()  # Launch the program.


