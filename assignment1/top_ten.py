import sys
import json
import types
import operator

tweet_file = open(sys.argv[1])

freq = {}

def parse_twitter_stream():
	for line in tweet_file:
			tweet = json.loads(line)
			if 'entities' in tweet and type(tweet['entities']) is not types.NoneType:
				if 'hashtags' in tweet['entities'] and type(tweet['entities']['hashtags']) is not types.NoneType:
					hashtags = tweet['entities']['hashtags']
					for hashtag in hashtags:
						tag = hashtag['text'].encode('utf-8')
						if freq.has_key(tag):
							freq[tag] += 1
						else:
							freq[tag] = 1

	for x in range(10):
		print sorted(freq.items(), key=lambda x:x[1], reverse=True)[x][0],
		print ' ',
		print float(sorted(freq.items(), key=lambda x:x[1], reverse=True)[x][1])



def main():
	parse_twitter_stream()

if __name__ == '__main__':
	main()
