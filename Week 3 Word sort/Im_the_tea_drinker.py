#made by Michael parker
#discord Im_the_tea_drinker_
#03/05/22 discord challenge 
 
import string
from collections import Counter
 
cleaner = input("Enter text: \n")
tosplit = cleaner.translate(str.maketrans('', '', string.punctuation))
 
clean = tosplit.split()
print(f"{clean}\n\n")
done = Counter(clean)
print(done)