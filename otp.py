import random

def generate_otp():
    return random.randint(100000, 999999)

def verify_otp():
  
    sender_email = "settamsaisandeep@gmail.com"
    receiver_email = "settamsaisandeep@gmail.com"
    
    otp = generate_otp()

    print("Simulated OTP:", otp)

    user_otp = input("Enter the OTP you received: ")

    if user_otp == str(otp):
        print("OTP verification successful!")
    else:
        print("OTP verification failed!")

print("Welcome to OTP Verification!")
verify_otp()