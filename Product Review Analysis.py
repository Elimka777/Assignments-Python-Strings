#Write a program that searches through a series of product reviews for keywords 
# such as "good", "excellent", "bad", "poor", and "average". 
# Print out each review with the keywords in uppercase so they stand out.
def keyword_search(python_reviews, keywords):
    for review in python_reviews:
        highlighted_review = review
        for keyword in keywords:
            highlighted_review = highlighted_review.replace(keyword, keyword.upper())
            highlighted_review= highlighted_review.replace(keyword.capitalize(), keyword.upper())
        print(highlighted_review)
python_reviews = [ 
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.", 
    "Poor quality product. Wouldn't recommend it to anyone.", 
    "The product was average. Nothing extraordinary about it." 
]

keywords = ["good", "excellent", "bad", "poor", "average"]   
keyword_search(python_reviews, keywords)

# Develop a function that tallies the number of positive and negative words in each review.
# Use a predefined list of positive and negative words to check against. 
# The function should return the count of positive and negative words for each review.
def counter(python_reviews, positive_words, negative_words):
    num_positive = 0
    num_negative = 0
    for review in python_reviews:
     for positive_word in positive_words:
         if positive_word in review.lower():
             num_positive+=1
     for negative_word in negative_words:
          if negative_word in review.lower():
              num_negative +=1
    print(f"The number of positive feedbacks are {num_positive}.")
    print(f"the number of negative feedbacks are {num_negative}.")
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
python_reviews = [ 
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.", 
    "Poor quality product. Wouldn't recommend it to anyone.", 
    "The product was average. Nothing extraordinary about it." 
]

counter(python_reviews, positive_words, negative_words)
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary.
# Ensure that the summary does not cut off in the middle of a word.
def summary(review):
    max_length= 30
    if len(review) <= max_length:
        return review
    truncated_review = review[:max_length]
    
    if review[max_length].isalpha():
        last_space = truncated_review.rfind(' ')
        if last_space != -1:
            truncated_review = truncated_review[:last_space]
    
    return truncated_review + "…"

reviews = [ 
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.", 
    "Poor quality product. Wouldn't recommend it to anyone.", 
    "The product was average. Nothing extraordinary about it." 
]

summaries = [summary(review) for review in reviews]
for summary in summaries:
    print(summary)