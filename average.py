class Average:
   def arrayNumbers(self, array):
       response = ['length', 'min', 'max', 'average']
       elementos = array.split(",")
       if len(array) == 0:
           response[0]=0
           response[1] = None
       else:
           response[0]=len(elementos)
       if len(elementos) == 1 and len(array)>0:
           response[1] = int(elementos[0])
       return response