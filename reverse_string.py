text = "Hello World!" #take input string

reversed_text = "" #take empty string to store result of reversed text

#fetching each characters from input string and merge it with previous character in reversed_text string 
for char in text:   
    reversed_text = char + reversed_text

#print the string
print(text)
print(reversed_text)