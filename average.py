class Average:
   def arrayNumbers(self, array):
       response = ['length', 'min', 'max', 'average']
       elementos = array.split(",")
       if len(array) == 0:
           response[0]=0
       else:
           response[0]=len(elementos)
       return response