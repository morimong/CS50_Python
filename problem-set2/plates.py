def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0:2].isalpha() == False:
        return False
    
    num_flg = False
    for i in s[2:]:
        if i.isdigit():
            num_flg = True
            
main()

