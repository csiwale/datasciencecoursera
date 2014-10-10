import sys
import json
import operator

tweet_file = open(sys.argv[1])

freq = {}

def parse_twitter_stream():
	tweets = tweet_file.readlines()
	for tweet in tweets:
		try:
			hashtags = json.loads(tweet)["entities"]["hashtags"]
			
			for hashtag in hashtags:
				hashtag = hashtag["text"].encode("utf-8")
				if (hashtag in freq):
					freq[hashtag] = freq[hashtag] + 1
				else:
					freq[hashtag] = 1

		except KeyError:
			continue


	sorted_hashtags = []
	for key, value in sorted(freq.iteritems(), key=lambda (k,v): (v,k), reverse = True):
		sorted_hashtags.append((key, value))
		#print "%s: %s" % (key, value)

	#new = sorted_hashtags[1:10]	

	for i in range(10):
		print "%s: %s" % (sorted_hashtags[i][0], sorted_hashtags[i][1])



def main():
	parse_twitter_stream()

if __name__ == '__main__':
	main()
