print("\n\n======== Welcome to Ro's LCM & HCF ========")
print("\nEnter the numbers below to find the HCF and LCM:")
num1 = int(input("Enter the first number => ")) #user_input1
num2 = int(input("Enter the second number => ")) #user_input2

#LCM:
def lcm(num1, num2):
    m_n = max(num1, num2) #max_num

    while True:
        if m_n % num1 == 0 and m_n % num2 == 0:
            break
        m_n += 1
    lcm = m_n    
    print(f"\nThe LCM of numbers {num1} & {num2} = {lcm}")

#HCF:
def hcf(num1, num2):
    if num2>num1:
        s_n = num1 #smaller_num
    else:
        s_n = num2 #smaller_num

    for factor in range(2, s_n+1):
        if num1 % s_n == 0 and num2 % s_n == 0:
            hcf = factor
    hcf = factor
    print(f"The HCF of numbers {num1} & {num2} = {hcf}")

lcm(num1, num2)
hcf(num1, num2)