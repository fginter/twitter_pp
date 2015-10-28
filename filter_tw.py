#-*- coding: utf-8 -*-

import json
import sys
import re
import codecs

out8=codecs.getwriter("utf-8")(sys.stdout)

focus_h_tags=set((u"pakolaiset",u"refugeecrisis",u"syrianrefugees",u"syria",u"syyria",u"pakolaiskriisi",u"migrantcrisis",u"refugeeswelcome",u"migrants",u"réfugiés",u"syrie"))
def keep(tweet):
    """in goes one tweet parsed json
    returns True/False do we want it or not"""
    htags=set(h["text"].lower() for h in tweet["entities"]["hashtags"])
    return htags&focus_h_tags

ws_re=re.compile(r"\s+")
def print_tweet(t):
    l=t["lang"]
    ul=t["user"]["lang"]
    tstamp=t["created_at"]
    geo=t["coordinates"]
    ugeo=t["user"]["location"]
    if not ugeo or not ugeo.strip():
        ugeo=u"NA"
    else:
        ugeo=ugeo.strip()
    place=t["place"]
    if not geo:
        geo=u"NA"
    else:
        geo=u"%f,%f"%tuple(geo["coordinates"])
    if not place:
        place=u"NA"
    else:
        place=place["full_name"]
    htags=u",".join(sorted(set(h["text"].lower() for h in t["entities"]["hashtags"])))
    txt=ws_re.sub(u" ",t["text"])
    print >> out8, u"\t".join((l,tstamp,geo,place,ul,ugeo,htags,txt))

print >> out8, u"\t".join((u"Lang",u"Time",u"TweetGeo",u"TweetPlace",u"UserLang",u"UserPlace",u"HashTags",u"Text"))
with open("/dev/stdin","r") as f_in:
    tweet_list=json.load(f_in)
    print >> sys.stderr, "Tweets:", len(tweet_list)
    counter=0
    for t in tweet_list:
        if not keep(t):
            continue
        print_tweet(t)
        counter+=1
    print >> sys.stderr, "Matched:", counter

