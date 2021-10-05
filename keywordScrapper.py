
#Simple scrapper for a specific task. Used to grab the department chair of a University subject.
#But can search for any keyword, for my purposes it was chair, department head...

from bs4 import BeautifulSoup
from bs4.element import PageElement
import requests
import re

goFlag = True
rFlag = False
links = []

#Example links I used
#page = requests.get("https://brocku.ca/humanities/english-language-and-literature/faculty/")
#page2 = requests.get("https://algomau.ca/academics/programs/english/")
#page3 = requests.get("https://english.acadiau.ca/faculty-staff.html")


while True:

   if goFlag == True:
      print("Enter a link to scrape. Or enter q to exit.")
      print("If no name was returned try using the -r flag.")
      cmd = input().split()

      if cmd[0] == 'q':
         exit()
      if len(cmd) > 1:
         if cmd[1] == '-r':
            rFlag = True
      else:
         rFlag = False
      
      try:
         page = requests.get(cmd[0])
      except:
         print("Bad Link")
         continue

      soup = BeautifulSoup(page.content ,'html.parser') #parse html
      print('\n')
      print("Enter keyword word to search for")
      keyword = input()
      result = soup.find_all(string=re.compile(keyword, re.I)) #search for keyword
      if not result:
         print("No results found, try a different keyword?")
      for i in result:
         if rFlag == True:
            print(i.parent.parent.get_text())
            print("\n")
         else: 
            print(i.parent.get_text())
            print("\n")

'''
      if not result:
         result = soup.find_all(string=re.compile("Head"))
         for i in result:
            try:
               links.append(i.parent.findChild("a")['href'])
            except:
               pass
         if rFlag == True:
            print(i.parent.parent.get_text())
            print("\n")
         else: 
            print(i.parent.get_text())
            print("\n")
         if links:
            newLink = cmd[0].split('/')[:-1]
            for link in links:
               link = '/'.join(newLink)+'/'+link
               print(link)
            '''