#lex_auth_0127382206342184961397

def check_anagram(str1,str2):
   str1 = list(str1.lower())
   str2 = list(str2.lower())

   if sorted(str1) == sorted(str2):
        for i in range(len(str1)):
           if str1[i].lower() == str2[i].lower():
               return False
        return True 
   else:
        return False


print(check_anagram("tea","eat"))