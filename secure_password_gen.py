import random
import string
from termcolor import colored

def generate_password_specia_chars():
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[]{^_}~"
    password = ""
    for i in range(1, 31): 
        password = password + str(random.choice(chars))
    print(colored("password: " + password, "yellow", attrs=["bold"]))


def generate_password_just_letters():
    chars = string.ascii_lowercase + string.ascii_uppercase + "1234567890"
    password = ""

    for i in range(1, 31):  # Se mantiene el rango como en el código original
        password = password + str(random.choice(chars))
    print(colored("password: " + password, "yellow", attrs=["bold"]))

def main():
    title = """
  _____ ______  ____    ___   ____    ____  ____    ____  _____ _____ __    __   ___   ____   ___     ____    ___  ____  
 / ___/|      T|    \  /   \ |    \  /    T|    \  /    T/ ___// ___/|  T__T  T /   \ |    \ |   \   /    T  /  _]|    \ 
(   \_ |      ||  D  )Y     Y|  _  YY   __j|  o  )Y  o  (   \_(   \_ |  |  |  |Y     Y|  D  )|    \ Y   __j /  [_ |  _  Y
 \__  Tl_j  l_j|    / |  O  ||  |  ||  T  ||   _ |     |\__  T\__  T|  |  |  ||  O  ||    / |  D  Y|  T  |Y    _]|  |  |
 /  \ |  |  |  |    \ |     ||  |  ||  l_ ||  |   |  _  |/  \ |/  \ |l  `  '  !|     ||    \ |     ||  l_ ||   [_ |  |  |
 \    |  |  |  |  .  Yl     !|  |  ||     ||  |   |  |  |\    |\    | \      / l     !|  .  Y|     ||     ||     T|  |  |
  \___j  l__j  l__j\_j \___/ l__j__jl___,_jl__j   l__j__j \___j \___j  \_/\_/   \___/ l__j\_jl_____jl___,_jl_____jl__j__j                                                                                                            
    """
    credits = """By: https://github.com/estefanozarate"""
    print(colored(title,"magenta", attrs=["bold"]))
    print(colored(credits,"blue", attrs=["bold"]))
    while True:
        print("[+] Generate secure password with special chars: 1")
        print("[+] Generate secure password without special chars: 2")
        print("[+] Exit: 3")
        code = int(input("[1, 2, 3]: "))
        if code == 1:
            generate_password_specia_chars()
            break
        elif code == 2:
            generate_password_just_letters()
            break
        elif code == 3:
            print("Good-Bye!")
            break
        else:
            print("[!] Invalid Code!")
            print("\n")
            main()

if __name__ == "__main__":
    main()

