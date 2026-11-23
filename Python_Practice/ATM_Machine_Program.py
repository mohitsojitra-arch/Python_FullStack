# # Create an ATM machine
# # - User should be able get money out of it
# # - User should be able to deposite money into it
# # - You must ask card number and pin before any transaction
# # - User can get overall information about his bank account
# # - There should be a limit in one time transaction and total transaction in a day (Consider day as from
# # starting of script to exit)
# # - Limit on number of transaction
# # - Let user choose the bank of ATM
# # - Every ATM will have some initial balance
# # - Every user has it's own bank
# # - If user takes money from an ATM other than his bank take 5% cut in withdrawl amount
# # Nice to have features:
# # - Insert, update and delete users (Generate card number and PIN randomly)
# # - Insert, update and delete ATMs
# # - Insert, update and delete banks
# # - Insert money into ATM (No database is needed for this it can be managed using dicts)
# # Hint: You can manage all this with data dictionary data type.




class Banks:

    def __init__(self, BankName, ATMBalance,
                 NumberOfTransactionLimit, OneDayLimit,
                 PerTransactionLimit):

        self.BankName = BankName
        self.ATMBalance = ATMBalance
        self.NumberOfTransactionLimit = NumberOfTransactionLimit
        self.OneDayLimit = OneDayLimit
        self.PerTransactionLimit = PerTransactionLimit

    def Bank_Detail(self):

        print("----------------------------------")
        print(f"Bank Name : {self.BankName}")
        print(f"ATM Balance : {self.ATMBalance}")
        print(f"Number Of Transaction Limit : {self.NumberOfTransactionLimit}")
        print(f"One Day Limit : {self.OneDayLimit}")
        print(f"Per Transaction Limit : {self.PerTransactionLimit}")
        print("----------------------------------")


class User:

    def __init__(self, UserName, BankName, Balance,
                 TransactionCount, CardNumber, PIN, WithDrawMoney):

        self.UserName = UserName
        self.BankName = BankName
        self.Balance = Balance
        self.TransactionCount = TransactionCount
        self.CardNumber = CardNumber
        self.PIN = PIN
        self.WithDrawMoney = WithDrawMoney

    def User_Detail(self):

        print("----------------------------------")
        print(f"User Name : {self.UserName}")
        print(f"Bank Name : {self.BankName}")
        print(f"Balance : {self.Balance}")
        print(f"Transaction Count : {self.TransactionCount}")
        print(f"Card Number : {self.CardNumber}")
        print(f"PIN Number : {self.PIN}")
        print(f"Total Withdraw Money : {self.WithDrawMoney}")
        print("----------------------------------")

    # Withdraw Money

    def WithDraw(self, CurrentWithDrawMoney,
                 Current_Bank_OneDayLimit,
                 Current_Bank_ATMBalance,
                 Current_Bank_TransactionLimit,
                 Current_Bank_PerTransactionLimit,
                 IsOtherBank):

        print("\nWithdraw Money :")

        if CurrentWithDrawMoney <= 0:
            print("Please Enter Valid Amount")
            return False

        if CurrentWithDrawMoney > self.Balance:
            print("Insufficient Account Balance")
            return False

        if self.TransactionCount >= Current_Bank_TransactionLimit:
            print("Transaction Limit Exceeded")
            return False

        if self.WithDrawMoney + CurrentWithDrawMoney > Current_Bank_OneDayLimit:
            print("One Day Withdrawal Limit Exceeded")
            return False

        if CurrentWithDrawMoney > Current_Bank_PerTransactionLimit:
            print("Per Transaction Limit Exceeded")
            return False

        if CurrentWithDrawMoney > Current_Bank_ATMBalance:
            print("ATM Balance Not Available")
            return False

        # 5% charge for using another bank ATM

        Charge = 0

        if IsOtherBank:
            Charge = CurrentWithDrawMoney * 0.05

        TotalAmount = CurrentWithDrawMoney + Charge

        if TotalAmount > self.Balance:
            print("Insufficient Balance Including 5% ATM Charges")
            return False

        # Update account details

        self.Balance -= TotalAmount
        self.TransactionCount += 1
        self.WithDrawMoney += CurrentWithDrawMoney

        print("\nSuccessfully Withdraw Money:", CurrentWithDrawMoney)

        if IsOtherBank:
            print("Other Bank ATM Charges (5%):", Charge)

        print("Total Amount Deducted:", TotalAmount)

        return True

    # Deposit Money

    def Deposit(self, DepositMoney, CurrentBank):

        print("\nDeposit Money :")

        if DepositMoney <= 0:
            print("Please Enter Valid Amount")
            return False

        if self.TransactionCount >= CurrentBank.NumberOfTransactionLimit:
            print("Transaction Limit Exceeded")
            return False

        # Update account and ATM balance

        self.Balance += DepositMoney
        CurrentBank.ATMBalance += DepositMoney
        self.TransactionCount += 1

        print("Successfully Deposited:", DepositMoney)

        return True


