import re
import random


class Product:
    def __init__(self,name,categoryName,prodCode,basicPrice,taxPercent,discount,mrp):
        self.name = name
        self.categoryName = categoryName
        self.basicPrice  = basicPrice
        self.taxPercent = taxPercent
        self.discount = discount
        self.mrp = mrp


def productCodeGenerator(name,categoryName):
    prodCode = ""
    prodCode = prodCode + categoryName[0:2] + name[0:2]
  
    keyString = ""
    for i in dict:
        keyString += i
    count = len(re.findall(prodCode,keyString))
    prodCode += str(count) + str(random.randint(100,999))
    return prodCode


def taxCalculator(price, taxCriteria, taxpercent):
    if taxCriteria == 1:
        return price + (price * taxpercent/100)
    else:
        return price - (price * taxpercent/100)


def enterDetails():
    name = input("Enter the name of the product: ")

    
    categoryName = input("Enter category of the product: ")
    
    prodCode = productCodeGenerator(name,categoryName)
    
    price = int(input("Enter the price of the product: "))
    taxPercent = int(input("Enter tax perentage: "))
    taxCriteria = int(input("Give type of price entered\n1 -> tax extra\n2 -> includes tax\n>"))
    if taxCriteria == 1:
        basePrice = price
        mrp = taxCalculator(price,taxCriteria,taxPercent)
    else:
        mrp = price
        basePrice = taxCalculator(price,taxCriteria,taxPercent)
    taxAmount = mrp - basePrice
    
    discountType = int(input("Enter discount type:\n1 -> Percentage\n2 -> Amount\n>"))
    if discountType == 1:
        discountPercent = int(input("Enter percentage of discount: "))
        discountAmount = (discountPercent/100) * mrp
    else:
        discountAmount = int(input("Enter amount of discount: "))
        discountPercent = (discountAmount/mrp) * 100

    print(f'''    name = {name}
    category = {categoryName}
    prodCode = {prodCode}
    tax% = {taxPercent}
    tax Amount = {taxAmount}
    mrp = {mrp}
    discount % = {discountPercent}
    discount Amount = {discountAmount}''')

dict = {'capr0125':'obj1', 'capr1215':'obj2'}
enterDetails()