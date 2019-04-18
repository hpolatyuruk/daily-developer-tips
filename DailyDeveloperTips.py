import os
import time
import random
import tweepy
import datetime
from configparser import ConfigParser

def get_tokens(fileName = os.path.join(os.getcwd(), 'tokens.ini'), section = 'tokens'):
    parser = ConfigParser()
    parser.read(fileName)

    # get section, default to postgresql

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, fileName))
    return db

tokens = get_tokens()

if len(tokens['consumer_key']) == 0:
    print('Please enter your app consumer key.')
    exit()
if len(tokens['consumer_secret']) == 0:
    print('Please enter your app consumer secret.')
    exit()
if len(tokens['access_key']) == 0:
    print('Please enter your app access token key.')
    exit()
if len(tokens['access_secret']) == 0:
    print('Please enter your app access secret.')
    exit()

auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
auth.set_access_token(tokens['access_key'], tokens['access_secret'])

api = tweepy.API(auth)

tweets = [
    'Start small, then extend.',
    'Change one thing at a time.',
    'Add logging and error handling early.',
    'All new lines must be executed at least once.',
    'Test the parts before the whole.',
    'Everything takes longer than you think.',
    'First understand the existing code.',
    'Read and run.',
    'There will always be bugs.',
    'Solve trouble reports.',
    'Reproduce the problem.',
    'Fix the known errors, then see what’s left.',
    'Assume no coincidences.',
    'Correlate with timestamps.',
    'Face to face has the highest bandwidth.',
    'Rubber ducking.',
    'Ask.',
    'Share credit.',
    'Try it.',
    'Sleep on it.',
    'Change.',
    'Keep learning.',
    'If you can automate it, automate it.',
    'Rewriting a system from the ground up is essentially an admission of failure as a designer. It is making the statement, "We failed to design a maintainable system and so must start over."',
    'Rewriting code is a developer illusion, not the solution in most cases',
    'Consider refactoring before taking a step to code rewriting',
    'Rewriting softrare: Beware. This is a longer, harder, more failure-prone path than you expect',
    'Rewriting software: Ensure new product is better than the old one at solving user\'s problem or at least the same. Worse cannot be acceptable',
    'Rewriting software: Keep maintaining and supporting the existing product while rewriting the old one',
    'Rewriting software: Involve users in the design process as soon as possible',
    'Rewriting software: Keep the teams working on the product synced while rewriting your software',
    'Rewriting software: Don\'t make dramatic changes in the new product',
    'Don\'t make your product depend on only one developer',
    'Rewriting software: Migrations should be slow and steady from old product the new product',
    'Rewriting your code from scratch could be the single biggest mistake you make, but equally so, not-rewriting your code could lead to the same result. Here is a piece of advice. Refactoring should be the first option',
    'Some developers will keep believing that all systems must eventually be rewritten. Always keep in mind that this is not true. It is possible to design a system that never needs to be thrown away',
    'There will be always a software designer around you saying "We\'ll have to throw the whole thing away someday anyway". But if software were built right to start with and then properly maintained, why would it be thrown away?',
    'When to rewrite the software: Switching to another language or platform',
    'When to rewrite the software: The existing codebase is not maintainable anymore',
    'When to rewrite the software: You have the resources available to both maintain the existing system and design a new system at the same time',
    'When to rewrite the software: The developers in the team are a bottleneck for software',
    'When to rewrite the software: The software is long-lived (I\'m talking like 10–20 years or more)',
    'Rewriting the software: The correct thing to do is to handle the complexity of the existing system without a rewrite, by improving the system\'s design in a series of simple steps',
    'The purpose of software is not to show off how intelligent you are',
    'Don\'t forget: The purpose of software is to help people',
    'Every programmer is a designer. So remember this while you are writing your code',
    'The goal of the software is to design systems that can be created and maintained as easily as possible by their developers, so that they can be - and continue to be - as helpful as possible.',
    'Understanding is the key difference between a bad developer and a good developer.',
    'Developers who don\'t fully understand their work tend to develop complex systems.',
    'Misunderstanding leads to complexity, which leads to further misunderstanding, and so on',
    'Bad developers don\'t understand what they are doing, and good developers do. It really is that simple',
    'Simplicity is the ultimate sophistication. - Leonardo da Vinci',
    'Complexity has nothing to do with intelligence, simplicity does. - Larry Bossidy',
    'Developers who are new to your code don\'t know anything about it; they have to learn. So, you should ask this question: "Do I want people to understand this and be happy, or do I want them to be confused and frustrated?"',
    'How simple do you have to be? Here is your answer: Stupid, dumb simple',
    'Controlling complexity is the essence of computer programming. - Brian Kernighan',
    'As a developer, your main purpose is to control complexity, not to create it.',
    'Don\'t forget: All changes require maintenance.',
    'It is more important to reduce the effort of maintenance than it is to reduce the effort of implementation.',
    'Consistency is a big part of simplicity. If you do something one way in one place, do it that way in every place.',
    'The desirability of any change is directly proportional to the value of the change and inversely proportional to the effort involved in making the change.',
    'The changes that will bring you a lot of value and require little effort are better than those that will bring little value and require a lot of effort.',
    'If you can\'t explain something in simple terms, you don\'t understand it. - Richard Feynman',
    'Think before acting',
    '"Perfect is the enemy of good." - Voltaire',
    'Start small, improve it, then extend.',
    'Being too generic involves a lot of code that isn\'t needed.',
    'Don\'t be too generic',
    'Don\'t predict to future. Be only as generic as you know you need to be right now.',
    'Code should be designed based on what you know now, not on what you think will happen in the future.',
    'Don\'t reinvent the wheel',
    'Stop Reinventing',
    'As a developer, your first reaction to changing requests should be "NO''. Always resist adding more code, more features until you are convinced that they are required and there is a need to implement them',
    'Don\'t forget: Unnecessary changes will increase defects in your software',
    'The optimum code is a small bunch of code that is easy to understand, easy to read.',
    'If your software contains hundred of thousands of lines, it\'t doesn\'t mean your software is so big. Check your unnecessary codes.',
    '"One of my most productive days was throwing away 1000 lines of code." - Ken Thompson',
    'Untested code is the code that doesn\'t work.',
    'Developers\' estimation sucks',
    'Rewriting software: Refactoring should be the first option.',
    'Write a comment to explain "WHY", not to explain "WHAT".',
    'Don\'t depend on external technologies or reduce your dependency to them as much as possible.',
    'Know that every specific problem has its own specific solution.',
    'Try out different programming languages and tools, read books on software development. They will give you another perspective.',
    'Don\'t be a hero',
    'Don\'t be obsessive. Know when to quit.',
    'Don\'t hesitate to ask for help.',
    'When you have something to implement and you are not sure about the solutions, don\'t ask others how to solve it …at least not immediately. Instead, try anything and everything you can think of.',
    'Assumptions are poison',
    'Assumptions are your enemy',
    'How to solve a problem: 1.Understand 2.Plan 3.Divide it into smaller tasks',
    'Don\'t try to solve one big problem',
    'The factors you should consider before you start using some technology:Is there active development behind it? Will it continue to be maintained? How easy is it to switch away from? What does the community say about it?',
    'It\'s harder to read code than to write it.',
    'The issue is not on their side, it is on your side',
    'It should work now but probably it will not work.',
    '"It’s 90% done." you know it\'s a lie',
    'Learn to identify them, make habits to avoid them',
    'Think. Research. Plan. Write. Validate. Modify.',
    'Don\'t write code without planning',
    'Don\'t plan too much before writing code',
    'Do not look for a perfect plan',
    'Don\'t underestimate the importance of code quality',
    'Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.— John Woods',
    'There are only two hard things in Computer Science: cache invalidation and naming things.',
    'Measuring programming progress by lines of code is like measuring aircraft building progress by weight. — Bill Gates',
    'There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies, and the other way is to make it so complicated that there are no obvious deficiencies.— C.A.R. Hoare',
    'Fail early and fail often.',
    'Do not be attached to code because of how much effort you put into it. Bad code needs to be discarded.',
    'Google it first',
    'The most dangerous thought that you can have as a creative person is to think that you know what you’re doing. — Bret Victor',
    'Don\'t plan for the unknown',
    'Don\'t make existing code worse',
    'Don\'t write comment about the obvious things',
    'Write unit tests',
    'Don\'t assume that if things are working then things are right',
    'Always question the existing code',
    'Don\'t be obsessive about best practices',
    'Don\'t be obsessive about performance',
    'Premature optimization is the root of all evil (or at least most of it) in programming— Donald Knuth',
    'Target the end-user experience',
    'Know to pick the right tool for the job',
    'Understand that code problems will cause data problems',
    'Don\'t have the wrong attitude towards code reviews',
    'Always use source control',
    'Break things',
    'Cheap, fast, high quality. Pick any two.'
]

last_tweet_index = 0
tweet_indexes = list(range(0, len(tweets)))

while True:
    try:     
        tweet_index = random.choice(tweet_indexes)
        api.update_status(tweets[tweet_index])

        # twitter doesn't allow us to tweet same status in same day
        # therefore we remove the already tweet from list to skip it
        tweet_indexes.remove(tweet_index)

        # refill the list to start from scratch to tweet them all for new day
        if len(tweet_indexes) == 0:
            tweet_indexes = list(range(0, len(tweets)))

        # every 3hours
        time.sleep(10800)
    except tweepy.error.TweepError as err:
        print(err)
    