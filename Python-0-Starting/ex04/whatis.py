import sys

try:
    assert len(sys.argv) < 3, "more than one argument is provided"
    # assert len(sys.argv) > 1, "no argument"
    
    if len(sys.argv) == 1 :
        exit()
    try:
        tem = int(sys.argv[1])
        
    except:
        raise AssertionError("argument is not an integer")

except AssertionError as e:
    print("AssertionError:", e)

else:
    if tem % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")