# ----------------------------------
# Bank Users
# ----------------------------------

All_User = []

All_User.append(User("Mohit", "SBI", 150000, 0, 1001, 123, 0))
All_User.append(User("Keval", "BOI", 50000, 0, 1002, 456, 0))
All_User.append(User("Raj", "ICICI", 240000, 0, 1003, 789, 0))
All_User.append(User("Meet", "BOI", 10000, 0, 1004, 123, 0))
All_User.append(User("Rahul", "SBI", 6000, 0, 1005, 456, 0))


# ----------------------------------
# All Banks
# ----------------------------------

All_Banks = []

All_Banks.append(Banks("SBI", 5000000, 5, 100000, 40000))
All_Banks.append(Banks("BOI", 3000000, 4, 80000, 30000))
All_Banks.append(Banks("ICICI", 2000000, 3, 70000, 20000))


# ----------------------------------
# Main ATM Program
# ----------------------------------

while True:

    print("\n================================")
    print("          ATM MACHINE")
    print("================================")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")
    print("================================")

    try:
        user = int(input("Enter Your Choice : "))
    except ValueError:
        print("Please Enter Valid Choice")
        continue

    # ----------------------------------
    # Admin Option
    # ----------------------------------

    if user == 1:

        print("\nAdmin Menu")

        print("\n 1 For Show All User : ")
        print("\n 2 For Show All Banks : ")
        print("\n 3 For Add User : ")
        print("\n 4 For Remove User : ")
        print("\n 5 For Add Banks : ")
        print("\n 6 For Remove Banks : ")

        try:
            Admin_Choice = int(input("Enter Admin Choice : "))
        except ValueError:
            print("Please Enter Valid Choice")
            continue

        if Admin_Choice == 1:

            for i in range(0, len(All_User)):
                All_User[i].User_Detail()

        elif Admin_Choice == 2:

            for i in range(0, len(All_Banks)):
                All_Banks[i].Bank_Detail()

        elif Admin_Choice == 3:

            print("***************************")

            New_UserName = input("Enter New User Name : ")
            New_UserBankName = input("Enter New User Bank Name : ")

            New_UserBankBalance = int(input("Enter New User Bank Balance : "))
            New_UserCardNumber = int(input("Enter New User Card Number : "))
            New_UserPINNumber = int(input("Enter New User PIN Number : "))

            All_User.append(User(
                New_UserName,
                New_UserBankName,
                New_UserBankBalance,
                0,
                New_UserCardNumber,
                New_UserPINNumber,
                0
            ))

            print("User Added Successfully")
            print("***************************")

        elif Admin_Choice == 4:

            print("Remove User : ")

            if len(All_User) == 0:
                print("No Users Available")
                continue

            for i in range(0, len(All_User), 1):
                print(f"User Name : {All_User[i].UserName} index : {i}")

            try:
                User_delete_Index_Number = int(
                    input("Enter Index Number To Delete User : ")
                )
            except ValueError:
                print("Please Enter Valid Index Number")
                continue

            # Correct Remove User Logic

            if 0 <= User_delete_Index_Number < len(All_User):

                Deleted_User = All_User.pop(User_delete_Index_Number)

                print("User Removed Successfully :", Deleted_User.UserName)

            else:
                print("Invalid User Index Number")

        elif Admin_Choice == 5:

            print("***************************")

            New_BankName = input("Enter New Bank Name : ")
            New_ATMBalance = int(input("Enter New ATM Balance : "))
            New_NumberOfTransactionLimit = int(input("Enter Transaction Limit : "))
            New_OneDayLimit = int(input("Enter One Day Limit : "))
            New_PerTransactionLimit = int(input("Enter Per Transaction Limit : "))

            All_Banks.append(Banks(
                New_BankName,
                New_ATMBalance,
                New_NumberOfTransactionLimit,
                New_OneDayLimit,
                New_PerTransactionLimit
            ))

            print("Bank Added Successfully")
            print("***************************")

        elif Admin_Choice == 6:

            print("Remove Banks : ")

            if len(All_Banks) == 0:
                print("No Banks Available")
                continue

            for i in range(0, len(All_Banks), 1):
                print(f"Bank Name : {All_Banks[i].BankName} index : {i}")

            try:
                Bank_delete_Index_Number = int(
                    input("Enter Index Number To Delete Bank : ")
                )
            except ValueError:
                print("Please Enter Valid Index Number")
                continue

            # Correct Remove Bank Logic

            if 0 <= Bank_delete_Index_Number < len(All_Banks):

                Deleted_Bank = All_Banks.pop(Bank_delete_Index_Number)

                print("Bank Removed Successfully :", Deleted_Bank.BankName)

            else:
                print("Invalid Bank Index Number")

        else:
            print("Invalid Admin Choice")

    # ----------------------------------
    # User Option
    # ----------------------------------

    elif user == 2:

        print("\nUser Login")

        Current_Card_Number = input("Enter Card Number : ")
        Current_PIN = input("Enter PIN : ")

        Current_User_Index = -1

        # Validate Card Number and PIN

        for i in range(len(All_User)):

            if (str(All_User[i].CardNumber) == Current_Card_Number
                    and str(All_User[i].PIN) == Current_PIN):

                Current_User_Index = i
                break

        if Current_User_Index == -1:

            print("\nInvalid Card Number or PIN")
            continue

        Current_User = All_User[Current_User_Index]

        print("\nWelcome", Current_User.UserName)

        # ----------------------------------
        # User Menu
        # ----------------------------------

        while True:

            print("\n--------------------------------")
            print("1. Withdraw Money")
            print("2. Deposit Money")
            print("3. Show Account Details")
            print("4. Exit")
            print("--------------------------------")

            try:
                Current_Choice = int(input("Enter Your Choice : "))
            except ValueError:
                print("Please Enter Valid Choice")
                continue

            # ----------------------------------
            # Withdraw Money
            # ----------------------------------

            if Current_Choice == 1:

                try:
                    User_Amount_To_WithDraw = int(
                        input("Enter Amount To Withdraw : ")
                    )
                except ValueError:
                    print("Please Enter Valid Amount")
                    continue

                print("\nAvailable ATM Banks")

                for bank in All_Banks:
                    print(bank.BankName)

                User_Enter_ATM_Name = input(
                    "\nEnter ATM Bank Name : "
                ).strip().upper()

                Current_Index_Banks = -1

                # Find Selected ATM Bank

                for i in range(len(All_Banks)):

                    if All_Banks[i].BankName.upper() == User_Enter_ATM_Name:
                        Current_Index_Banks = i
                        break

                if Current_Index_Banks == -1:

                    print("ATM Bank Not Found")
                    continue

                Current_Bank = All_Banks[Current_Index_Banks]

                # Check Other Bank ATM

                IsOtherBank = (
                    Current_User.BankName.upper()
                    != Current_Bank.BankName.upper()
                )

                # Call Withdraw Method

                Result = Current_User.WithDraw(
                    User_Amount_To_WithDraw,
                    Current_Bank.OneDayLimit,
                    Current_Bank.ATMBalance,
                    Current_Bank.NumberOfTransactionLimit,
                    Current_Bank.PerTransactionLimit,
                    IsOtherBank
                )

                # Update ATM Balance

                if Result:

                    Current_Bank.ATMBalance -= User_Amount_To_WithDraw

            # ----------------------------------
            # Deposit Money
            # ----------------------------------

            elif Current_Choice == 2:

                try:
                    DepositMoney = int(
                        input("Enter Deposit Amount : ")
                    )
                except ValueError:
                    print("Please Enter Valid Amount")
                    continue

                # Find User's Own Bank ATM

                Current_Bank = None

                for bank in All_Banks:

                    if bank.BankName == Current_User.BankName:
                        Current_Bank = bank
                        break

                if Current_Bank is None:

                    print("User Bank Not Found")
                    continue

                # Call Deposit Method

                Current_User.Deposit(DepositMoney, Current_Bank)

            # ----------------------------------
            # Account Details
            # ----------------------------------

            elif Current_Choice == 3:

                print("\nAccount Details")

                Current_User.User_Detail()

            # ----------------------------------
            # Exit User Menu
            # ----------------------------------

            elif Current_Choice == 4:

                print("Thank You For Using ATM")
                break

            else:

                print("Invalid Choice")

    # ----------------------------------
    # Exit Program
    # ----------------------------------

    elif user == 3:

        print("\nThank You For Using ATM Machine")
        break

    else:

        print("Invalid Choice")
