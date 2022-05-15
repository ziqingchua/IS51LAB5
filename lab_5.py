


"""
The program is trying to translate a sentence caprured as user input.
We first read in the text file textese.txt.
then from the text file, we create a list of strings from each lines in the text file
Then, we create a dictionary from the list.
Once the text file has been read into memory, we close the file.

We define a function for translating which involves splitting the user input (sentence) into an
array of strings ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

Once we have the array of strings representing the user's input sentence, we
loop through each words, find the key matching the word and retirns back the value tied to the word
in our dictionary. 

After each word is translated, we then
print out the translated sentance to the user. 
"""

"""
main():
  sentence = input ()
  set dictionary = create_dictionary()
  translate(sentence, dictionary)

translate(sentence, dictionary):
  words = for each of the word in the sentence,
  for each words, translate the word
  print trabslated sentence to user

create dictionary():
  read in textese.txt
  create list = each line from the text file
  close the file
  create a dict off of the list
  return the dict

main()
"""