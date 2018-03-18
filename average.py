class Average:

    def string_to_num_array(self, array):
        stringsArray = array.split(",")
        elementos = list()
        for i in stringsArray:
            if i != '':
                elementos.append(int(i))
        return elementos

    def mean(self, numbers):
        return float(sum(numbers)) / max(len(numbers), 1)

    def arrayNumbers(self, array):
           elementos = Average().string_to_num_array(array)
           if len(array) == 0:
               return [0, None, None, None]
           else:
               return [len(elementos), min(elementos), max(elementos), Average().mean(elementos)]