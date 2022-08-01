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


#function to generate the product code for a product
def productCodeGenerator(name,categoryName):
    prodCode = ""
    prodCode = prodCode + categoryName[0:2] + name[0:2]
  
    keyString = ""
    for i in dict:
        keyString += i
    count = len(re.findall(prodCode,keyString))
    prodCode += str(count) + str(random.randint(100,999))
    return prodCode


#function to calculate the mrp or baseprice
def taxCalculator(price, taxCriteria, taxpercent):
    if taxCriteria == 1:  #returns mrp
        return price + (price * taxpercent/100)
    else:  #returns base price
        return price - (price * taxpercent/100)


#function to user input the details and display all the entered and calculated details
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
    
    #calculates the discount percent or amount
    discountType = int(input("Enter discount type:\n1 -> Percentage\n2 -> Amount\n>"))
    if discountType == 1:
        discountPercent = int(input("Enter percentage of discount: "))
        discountAmount = (discountPercent/100) * mrp
    else:
        discountAmount = int(input("Enter amount of discount: "))
        discountPercent = (discountAmount/mrp) * 100

    #printing all the details
    print(f'''    name = {name}
    category = {categoryName}
    prodCode = {prodCode}
    tax% = {taxPercent}
    tax Amount = {taxAmount}
    mrp = {mrp}
    discount % = {discountPercent}
    discount Amount = {discountAmount}''')

# a dictionary of objects to hold objects with product code as the key
# objects are to be the values
dict = {'capr0125':'obj1', 'capr1215':'obj2'}

enterDetails()  #calling the function

# Output

# Enter the name of the product: prod
# Enter category of the product: cat
# Enter the price of the product: 100
# Enter tax perentage: 10
# Give type of price entered
# 1 -> tax extra
# 2 -> includes tax
# >2
# Enter discount type:
# 1 -> Percentage
# 2 -> Amount
# >1
# Enter percentage of discount: 10
#     name = prod
#     category = cat
#     prodCode = capr2343
#     tax% = 10
#     tax Amount = 10.0
#     mrp = 100
#     discount % = 10
#     discount Amount = 10.0