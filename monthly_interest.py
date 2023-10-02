'''Program that calculates monthly savings'''

initial_savings = int(input("Enter your initial savings: $"))
interest_rate = input("Enter your APY interest rate (percentage): ")
months = int(input("Enter months: "))

monthly_interest_rate = (float(interest_rate.strip("%")) / 100) / 12

savings = initial_savings
i = 1
while i <= months:
    savings += (initial_savings * monthly_interest_rate)
    print(f"Savings after {i} month/s: ${savings:.2f}")
    i += 1
