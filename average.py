class Average:
   def arrayNumbers(self, array):
       elementos = array.split(",")
       if len(array) == 0 :
           return 0
       elif len(elementos)==1:
           return 1
       elif len(elementos)==2:
           return 2
       else:
           return len(elementos)