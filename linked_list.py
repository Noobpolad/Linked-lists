import csv
import time

class Airport:

	def __init__(self, code):
		self.setCode(code)
		self.setNext(None)

	def setCode(self, code):
		self._code = code

	def getCode(self):
		return self._code

	def setNext(self, next):
		self._next = next

	def getNext(self):
		return self._next

class LinkedList:

	def __init__(self):
		self._head = None
		self._tail = None
		self._changedTail = None

	def add(self, airportCode):
		newest = Airport(airportCode)
		newest.setNext(self._head)
		if self._head == None:
			self._tail = newest
		self._head = newest

	def display(self):
		iterator = self._head
		while iterator != None:
			print(iterator.getCode())
			iterator = iterator.getNext()

	def bubbleSort(self):
		stop = self._tail
		nextStop = None
		while stop != self._head:
			iterator = self._head
			while iterator != stop:
				if iterator.getNext() == stop:
					nextStop = iterator
				if iterator.getCode() > iterator.getNext().getCode():
					tmp = iterator.getCode()
					iterator.setCode(iterator.getNext().getCode()) 
					iterator.getNext().setCode(tmp)

				iterator = iterator.getNext()

			stop = nextStop

	def remove(self,element):
		value = self._head
		if value.getCode() == element:
			self._head = value.getNext()

		while value != self._tail:
			if value.getNext().getCode() == element and value.getNext() != self._tail:
				value = value.setNext(value.getNext().getNext())
				break
			
			elif value.getNext().getCode() == element and value.getNext() == self._tail:
				self._tail = value
				value = value.setNext(None)
				break
				
			value = value.getNext()					

list = LinkedList()

with open('airport-codes.csv',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       list.add(row['ident'])

start = time.time()       
list.bubbleSort()
end = time.time()

list.display()

print('{:.2f}'.format(end - start))
