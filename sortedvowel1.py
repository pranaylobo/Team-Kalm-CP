class Solution:
    def countVowelStrings(self, n: int) -> int:
        # print(("a" + "a")*2)
        
        arr=["a","e","i","o","u"]
        
        vowels={}
        n=n-1
        
        for index,number in enumerate(arr):
            
            con=number *n
            
            vowels.update({con:arr})
            
            
        print(vowels)
            
            
            

        
        
        
    
            
        
        

        
        
