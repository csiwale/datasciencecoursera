import sys
import json

sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])

scores = {} # initialize an empty dictionary

def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))

def init_dict():
	"""Initializes the Dictionary to hold the sentiments and scores""" 
	sent_lines = sent_file.readlines() 

	for line in sent_lines: #afinnfile:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.

	#print scores.items() # Print every (term, score) pair in the dictionary

def parse_twitter_stream():

	#sentiments = open("sentiments.txt", "a")

	tweets = tweet_file.readlines()
	for tweet in tweets:
		try:
			score = 0
			line = json.loads(tweet)["text"]
			words = line.split()	
			for word in words:
				try:
					score = score + scores[word]	
					#print word, scores[word]
				except KeyError:
					continue
			print score
			#sentiments.write(str(score) + "\n")	
			
		except KeyError:
			continue
	

def main():
	#hw()
	#lines(sent_file)
	#lines(tweet_file)
	init_dict()
	parse_twitter_stream()

if __name__ == '__main__':
	main()
