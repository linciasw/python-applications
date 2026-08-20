

def main():
    initial_investment = float(input("Enter initial investment amount: "))
    annual_interest_rate = float(input("Enter annual interest rate: "))
    investment_period = int(input("Enter investment period (years): "))

    rate = annual_interest_rate / 100
    





    while True:

        try:

            print("""
                        Choose compounding frequency: 
                            1. Annually
                            2. Semi-annually
                            3. Quarterly
                            4. Monthly
            
            """)
            choice = int(input("Choice: "))

        
            if choice == 1:
                compounding_frequency = 1
                cf = "Annually"
            elif choice == 2:
                compounding_frequency = 2
                cf = "Semi-Annually"
            elif choice == 3:
                compounding_frequency = 4
                cf = "Quarterly"
            elif choice == 4:
                compounding_frequency = 12
                cf = "Monthly"
            else:
                continue




        except ValueError:
            print("Choice must be between 1 - 4")
        else:
            break



#     A = P(1 + r/n)^(nt)
# Where:

# A = Final investment amount
# P = Initial investment amount
# r = Annual interest rate (decimal)
# n = Number of times interest compounds per year
# t = Number of years
    

   

    final_investment_amount = initial_investment * (1 + rate / compounding_frequency) ** (compounding_frequency * investment_period)

    total_interest_earned = final_investment_amount - initial_investment
    


    
    print(f"""
    === Investment Summary ===
    Initial investment: ${initial_investment:,.2f}
    Interest rate: {annual_interest_rate}%
    Intvestment period: {investment_period} years
    Compounding frequency: {cf}
    Total interest earned: ${total_interest_earned:,.2f}
    Future Value: ${final_investment_amount:,.2f}
          """)


    calculation_history = {

        
    }



main()