class DistanceConversion:
  def __init__(self, distance):
    self.__distance = distance

  def __convert_to_Centimeter(self):
    return self.__distance *100

  def __convert_to_Kilometer(self):
    return self.__distance /1000

  def __convert_to_inches(self):
    return self.__distance *39.37

  def display_convertion(self):
    print(f'{self.__distance}meter is {self.__convert_to_Centimeter()} centimeter')
    print(f'{self.__distance}meter is {self.__convert_to_Kilometer()} kilometer')
    print(f'{self.__distance}meter is {self.__convert_to_inches()} inches')

distance_in_meter = float(input("ENTER A DISTANCE IN METER:"))
conversion = DistanceConversion(distance_in_meter)
conversion.display_convertion()

