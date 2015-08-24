import os
import re
import operator
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

with open('hackcache.txt','rb') as f:
    lines = f.readlines()
    top_authors = {} # a dictionary of the top tweeters
    #pattern = re.compile("@* tweeted:")
    for line in lines:
        #if pattern.match(line):
        # pull out the author's name
        if line[0] == '@':
            author = line.split()[0]
        # add one to the dictionary top_authors
        if author not in top_authors:
            top_authors[author] = 1
        else:
            top_authors[author] += 1
    outfile = open('top_tweeters.txt','w')

    print "the top tweeters are: "

    sorted_authors = sorted(top_authors.items(), key=operator.itemgetter(1), reverse=True)
    for k,v in sorted_authors:
        print "{} tweeted {} times".format(k,v)
    outfile.close()


