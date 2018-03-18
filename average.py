class Average:

    def string_to_num_array(self, array):
        stringsArray = array.split(",")
        elementos = list()
        for i in stringsArray:
            if i != '':
                elementos.append(int(i))
        return elementos

    def arrayNumbers(self, array):
           response = ['length', 'min', 'max', 'average']
           elementos = Average().string_to_num_array(array)
           if len(array) == 0:
               response[0]=0
               response[1] = None
           else:
               response[0]=len(elementos)
           if len(elementos) == 1 and len(array)>0:
               response[1] = int(elementos[0])
           elif len(elementos) == 2:
               response[1] = min(elementos)
           elif len(elementos) > 2:
               response[1] = min(elementos)
           return response


