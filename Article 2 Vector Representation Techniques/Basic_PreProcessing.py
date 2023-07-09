import re

input_text = "Wooden Table https://github.com/shubhbrth/ -*/"
#   Convert the text to Lowercase (wooden <--SAME--> Wooden)
text = input_text.lower()
#   Remove if any URL Present
text = re.sub(r"https?://\S+", "", text)
#   Remove Special Character {$, %, Š, Ú, etc.}
text = re.sub(r"[^\w\s]", " ", text)
#   Remove Concurrent Blank Spaces
text = re.sub(r"\s+", " ", text)