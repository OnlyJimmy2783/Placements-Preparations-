text = input("Enter The String:") #take input from user

text = text.lower() #to ensure case-insensative matching

reversed_text = "" #to reverse the string and fetching characters from the end
for char in text:
    reversed_text = char + reversed_text

#matching the text with the reversed text
if(text == reversed_text):
    print("✅ The String Is Palindrome.")
else:
    print("❌ The String Is Not Palindrome.")
