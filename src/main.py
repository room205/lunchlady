#!/usr/bin/env python
import os, time

import tweet_queue

espeak_command = "espeak -s 120 -v f1 -k 20 -a 800 \"%s\""

def process(tweet):
    text = tweet.text.lower()

    text = "%s tweeted %s" % (tweet.user.screen_name, text)
    text = text.replace("@roomtwozerofive", "room 2 0 5")
    text = text.replace("#", "hashtag ")

    clean_text = text.replace("\"", "")

    #print clean_text

    os.system(espeak_command % (clean_text,))

def main():
    tq = tweet_queue.get()
    while True:
        tweet = tq.poll()
        if tweet:
            print "%s: %s" % (tweet.user.screen_name, tweet.text)
            process(tweet)
	else:
            time.sleep(30)

if __name__=="__main__":
    main()
