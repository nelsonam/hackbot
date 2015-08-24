# Hackbot

Hackbot mines twitter for the #hackathon search tag and finds the top authors.

It uses [TwitterSearch](https://github.com/ckoepp/TwitterSearch) for the Twitter API wrapper. Install it using `pip install TwitterSearch`.

A sample file of 100 tweets can be found in `hackcache.txt`. To see the output, run `python read_tweets.py`.

To mine your own tweets or change the keyword that the program searches for, edit `grab_tweets.py`. The Twitter API credentials are set as environment variables, so ensure that these are set on your system before beginning. To set an environment variable, run `export access_token='myaccesstoken'` at the command line.
