#Exercise 10
#Name your file: PoundsToDollars.py
#Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
#An example runs of the program:
#Please enter amount in pounds: XXX
#£ XXX are $ XXX

def poundsToDollar(pound):
    # Conversion rate: 1 pound = 1.25 dollars (example rate, you can adjust as needed)
    conversion_rate = 1.25
    # Convert pounds to dollars
    dollars = pounds * conversion_rate
    return dollars

pounds = float(input("Please enter amount in pounds"))
dollars = poundsToDollar(pounds)

# Print the converted amount
print(f"£ {pounds} are $ {dollars}")