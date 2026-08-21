


# create functions for future value calculation [DONE]
# create function to view calculation history [DONE]
# create function to add calculation to list [DONE]
# create function to print summary


calculation_list = []



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
                ii, air, ip, fia, tia = calculate_future_value()

            elif program == 2:
                view_calc_history(ii, air, ip, fia, tia)

            elif program == 3:
                break

            else:
                print("Choice must be between 1 - 3")

        except (ValueError, TypeError):
            print("Choice must be between 1 - 3")



def calculate_future_value():

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


    final_investment_amount = initial_investment * (1 + rate / compounding_frequency) ** (compounding_frequency * investment_period)
    total_interest_earned = final_investment_amount - initial_investment

    
    print(f"""
    === Investment Summary ===
    Initial investment: ${initial_investment:,.2f}
    Interest rate: {rate}%
    Intvestment period: {investment_period} years
    Compounding frequency: {cf}
    Total interest earned: ${total_interest_earned:,.2f}
    Future Value: ${final_investment_amount:,.2f}
          """)

    # for calculation in calculation_list:
    #     print(calculation)

    # return calculation_list.append(calculations)

    add_calculation_to_list(initial_investment, annual_interest_rate, investment_period, final_investment_amount, total_interest_earned)

    return initial_investment, annual_interest_rate, investment_period, final_investment_amount, total_interest_earned





def add_calculation_to_list(ii, air, ip, fia, tia):
    calculations = {}

    calculations["Investment"] = ii
    calculations["Interest Rate"] = air
    calculations["Years"] = ip
    calculations["Future Value"] = fia


    calculation_list.append(calculations)






def view_calc_history(ii, air, ip, fia, tia):

    for calculation in calculation_list:
        print(f"Investment: {calculation['Investment']}")
        print(f"Interest rate: {calculation['Interest Rate']}")
        print(f"Years: {calculation['Years']}")
        print(f"Future Value: {calculation['Future Value']}")





def main():

    get_investment_info()


main()



"""
# THINGS LEARNT
- in control flow, one break should be done to ensure the program doesn't break out of the loop prematurely (had a break in the try-except block)
- an else: break at the end of the try-except is not always needed and it means the meu will exit after any valid input 

def get_investment_info():
    while True:
        try:
            print("""
# === Compound Interest Calculator ===
# 1. Calculate Future Value
# 2. View Calculation History
# 3. Exit
""")

            program = int(input("Select one: "))

            if program == 1:
                calculate_future_value()
            elif program == 2:
                view_calc_history()
            elif program == 3:
                break

        except (ValueError, TypeError):
            print("Choice must be between 1 - 3")

        else:
            break


- view_calc_history wasn't working because using " to identify the dictionary key was preventing the loop from accessing the key properly
- 
"""


