fruits=["lemon","honeyberry","grapefruit","apple","banana","mango","strawberry","grape","pineapple","blueberry","blackberry","pomegranate","jackfruit","guava","raspberry","dragonfruit","starfruit","cherry","avocado","orange","cranberry","greenapples","papaya","kiwi","custardapple","watermelon","lychee","pear","date","ackee","apricot","amla","boysenberry","barberry","bilberry","coconut","cashewapple","elephantapple"] 
print(" Let's play  Hangman game !!!")
word=[]
print("you have only 6 lives so try to guess the word within 6 attempts ! Good luck!!")
import random
fruit=random.choice( fruits)
for letters in fruit:
        word.append('_')
      
number_of_wrong_attempts=0
guessed_letters=[]

while(number_of_wrong_attempts<6) :
    guess=input("guess a letter !!").lower()
    if(len(guess))!=1:
       print("please enter only one letter")
       continue
    if guess in guessed_letters:
        print(" you already guessed this letter")
        continue
    guessed_letters.append(guess)

    if(guess in  fruit):
         for i in range(len(fruit)):
                 if fruit[i]==guess :   
                         word[i]=guess
         print(word)                
         
         
                     
    else:
        
        print(word)
        print(f" you guessed {guess} is  wrong letter \n you lose a life")
        number_of_wrong_attempts=number_of_wrong_attempts+1
        print(f"you have only {6- number_of_wrong_attempts} lives left")
       
  
    if "_" not in  word:
        print(f"you win\n game is over\n the word is {fruit}")
        break      
    
    print( )           
    if(number_of_wrong_attempts== 1):
                     
            for r in range(0,12):
              for c in range(0,12):
                  if(r==2 and c==2 or r==2 and c==3 or r==3 and c==1 or r==3 and c==4  or r==4  and c==1  or r==4 and c==4 or r==5 and c==2 or r==5 and c==3 or  r==1 and c==2 or r==2 and c==6 or r==3 and c==6 or r==4 and c==6 or r==4 and c==6 or r==5 and c==6 or r==6 and c==6 or r==7 and c==6 or r==8 and c==6 or r==9 and c==6 or r==10 and c==6 or r==0 and c==0  or r==0 and c==1 or r==0 and c==2 or  r==0 and c==3 or r==0 and c==4 or r==0 and c==5 or r==0 and c==6 or r==1 and c==6):
                      print("*",end=" ")
                  else:
                       print(" ",end=" ")   
              print()
    
    if(number_of_wrong_attempts== 2):
         for r in range(0,12):  
            for c in range(0,12):
               if(r==2 and c==2 or r==2 and c==3 or r==3 and c==1 or r==3 and c==4  or r==4  and c==1  or r==4 and c==4 or r==5 and c==2 or r==5 and c==3 or  r==6 and c==2 or r==7 and c==2 or r==8 and c==2 or r==9 and c==2 or r==10 and c==2 or r==11 and c==2   or r==1 and c==2 or r==2 and c==6 or r==3 and c==6 or r==4 and c==6 or r==4 and c==6 or r==5 and c==6 or r==6 and c==6 or r==7 and c==6 or r==8 and c==6 or r==9 and c==6 or r==10 and c==6 or r==11 and c==6 or r==0 and c==0  or r==0 and c==1 or r==0 and c==2 or  r==0 and c==3 or r==0 and c==4 or r==0 and c==5 or r==0 and c==6 or r==1 and c==6):
                     print("*",end=" ")
               else:
                     print(" ",end=" ")   
            print()  
            
    if(number_of_wrong_attempts== 3):     
        for r in range(0,12):  
            for c in range(0,12):
               if(r==2 and c==2 or r==2 and c==3 or r==3 and c==1 or r==3 and c==4  or r==4  and c==1  or r==4 and c==4 or r==5 and c==2 or r==5 and c==3 or  r==6 and c==2 or r==7 and c==2 or r==8 and c==2 or r==9 and c==2 or r==10 and c==2 or r==11 and c==2   or r==1 and c==2 or r==2 and c==6 or r==3 and c==6 or r==4 and c==6 or r==4 and c==6 or r==5 and c==6 or r==6 and c==6 or r==7 and c==6 or r==8 and c==6 or r==9 and c==6 or r==10 and c==6 or r==11 and c==6 or r==0 and c==0  or r==0 and c==1 or r==0 and c==2 or  r==0 and c==3 or r==0 and c==4 or r==0 and c==5 or r==0 and c==6 or r==1 and c==6 or r==7 and c==1 or r==8 and c==0):
                     print("*",end=" ")
               else:
                     print(" ",end=" ")   
            print()

        
    if(number_of_wrong_attempts== 4):
        for r in range(0,12):  
            for c in range(0,12):
               if(r==2 and c==2 or r==2 and c==3 or r==3 and c==1 or r==3 and c==4  or r==4  and c==1  or r==4 and c==4 or r==5 and c==2 or r==5 and c==3 or  r==6 and c==2  or r==7 and c==2 or r==8 and c==2 or r==9 and c==2 or r==10 and c==2 or r==11 and c==2  or r==1 and c==2 or r==2 and c==6 or r==3 and c==6 or r==4 and c==6 or r==4 and c==6 or r==5 and c==6 or r==6 and c==6 or r==7 and c==6 or r==8 and c==6 or r==9 and c==6 or r==10 and c==6 or r==11 and c==6 or r==0 and c==0  or r==0 and c==1 or r==0 and c==2 or  r==0 and c==3 or r==0 and c==4 or r==0 and c==5 or r==0 and c==6 or r==1 and c==6 or r==7 and c==1 or r==8 and c==0 or r==7 and c==3 or r==8 and c==4):
                     print("*",end=" ")
               else:
                     print(" ",end=" ")   
            print()  
           
    if(number_of_wrong_attempts== 5):
         for r in range(0,12):  
            for c in range(0,12):
               if(r==2 and c==2 or r==2 and c==3 or r==3 and c==1 or r==3 and c==4  or r==4  and c==1  or r==4 and c==4 or r==5 and c==2 or r==5 and c==3 or  r==6 and c==2   or  r==7 and c==2 or r==8 and c==2 or r==9 and c==2 or r==10 and c==2 or r==11 and c==2 or r==1 and c==2 or r==2 and c==6 or r==3 and c==6 or r==4 and c==6 or r==4 and c==6 or r==5 and c==6 or r==6 and c==6 or r==7 and c==6 or r==8 and c==6 or r==9 and c==6 or r==10 and c==6 or r==11 and c==6 or r==0 and c==0  or r==0 and c==1 or r==0 and c==2 or  r==0 and c==3 or r==0 and c==4 or r==0 and c==5 or r==0 and c==6 or r==1 and c==6 or r==7 and c==1 or r==8 and c==0 or r==7 and c==3 or r==8 and c==4 or r==10 and c==1 or r==11 and c==0):
                     print("*",end=" ")
               else:
                      print(" ",end=" ")   
            print()  
            
    if(number_of_wrong_attempts== 6):
        for r in range(0,12):  
            for c in range(0,12):
                  if(r==2 and c==2 or r==2 and c==3 or r==3 and c==1 or r==3 and c==4  or r==4  and c==1  or r==4 and c==4 or r==5 and c==2 or r==5 and c==3 or  r==6 and c==2   or  r==7 and c==2 or r==8 and c==2 or r==9 and c==2 or r==10 and c==2 or r==11 and c==2 or r==1 and c==2 or r==2 and c==6 or r==3 and c==6 or r==4 and c==6 or r==4 and c==6 or r==5 and c==6 or r==6 and c==6 or r==7 and c==6 or r==8 and c==6 or r==9 and c==6 or r==10 and c==6 or r==11 and c==6 or r==0 and c==0  or r==0 and c==1 or r==0 and c==2 or  r==0 and c==3 or r==0 and c==4 or r==0 and c==5 or r==0 and c==6 or r==1 and c==6 or r==7 and c==1 or r==8 and c==0 or r==7 and c==3 or r==8 and c==4 or r==10 and c==1 or r==11 and c==0 or r== 10 and c==3 or r==11 and c==4):
                         print("*",end=" ")
                  else:
                          print(" ",end=" ")   
            print()       
    if(number_of_wrong_attempts== 6):
        print(f" you lose the game\n word is {fruit}")                                                 

                        
                
              
   
    

