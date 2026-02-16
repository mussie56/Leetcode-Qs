class Solution:
    def reverseBits(self, n: int) -> int:
        binary = [0]*32
        i = 0
        while n > 0:
            binary[i]=(n%2)
            n//=2
            i+=1
            
        ans = 0
        binary.reverse()
        
        for i in range(len(binary)):
            if binary[i] == 1:
                ans+=(2**i)


        return ans