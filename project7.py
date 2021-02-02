def readWords(fileName):
  wordList=[]  
  with open(fileName,'rt') as file:
    for line in file:
      word=line.strip()
      if word:
        wordList.append(word)
  return wordList

#-----------------------------------------------------------------------------
def getScrabbleLetterScore(letter):
  if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u' or letter=='n' or letter=='r' or letter=='t' or letter=='l' or letter=='s':
    return 1
  elif letter=='d' or letter=='g':
    return 2
  elif letter=='b' or letter=='c' or letter=='m' or letter=='p':
    return 3
  elif letter=='f' or letter=='h' or letter=='v' or letter=='w' or letter=='y':
    return 4
  elif letter=='k':
    return 5
  elif letter=='j' or letter=='x':
    return 8
  elif letter=='q' or letter=='z':
    return 10
  else:
    return 0

#-----------------------------------------------------------------------------
def getScrabbleWordScore(word):
  score=0
  for letter in word:
    score+=getScrabbleLetterScore(letter)
  return score

#-----------------------------------------------------------------------------
def getTotalScore(wordList):
  totalScore=0
  for word in wordList:
    totalScore+=getScrabbleWordScore(word)
  return totalScore

#-----------------------------------------------------------------------------
def getDictOfScores(wordList):
  dic={}
  new_list=[]
  for word in wordList:    
    score=getScrabbleWordScore(word)
    if score in dic:
      dic[score]+=1
    elif score not in dic:
      dic[score]=1
  keymax=max(dic, key=dic.get)
  for word in wordList:
    if getScrabbleWordScore(word)==keymax:
      new_list.append(word)
  return new_list

#-----------------------------------------------------------------------------
wordList = readWords('/Users/SahilRajapkar/Desktop/words.txt') 
mySevenLetterWord='ferrari'

#-----------------------------------------------------------------------------
wordLists = []
for x in wordList:
  counter = 0
  for y in x:
    if y in mySevenLetterWord:
      counter = counter + 1
  if counter >= 2:
    wordLists.append(x)
print(getTotalScore(wordLists))

#-----------------------------------------------------------------------------
majorityList = getDictOfScores(wordList)
wordListss = []
for z in majorityList:
  counter1 = 0
  for a in z:
    if a in mySevenLetterWord:
      counter1 = counter1 + 1
  if counter1 >= len(mySevenLetterWord):
    wordListss.append(x)
print(getTotalScore(wordListss))
