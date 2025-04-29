class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self,value):
        if self.__celsius >= -273.15:
            self.__celsius = value
        else:
            raise ValueError("Temperature can't go below absolute zero")
        
    @property
    def fahrenheit(self):
        return self.__celsius * 9/5 + 32