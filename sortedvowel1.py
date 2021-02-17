from itertools import permutations
from itertools import combinations
class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        
    
        n=n-1
        vowels={}
  
        # Print the obtained permutations  
         
        
     
        comb = combinations(["a","e","i","o","u"], n) 
        arr=["a","e","i","o","u"]
        
            
        for index,number in enumerate(list(comb)): 

            temp=list[number]

            vowels.update({temp:arr[index:]})
            
        print(vowels)
 
        
            
