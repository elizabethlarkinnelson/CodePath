# Prework for CodePath
# InterviewBit Levels 1-5


#Level 1 - AMORTIZED2
#Solution:
# O(n) - There is one for loop.

#Level2 - PRETTYPRINT
#Solution:

 def prettyPrint(self, A):
        
        rectangle = []
        
        for i in range(1,A+1):
            if i == 1:
                rectangle.append([1])
            else:
                for j in range(len(rectangle)):
                    rectangle[j].insert(0, i)
                    rectangle[j].append( i)
                num = len(rectangle[len(rectangle)/2])
                rectangle.insert(0,[i] * num)
                rectangle.append([i] * num)
                
        return rectangle


#Level3 - Kth SMALLEST
#Solution:
#Note: This satisfies not modifying original array, but uses O(n) space for the copied array.
 def kthsmallest(self, A, B):
        
        sorted_A = sorted(A)
        
        return sorted_A[B-1]


#Level4 - SUBTRACT
#Solution:

def subtract(self, A):

        counter = 0
    
        a = A
        
        while a is not None:
            a = a.next
            counter += 1
            #We now have the length of the list
            
        half = counter / 2
        current = 1
        length = counter
        node = A
        play = A
        
        while current <= half:
            for num in range(length-1):
                play = play.next
            node.val = play.val - node.val
            node = node.next
            play = node
            current += 1
            length -= 2
            
        return A


#Level5 - LONGEST CONSECUTIVE SEQUENCE
#Solution:

def longestConsecutive(self, A):
        
        if len(A) == 1:
            return 1

        max_num = 1
        unique_num = set()
        
        current = []
        
        for i in A:
            unique_num.add(i)
            
        for j in range(len(A)):
            
            if (A[j]-1) not in unique_num:
                
                if A[j] + 1 in unique_num:
                    
                    current.append(A[j])
                    current.append(A[j]+1)
                    num = A[j] + 2
                    
                    while num in unique_num:
                        current.append(num)
                        num += 1
                        
                    if len(current) > max_num:
                        max_num = len(current)
                        
                    current = []
                    
        return max_num
