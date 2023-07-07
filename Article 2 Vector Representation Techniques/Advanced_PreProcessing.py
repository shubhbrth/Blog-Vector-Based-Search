import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

root_technique = "Lemmatization" # or "Stemming"

input_text = ""

# Tokenize text into individual words or token
text_tokens = word_tokenize(input_text)

# Remove Stop words
clean_tokens = [token for token in text_tokens if not token in stop_words]

# Get root of words
if root_technique == "Lemmatization":
  root_tokens = [lemmatizer.lemmatize(token) for token in clean_tokens]
elif root_technique == "Stemming":
  root_tokens = [stemmer.stem(token) for token in clean_tokens]

clean_text = " ".join(root_tokens)