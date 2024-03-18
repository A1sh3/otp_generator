import random
import string

def generateOTP(length):
    char = string.digits
    otp = ''.join(random.choice(char) for i in range(length))
    return otp

otp = generateOTP(4)
print("OTP generated is:", otp)
