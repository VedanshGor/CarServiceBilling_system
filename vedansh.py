
def printSubArray(Array):


	for i in range(len(Array)):  #intitating from starting Element , and adding the other rest Elements into it  
		TargetSum = 0            #by default we will start from nothing and later we will add the array Elements one by one and later we are gonna 
								#check whether it became 0 or not.
		
		for j in range(i, len(Array)):   #this for loop i used for traversing the rest Array Elements and adding them to my TargetSum AKA "start"
		
			TargetSum =TargetSum + Array[j] 		# adding the traversed array Element (in one pass ) and add it to the TargetSum AKA "start"
		
			if TargetSum == 0:						#checking if it gives me total 0 or not
				print('SubArray from', (Array[i]))			# if it gives 0 then print those Element, NOTE : here i didn't used a loop to print all Element
				print('to the index ', Array[j])									# as it gives a O(n**3) solution but i did alternative idea for that to describe what is asked


if __name__ == '__main__':

	Array = [-4,1,3,-2,-1]
	printSubArray(Array)
