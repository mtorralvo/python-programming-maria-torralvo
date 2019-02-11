#!usr/bin/python3

def smith_waterman (seqA, seqB, match, mismatch, gap):

	'''Given two sequences and values for match, mismatch and gap penalty, returns the scores matrix, 
	   direction matrix and highest scored cell following the Smith-Waterman algorithm.'''

	seqA = '0' + seqA; seqB = '0' +seqB #Adding '0' at the beggining of the sequences for index purposes
	match = int(match); mismatch = int(mismatch); gap = int(gap)

	#Inizialization of matrices: S = scores and D = directions	
	S = [[]]; D = [[]] 
	
	rows = len(seqB); cols = len(seqA) 

	S = [[0 for col in range(cols)] for row in range(rows)]
	D = [['0' for col in range(cols)] for row in range(rows)]

	print(S,D)

	#Iterarion
	for i in range(1,rows):
		for j in range(1,cols):

			#Compute all possible values
			if seqA[j] == seqB[i]: 
				dia = S[i-1][j-1] + match
			else: 
				dia = S[i-1][j-1] + mismatch
			ver = S[i-1][j] + gap
			hor = S[i][j-1] + gap

			S[i][j] = max(dia,ver,hor,0) #Comple scores matrix with max values

			
			#Complete directions matrix
			if S[i][j] == dia:
				D[i][j] = 'D'
			elif S[i][j] == ver:
				D[i][j] = 'V'
			elif S[i][j] == hor:
				D[i][j] = 'H'

	#Looking for the highest score
	highest_score = 0; r = 0; c = 0
	
	for i in range(rows):
		for j in range(cols):
			
			if S[i][j] >= highest_score:
				highest_score = S[i][j]
				r = i; c = j

	#end function
	return (S,D,r,c)

#Collecting input
print("Give me to sequences to align:")
input_seqA = input("Sequence A:")
input_seqB = input("Sequence B:")
print("Indicate values for:")
input_match = input("Match:")
input_mis = input("Mismatch:")
input_gap = input("Gap:")

#Execute function
final_S,final_D,final_r,final_c = smith_waterman(input_seqA,input_seqB,input_match,input_mis,input_gap)

#Give results
print("This is the scores matrix:", final_S)
print(final_S)
print("This is the distances matrix:", final_D)
print("The cell with the highest score is in row", final_r,"and in column", final_c)









