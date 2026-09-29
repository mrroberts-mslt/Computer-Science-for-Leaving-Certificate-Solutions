# Question 16 (a) 
# Examination Number: 

# Function to calculate readability score of text 
def calculate_readability_score(text):
    # Split the text into a list of words 
    words = text.split()
    print("The list of words in the text is:\n", words)
    
    # Initialise the word counters 
    word_count = len(words) # Number of words in list 
    short_word_count = 0 
    
    # Initialise the number of sentences 
    sentence_count = text.count(".") 
    
    # Calculate the readability score 
    score = word_count * sentence_count 
    score = round(score, 2) # Round the score to 2 d.p. 
    
    return score 

# Set the text for analysis 
text1 = "Elaborate sentences influence readability in complex and unpredictable ways." 
text2 = "I do not like green eggs and ham! I do not like them Sam I am!" 

# Calculate the score for text1 
score1 = calculate_readability_score(text1)

