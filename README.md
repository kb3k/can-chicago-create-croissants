# can-chicago-create-croissants

ISO layered, artisan croissants. Perhaps a few Yelp reviews can help us narrow down a few top contenders potentially worthy of taking the trip to visit (and consuming large amts of butter) in this POC.

![alt_text](https://github.com/kb3k/can-chicago-create-croissants/blob/main/imgs/croissant.jpeg)

source/baker: Claire Saffitz

In this repo, you will find 4 notebooks with the following functionality:

1. nlp/nlp

Conducts a basic Naive Bayes algorithm against text to determine whether a bakery may be artisan, maybe, or definitely not.

2. nlp/label_data

Involves the thought process and source code behind labeling a bakery as artisan, maybe, or not artisan.

Note: the labeling is for experiment purposes only and is by no means intended to be taken seriously by any consumer outside of this POC.

3. nlp/extract_info 

Performs a word frequency distribution analysis. Cleans the data ultimately yielding a tokenized, stemmed, lower cased text filtered of tokenizing, filtered of stop words. 

4. artisan_croissant_locator

Uses BeautifulSoup to scrape the web for some Chicago bakery reviews involving the word 'croissant.'

Limitations:

There is only 1 review per bakery, totaling 90 reviews total. More reviews, perhaps from another medium such as Google, would ideally be collected per bakery as 1 review does not decide all. However for the business use case, 1 review will suffice.
