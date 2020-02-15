import random
import time
import sys

def isSorted(arr):
	for i in range(0,len(arr)-1):
		if arr[i]>arr[i+1]:
			return False
	return True

def bubbleSort(arr):
	for i in range(len(arr)-1,-1,-1):
		flag=0
		for j in range(0,i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
				flag=1
		if flag==0:
			break

def selectionSort(arr):
	for i in range(0,len(arr)):
		minIndex=i
		for j in range(i+1,len(arr)):
			if arr[minIndex]>arr[j]:
				minIndex=j
		arr[minIndex],arr[i]=arr[i],arr[minIndex]

def insertionSort(arr):
	for i in range(1,len(arr)):
		j=i-1
		while j>=0 and arr[j]>arr[i]:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=arr[i]

def partition(arr,low,high):
	pivot=arr[high]
	j=low-1
	for i in range(low,high):
		if arr[i]<pivot:
			j+=1
			arr[i],arr[j]=arr[j],arr[i]
	arr[high],arr[j+1]=arr[j+1],arr[high]
	return j+1

def quickSort(arr,low,high):
	if low<high:
		r = partition(arr,low,high)
		quickSort(arr,low,r-1)
		quickSort(arr,r+1,high)


def mergerSort(arr):
	if len(arr)>1:
		mid = len(arr)//2
		L=arr[:mid]
		R=arr[mid:]
		mergerSort(L)
		mergerSort(R)
		i=j=k=0
		while i<len(L) and j<len(R):
			if L[i]>R[j]:
				arr[k]=L[i]
				i+=1
				k+=1
			else:
				arr[k]=R[j]
				j+=1
				k+=1
		while i<len(L):
			arr[k]=arr[i]
			i+=1
			k+=1
		while j<len(R):
			arr[k]=arr[j]
			j+=1
			k+=1

def heapify(arr,i,heapSize):
	l=2*i+1
	r=2*i+2
	largest=i
	if l<heapSize and arr[l]>arr[i]:
		largest=l
	if r<heapSize and arr[r]>arr[largest]:
		largest=r
	if largest!=i:
		arr[i],arr[largest]=arr[largest],arr[i]
		heapify(arr,largest,heapSize)
def buildHeap(arr):
	for i in range(len(arr)//2,-1,-1):
		heapify(arr,i,len(arr))
def heapSort(arr):
	buildHeap(arr)
	for i in range(len(arr)-1,-1,-1):
		arr[0],arr[i]=arr[i],arr[0]
		heapify(arr,0,i)

def printTimes(sort_time):
	print('Bubble sort: ',sort_time[0]/3,'ms')
	print('Selection sort: ',sort_time[1]/3,'ms')
	print('Insertion sort: ',sort_time[2]/3,'ms')
	print('Quick sort: ',sort_time[3]/3,'ms')
	print('Merge sort: ',sort_time[4]/3,'ms')
	print('Heap sort: ',sort_time[5]/3,'ms')
	print('Tim sort: ',sort_time[6]/3,'ms')

def runAllSort(arr,sort_time):
	start_time = round(time.time() * 1000)
	bubbleSort(arr[:])
	end_time=round(time.time() * 1000)
	sort_time[0]+=(end_time-start_time)

	start_time = round(time.time() * 1000)
	selectionSort(arr[:])
	end_time=round(time.time() * 1000)
	sort_time[1]+=(end_time-start_time)

	start_time = round(time.time() * 1000)
	insertionSort(arr[:])
	end_time=round(time.time() * 1000)
	sort_time[2]+=(end_time-start_time)

	start_time = round(time.time() * 1000)
	quickSort(arr[:],0,len(arr)-1)
	end_time=round(time.time() * 1000)
	sort_time[3]+=(end_time-start_time)

	start_time = round(time.time() * 1000)
	mergerSort(arr[:])
	end_time=round(time.time() * 1000)
	sort_time[4]+=(end_time-start_time)

	start_time = round(time.time() * 1000)
	heapSort(arr[:])
	end_time=round(time.time() * 1000)
	sort_time[5]+=(end_time-start_time)

	start_time = round(time.time() * 1000)
	arr.sort()
	end_time=round(time.time() * 1000)
	sort_time[6]+=(end_time-start_time)

def demo(choice):
	sort_time=[0,0,0,0,0,0,0]
	size=100
	
	while size<100001:
		if choice==1:
			print('\nFor sorted array with size :',size,'\n')
		elif choice==2:
			print('\nFor reversly sorted array with size :',size,'\n')
		else:
			print('\nFor unsorted array with size :',size,'\n')

		for j in range(0,3):
			arr = [random.randint(0,10000) for i in range(size)]
			if choice==1:
				arr.sort()
			elif choice==2:
				arr.sort(reverse=True)
			runAllSort(arr[:],sort_time)

		size*=10
		printTimes(sort_time)
sys.setrecursionlimit(100000)
demo(1) #Sorted
demo(2) #Reversly Sorted
demo(3) #Unsorted