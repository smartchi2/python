invested = 0
years = 0
total = 0

print("WELCOME TO SMART INVESTMENT APP.........")
invested = int(input("Enter amount: "))
rate = 20 / 100

years = int(input("Enter years of investment: "))
interest = invested * rate

index = 1
for i in range(years):
		interest = invested * rate
		bestamount = interest + invested
		invested = bestamount
		print(f"years of invesmentu{index}   {invested:,.2f}")
		index += 1

		
		 