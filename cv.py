WHITE='\033[1;37m'
NC='\033[0m'

cv_text =f"""
    Here is my CV! Cool, right? 
    I love Stack Overflow {WHITE}I hate Stack Overflow
    I hate {NC}I really love Stack Overflow 
    {'This is right aligned text':>100}
    """ 

print(cv_text)
