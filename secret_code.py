# wap to translate a message into secret code language.
# rules are :-
# for coding
# if the word contain atleast 3 letter , remove the 1st letter and append it at the end . now append three random characters at the starting and the end
# else :
#     simply reverse the string

# decoding 
# if : the word contain less than 3 characters,reverse it.
# else : remove 3 characters from start and end. now remove the last letter and append it to the beginning.

import random
message=input("enter ur message >> ")
words=message.split()
print("press 1 for coding or 0 for decode")
coding = int(input("What do u want to do (encode / decode) >> "))

# for encode
if(coding==1):
    new_words=[]
    for word in words:
        if(len(word)>=3):
            r1=chr(random.randint(ord('e'),ord('v')))
            r2=chr(random.randint(ord('a'),ord('z')))
            for i in range(1,3):
                r1=r1+chr(random.randint(ord('d'),ord('s')))
                r2=r2+chr(random.randint(ord('f'),ord('z')))
            new_mess=r1+ word[1:] + word[0] + r2
            new_words.append(new_mess)
        else:
            rev_str=""
            count=len(word) 
            while (count>0 and count <=2):
                rev_str += word[count-1]
                count=count-1
            new_words.append(rev_str)
    print(" ".join(new_words))
  
# for decode   
else:
    new_words=[]
    for word in words:
        if(len(word)>=3):
            new_mess = word[3:-3]
            new_mess = new_mess[-1] + new_mess[:-1]
            new_words.append(new_mess)
        else:
            rev_str=""
            count=len(word) 
            while (count>0 and count<=2):
                rev_str += word[count-1]
                count = count-1
            new_words.append(rev_str)
    print(" ".join(new_words))
        
# def rev_str(str):
#     rev_str=""
#     for i in str:
#         rev_str=i+rev_str
#     return(rev_str)


# print(message[::-1])   