"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.'
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    a=[i for i in paragraphs if select(i)]
    if k>=len(a):
        return ''
    else:
        return a[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def helper(para):
        para = lower(para)
        para = remove_punctuation(para)
        para = split(para)
        for i in topic:
                if i in para:
                    return True
        return False
    return helper 

    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    lenth = len(reference_words)
    cunt = 0
    if len(typed_words)==0 or len(reference_words)==0:
        return 0.0
    if len(typed_words)==len(reference_words):
        for i in range (0,lenth):
            if typed_words[i]==reference_words[i]:
                cunt+=1
        return float(cunt/lenth)*100
    elif len(typed_words)>len(reference_words):
        for i in range (0,lenth):       
            if typed_words[i]==reference_words[i]:
                cunt+=1
        lenth = len(typed_words)
        return 100*float(cunt/lenth)
    else :
        lenth = len(typed_words)
        for i in range (0,lenth):
            if typed_words[i]==reference_words[i]:
                cunt+=1
        return 100*float(cunt/lenth)



    
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    amout = len(typed)/5
    return float((60/elapsed)*amout)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    temp = []
    for i in valid_words:
        temp.append(diff_function(user_word,i,limit))
        if i ==user_word:
            return i
    if min(temp)>limit:
        return user_word
    else :
        return valid_words[temp.index(min(temp))]
    

    
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def helper(st,go,lim,con):
        if len(st)==0 or len(go)==0:
            return con+abs(len(go)-len(st))
        if con>lim:
            return lim+1
        if st[0]==go[0]:
            return helper(st[1:],go[1:],lim,con)
        elif st[0]!=go[0]:
            return helper(st[1:],go[1:],lim,con+1)
    return helper(start,goal,limit,0)
        
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if start==goal: # Fill in the condition
        # BEGIN
        return 0
        # END
    elif len(start)==0 or len(goal )==0:
        return  abs(len(start)-len(goal))
    elif limit<0: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END
    elif start[0]==goal[0]:
        return pawssible_patches(start[1:],goal[1:],limit)
    

    else:
        add_diff = 1+ pawssible_patches(start,goal[1:],limit-1) # Fill in these lines
        remove_diff = 1+pawssible_patches(start[1:],goal,limit-1)
        substitute_diff = 1+pawssible_patches(start[1:],goal[1:],limit-1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add_diff,remove_diff,substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    cunt =0
    for i in range(0,len(typed)):
        if typed[i]==prompt[i]:
            cunt += 1
        else:
            break
    ratio = float (cunt / len(prompt))
    send({'id':user_id,'progress':ratio})
    return ratio
        
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    lenth = len(times_per_player[0])
    t = []
    for i in times_per_player:
        temp = []
        for b in range(1,lenth):
            a = i[b]-i[b-1]
            temp.append(a)
        t.append(temp)
    return game(words,t)

        
        
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = len(all_times(game)) # contains an *index* for each player 玩家数量
    word_indices = len(all_words(game))  # contains an *index* for each word 单词数量
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    result = []
    for i in range(0,player_indices):
        result.append([])
        
    for i in range(0,word_indices):
        #为每个word找玩家
        time1 = []
        for b in range(0,player_indices):
            time1.append(time(game,b,i))
        dst = time1.index(min(time1))
        result[dst].append(word_at(game,i))
    return result
            



    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)