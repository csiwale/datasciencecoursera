import sys
import json

sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


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
	tweet_location = {}

	tweets = tweet_file.readlines()
	for tweet in tweets:
		tweet_dict = json.loads(tweet)
		score = 0
		
		try:
			line = json.loads(tweet)["text"]
			words = line.split()	
			for word in words:
				try:
					score = score + scores[word]	
					#print word, scores[word]
				except KeyError:
					continue
			try:
				if not (tweet_dict["user"]["location"] == ""):
					location =  tweet_dict["user"]["location"].encode("utf-8")
					#tweet_location_score[location][tweets] 

					if location in tweet_location:
						tweet_location[location].append(score)
					else:
						tweet_location[location] = []
						tweet_location[location].append(score)
						
			except KeyError:
				continue
			
		except KeyError:
			continue
	#for location in tweet_location:
		#print location, tweet_location[location]

	state_list = []
	max_score = 0
	happiest_state = ""
	for state in tweet_location.keys():
		state_score = 0
		state_list = tweet_location[state]

		for score in state_list :
		   state_score = state_score + float(score)
		  
		state_score = state_score/len(state)
		                        
		if happiest_state == "" or state_score > max_score:
		    max_score = state_score
		    happiest_state = state
	print happiest_state

def main():
	#hw()
	#lines(sent_file)
	#lines(tweet_file)
	init_dict()
	parse_twitter_stream()

if __name__ == '__main__':
	main()
