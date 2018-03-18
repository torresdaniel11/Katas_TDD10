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
               response[2] = None
           else:
               response[0]=len(elementos)
               response[1] = min(elementos)
           if len(elementos) == 1:
               response[2] = max(elementos)
           elif len(elementos) == 2:
               response[2] = max(elementos)
           elif len(elementos) > 2:
               response[2] = max(elementos)
           return response


