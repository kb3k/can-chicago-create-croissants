# can-chicago-create-croissants

ISO layered, artisan croissants. Perhaps Yelp or Google reviews can help us narrow down a few top contenders before we go off and meander all over the city.

![alt_text](https://github.com/kb3k/can-chicago-create-croissants/blob/main/imgs/croissant.jpeg)

source/baker: Claire Saffitz

in this repo you will find 

1. nlp/nlp.ipynb which conducts a basic Naive Bayes algorithm against text to determine whether a bakery may be artisan, maybe, or definitely not

2. nlp/label_data which involves the thought process behind the user labeling a bakery (based on 1 review, admittedly this is limiting) belonging to one of three categories:

I. artisan
II. maybe artisan
III. not artisan

3. nlp/extract_info.ipynb performs a word frequency distribution analysis, and cleans the data ultimately yielding a tokenized, stemmed, lower cased text filtered of tokenizing, filteed of stop words. 

4. artisan_croissant_locator.ipynb which uses BeautifulSoup to scrape the web for some Chicago bakery reviews involving the word 'croissant'

