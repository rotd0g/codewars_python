def validate_pin(pin):
    #return true or false
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
        else:
            return False
    else:
        return False

print(validate_pin("33234"))

# validate_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()