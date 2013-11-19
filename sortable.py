import json

class Product(object):
   def __init__(self, productName, manufacture, model, announceDate, family=None):
      self.productName = productName
      self.manufacture = manufacture
      self.model = model


def main():
   #todo actually solve the problem eventually
   with open('products.json', 'r') as jsonData: 
      for line in jsonData:
         line = line.rstrip("\r\n")
         print(json.loads(line))
         # try: man = line["manufacture"] 
         #if man in bigDictionary
         # append to the thinger?

   #seems to lend itself to a dictionary, key == manufacture, value list of products

if __name__ == "__main__":
   main()

