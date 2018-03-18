class Average:
   def arrayNumbers(self, array):
       elementos = array.split(",")
       if len(array) == 0 :
           return 0
       else:
           return len(elementos)