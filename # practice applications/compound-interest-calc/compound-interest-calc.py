


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
                calculate_future_value()

            elif program == 2:
                view_calc_history()

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


        print()


    final_investment_amount = initial_investment * (1 + rate / compounding_frequency) ** (compounding_frequency * investment_period)
    total_interest_earned = final_investment_amount - initial_investment


    print_summary(initial_investment, annual_interest_rate, investment_period, final_investment_amount, cf, total_interest_earned)
    add_calculation_to_list(initial_investment, annual_interest_rate, investment_period, final_investment_amount)


    return initial_investment, annual_interest_rate, investment_period, final_investment_amount, total_interest_earned




def print_summary(ii, air, ip, fia, cf, tia):


    print(f"""
    === Investment Summary ===
    Initial investment: ${ii:,.2f}
    Interest rate: {air}%
    Intvestment period: {ip} years
    Compounding frequency: {cf}
    Total interest earned: ${tia:,.2f}
    Future Value: ${fia:,.2f}
          """)





def add_calculation_to_list(ii, air, ip, fia):
    calculations = {}

    calculations["Investment"] = ii
    calculations["Interest Rate"] = air
    calculations["Years"] = ip
    calculations["Future Value"] = fia


    calculation_list.append(calculations)






def view_calc_history():

    counter = 0

    for calculation in calculation_list:

        counter += 1

        print(f"Investment# {counter}")
        print(f"Investment: ${calculation['Investment']:,.2f}")
        print(f"Interest rate: {calculation['Interest Rate']}%")
        print(f"Years: {calculation['Years']}")
        print(f"Future Value: ${calculation['Future Value']:,.2f}")



        print()




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


