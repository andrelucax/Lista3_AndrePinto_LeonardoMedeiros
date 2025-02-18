import json
import matplotlib
import random
import time

from matplotlib import pyplot

class BloodMessage:
	Owner = ''
	AreaNumber = 0
	WorldNumber = 0
	XCoord = 0
	YCoord = 0
	ZCoord = 0
	Angle = 0
	TextID1 = 0
	TextID2 = 0
	Text = ''
	PositiveRatings = 0
	NegativeRatings = 0
	UnixTime = ''
	TimeString = ''
	
	
	def __init__(self, Owner, WorldNumber, XCoord, YCoord, ZCoord, Text):
		self.Owner = Owner
		self.WorldNumber = WorldNumber
		self.XCoord = XCoord
		self.YCoord = YCoord
		self.ZCoord = ZCoord
		self.Text = Text
	
	def __str__(self):
		return self.Text
		
	def __lt__(self, other):
		if(self.WorldNumber == other.WorldNumber):
			return self.Owner < other.Owner
		return self.WorldNumber < other.WorldNumber
		
	def __le__(self, other):
		if(self.WorldNumber == other.WorldNumber):
			return self.Owner <= other.Owner
		return self.WorldNumber <= other.WorldNumber

file = open("BloodMessages.json", "r")
jsondata = file.read()

jdata = json.loads(jsondata)

data = jdata['BloodMessages']  # Lista de dicionarios de BloodMessages
messages = []
for message in data:
	messages.append(BloodMessage(message['Owner'], message['WorldNumber'], message['XCoord'], message['YCoord'], message['ZCoord'], message['Text']))

mergeIteration = 0
def mergeSort(arr): 
	global mergeIteration
	if len(arr) > 1: 
		mid = len(arr)//2 
		L = arr[:mid] 
		R = arr[mid:]
  
		mergeSort(L) 
		mergeSort(R) 
  
		i = j = k = 0
          
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i]
				mergeIteration+=1
				i+=1
			else: 
				arr[k] = R[j]
				mergeIteration+=1
				j+=1
			k+=1
          
		while i < len(L): 
			arr[k] = L[i]
			mergeIteration+=1
			i+=1
			k+=1
          
		while j < len(R): 
			arr[k] = R[j]
			mergeIteration+=1
			j+=1
			k+=1
			

quickIteration = 0
def partition(arr,low,high): 
	global quickIteration
	i = (low-1)
	pivot = arr[high]    
	for j in range(low , high): 
		if arr[j] <= pivot: 
			i = i+1 
			arr[i],arr[j] = arr[j],arr[i] 
			quickIteration+=2
	arr[i+1],arr[high] = arr[high],arr[i+1]
	quickIteration+=2
	return (i+1) 


def quickSort(arr,low,high): 		
	if low < high: 
		pi = partition(arr,low,high) 

		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 
		
print("Foram lidos: " + str(len(data)) + " Blood Messages")
arr1 = messages
begin = time.time()
quickSort(arr1, 0, len(arr1)-1)
end = time.time()
quick_time = end - begin

arr2 = messages
begin = time.time()
mergeSort(arr2)
end = time.time()
merge_time = end - begin

print('O Merge sort, algoritmo estavel, demorou {} segundos, tendo feito {} atribuicoes e o Quick sort, instavel, demorou {} segundos, tendo feito {} atribuicoes'.format(merge_time, mergeIteration, quick_time, quickIteration))

Messages_per_world_X = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [],
					  6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 
					  12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: []}
					  
Messages_per_world_Y = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [],
					  6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 
					  12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: []}
					  
for each in arr1:
	Messages_per_world_X[each.WorldNumber].append(each.XCoord)
	Messages_per_world_Y[each.WorldNumber].append(each.YCoord)


# Ignorando os mundos [1:9] pois nao possuem mensagens
for i in range(9):
	fig, ax = pyplot.subplots()

	pyplot.xlabel('Position X')
	pyplot.ylabel('Position Y')
	ax.scatter(Messages_per_world_X[i+10], Messages_per_world_Y[i+10], label='World: '+str(i+10))
	
	pyplot.legend()

	pyplot.show()
	
	
