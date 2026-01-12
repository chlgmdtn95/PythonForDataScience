def NULL_not_found(object: any) -> int:
    #your code here
    
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif type(object) == float and not(object <= 0 or object > 0):
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif type(object) == int and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif type(object) == str and object == "":
        print(f"Empty: {object} {type(object)}")
        return 0
    elif type(object) == bool and object == False:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not found")
        return 1