import sys
import json

tweet_file = open(sys.argv[1])
total_words = []
freq = {}

def parse_twitter_stream():

	#sentiments = open("sentiments.txt", "a")

	tweets = tweet_file.readlines()
	for tweet in tweets:
		try:
			line = json.loads(tweet)["text"]
			words = line.split()
			
			for word in words:
				word = word.rstrip('?:!.,;"!@')
				word = word.replace("\n", "")		
				total_words.append(word)
			
		except KeyError:
			continue
	
	#unique_words = set(total_words)
	length = len(total_words)
	
	for word in total_words:
		if(word in freq):
			freq[word] = freq[word] + 1
		else:
			freq[word] = 1
	
	for word in freq:
		freq[word] = "%f" %(float(freq[word])/length)
		print word.encode("utf-8"), freq[word]
	#from itertools import groupby
	#valdict = dict((k, len(list(g))) for k, g in groupby(sorted(total_words)))
	
	#len_total = len(total_words)
	
	#for key, val in valdict.items():
		#print ("%s %f" % (key, float(val)/float(len_total)))

def main():
	parse_twitter_stream()

if __name__ == '__main__':
	main()
