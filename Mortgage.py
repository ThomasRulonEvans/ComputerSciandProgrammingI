#user input (mortgage amount, rate, length of mortgage)
amount = input("What is the total amount for your mortgage?")
rate = input("What is the interest rate?")
months = input("How many months is your mortgage?")

#calculations
monthly_rate = (float(rate)/100)/12
payment = float(amount) * ((monthly_rate*((1+monthly_rate)**float(months)))/((1+monthly_rate)**(float(months))-1))

#result
print("Your monthly payment will be " + str(payment))
