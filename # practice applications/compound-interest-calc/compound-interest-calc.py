


# create functions for future value calculation [DONE]
# create function to view calculation history



def get_investment_info():

    while True:
        try: 

            print("""
                === Compound Interest Calculator ===
                1. Calculate Future Value
                2. View Calculation History
                3. Exit 
            """)

            program = int(input("Select one: "))

            if program == 1:
                calculate_future_value()
            elif program == 2:
                view_calc_history()
            else:
                continue


        except (ValueError, TypeError):
            print("Choice must be between 1 - 3")
        else:
            break




def calculate_future_value():

    initial_investment = float(input("Enter initial investment amount: "))
    annual_interest_rate = float(input("Enter annual interest rate: ")) / 100
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



    calculation_list = []
    calculations = {}

    calculations["Investment"] = initial_investment
    calculations["Interest Rate"] = annual_interest_rate
    calculations["Years"] = investment_period
    calculations["Future Value"] = final_investment_amount

    calculation_list.append(calculations)

    # for calculation in calculations:
    #     print(calculation)






def main():

    get_investment_info()



main()



