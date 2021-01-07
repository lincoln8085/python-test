#creating a  dictonary
product={
    "M":"MILK",
    "B":"BREAD",
    "I":"ICE CREAM",
    0:"TONED",
    1:"DOUBLE TONED",
    2:"FULL CREAM ",
    10:"WHITE BREAD",
    11:"BROWN BREAD",
    20:"VANILLA",
    21:"STRAWBERRY"


}


#direct method
print(product[2])

#using get function
print(product.get("M","not a valid product id"))
print(product.get("g","not a valid product id"))