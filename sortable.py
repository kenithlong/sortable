import json

class Product(object):
   def __init__(self, productName, manufacture, model, announceDate, family=None):
      self.productName = productName
      self.manufacture = manufacture
      self.model = model


def buildProductMap(productFile):
   """
   Read in the product file and create a mapping
   based on the manufacturer. Potentially dangerous
   assumption of converting to lower, case could
   be important, also assuming products fit in 
   memory...

   returns {"manufacturer" : listOfProducts}   
   """
   productMap = {}
   with open(productFile, 'r') as jsonData: 
      for line in jsonData:
         line = line.rstrip("\r\n")
         singleEntry = json.loads(line)
         #to lower to avoid collisions
         currentManufacturer = singleEntry["manufacturer"].lower()
         if (currentManufacturer not in productMap):
            productMap[currentManufacturer] = [singleEntry]
         else:
            productMap[currentManufacturer].append(singleEntry)

   return productMap


def main():
   print(buildProductMap("products.json"))



if __name__ == "__main__":
   main()

