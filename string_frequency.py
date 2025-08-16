text = input("Enter The String:")   #take input from users
size = len(text)    #size of the string named text (optional)

freq = {}   #empty dictionary for count the frequency of each character
for ch in text:
    freq[ch] = freq.get(ch,0) + 1
              #freq.get(key,default) 
              
print(freq)
print(size)


#NOTE : Frequency means how many times a characters are repeted in a string.