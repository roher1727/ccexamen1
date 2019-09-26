import queue
from random import randint
import multiprocessing as mp
import time 

class filosofo():

	def __init__(self, nombre, tiempo):
		self.nombre = nombre
		self.tiempo = tiempo
		self.termino = False

	def comer(cfilosofos_conc):
	#	------Zona Critica------

		if self.tiempo != 0:
			self.tiempo -= 1
			print(filosofo.tiempo)
		else:
			print("\nTermino de comer el {}".format(self.nombre))
			cfilosofos_conc.value -= 1
			self.termino = True


def filosofos(cantidad_filosofos):
	tenedores = cantidad_filosofos//2

#-----------------------Concurrente------------------------

#	------------Semaforo------------
	cfilosofos_conc = mp.Value('i', cantidad_filosofos)

	filosofos_conc = [filosofo("Filosofo {}".format(k) ,randint(1, 20)) for k in range(cantidad_filosofos)]
	
	pool = mp.Pool(tenedores)	

	while cfilosofos_conc.value > 0:
		pool.map(comer, (filosofos_conc))

		
#---------------------------Secuencial---------------------------

	filosofos = queue.Queue()
	comensales = queue.Queue()
	[filosofos.put(filosofo("Filosofo {}".format(k) ,randint(1, 20))) for k in range(cantidad_filosofos)]


	while cantidad_filosofos > 0:


		print("\n --- Iteracion --- \n")

		for i in range(tenedores):

#		Problema de implementacion
			if filosofos.qsize() == 0:
				break

			temp = filosofos.get()

			print(temp.nombre," con tiempo:  ",temp.tiempo)

			if temp.tiempo != 0:
				temp.tiempo -= 1
				comensales.put(temp)
			else:
				print("\nTermino de comer el {}".format(temp.nombre))
				cantidad_filosofos -= 1

		

		for j in range(comensales.qsize()):
			filosofos.put(comensales.get())


if __name__ == "__main__":
	filosofos(5)

	
