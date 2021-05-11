import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    thing = book_to_words()
    bot, maxLength = 1, 1
    for word in thing:
      if len(word) >= maxLength:
        maxLength = len(word)

    while True:
      diff = maxLength-bot
      asciiArray, indexArray = [0]*128, [0]*128
      for word in thing:
        if diff < 0:
          break
        elif diff >= len(bytes(word)):
          asciiArray[0]+=1
        else:
          new = word[diff]
          asciiArray[new]+=1

      count = 0
      for x in range(128):
        count += asciiArray[x]
        if count == 0:
          indexArray[x] = 0
        else:
          indexArray[x] = count

      radixThing = [0]*len(thing)
      for word in reversed(thing):
        if len(bytes(word)) <= diff:
          start = 0
        else:
          start = (bytes(word))[diff]
        try:
          radixThing[indexArray[start]] = word
        except:
          pass
        indexArray[start] -= 1

      thing, bot = radixThing, bot+1
    return thing
