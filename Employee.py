Git-Hub Link:

# https://github.com/Jyoti-Pandey2610/CA1_Employee.git



import unittest


class Employee:
    # Constructor
    def __init__(self,StaffID,LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
        self.__StaffID = StaffID
        self.__RegHours = RegHours
        self.__HourlyRate = HourlyRate
        self.__OTMultiple = OTMultiple
        self.__TaxCredit = TaxCredit
        self.__StandardBand = StandardBand
        self.__LastName = LastName
        self.__FirstName = FirstName


    # defining the computePayment method:
    def computePayment(self, HoursWorked, date):
    # OverTimeWorked calculations [also checking for the ValueError condition]:
        if (self.__RegHours > HoursWorked):
            raise ValueError("Regular Hours Worked cannot exceed hours worked")
        else:
            OverTimeWorked = HoursWorked - self.__RegHours

    # calculating the Overtime rate:
        Over_Time_Rate = self.__HourlyRate * self.__OTMultiple
        # print(Over_Time_Rate)

    # calculating the Regular Pay:
        Regular_Pay = self.__RegHours * self.__HourlyRate
        # print(Regular_Pay)

    # calculating the Overtime pay [also, checking for the OverTimePay ValueError condition]:
        Over_Time_pay = Over_Time_Rate * OverTimeWorked
        if (Over_Time_pay < 0):
            raise ValueError('OverTimePay cannot be negative!')


    # calculating the Gross Pay:
        Gross_Pay = Regular_Pay + Over_Time_pay
        # print(Gross_Pay)

    # calculating the Higher rate pay:
        Higher_Rate_Pay = Gross_Pay - self.__StandardBand
        # print(Higher_Rate_Pay)

    # calculating the Standard tax: 20% Standard Tax as per the requirement
        Std_Tax = Gross_Pay * 0.2
        rnd_Std_Tax = round(Std_Tax)
        # print(rnd_Std_Tax)

    # calculating the Higher tax: 40% of Higher rate Pay
        Higher_Tax = Higher_Rate_Pay*0.4

    # checking the ValurError condotion for Higher Tax
        if (Higher_Tax < 0):
            raise ValueError("Higher Tax cannot be negative")


    # Calculating the Total Tax:
        Total_Tax = rnd_Std_Tax + Higher_Tax
        # print(Total_Tax)

    # Calculating Net Tax
        Net_Tax = Total_Tax - self.__TaxCredit
        # print(Net_Tax)

    # Calculating PRSI : with rate of 4%)
        PRSI = Gross_Pay * 0.04
        # print(PRSI)

    # calculating the Net Deduction
        Net_Deduction = Net_Tax + PRSI
        # print(Net_Deduction)


    # Checking for the ValueError for Net pay, which depends on the Net Deduction:
        if (Net_Deduction > 0):
            raise ValueError("Net Pay cannot be negative")
        else:
            Net_Pay = Gross_Pay - Net_Deduction
            if (Net_Deduction < 0):
                raise ValueError("Net Pay cannot exceed Gross Pay")

    # dictionary:
        dict = {
            "name": self.__FirstName + " " + self.__LastName,
            "Date": date,
            "Hours Worked": HoursWorked,
            "Regular Hours Worked": self.__RegHours,
            "Overtime Hours Worked": OverTimeWorked,
            "Regular Rate": self.__HourlyRate,
            "Overtime Rate": Over_Time_Rate,
            "Regular Pay": Regular_Pay,
            "Overtime Pay": Over_Time_pay,
            "Gross Pay": Gross_Pay,
            "Standard Rate Pay": self.__StandardBand,
            "Higher Rate Pay": Higher_Rate_Pay,
            "Standard Tax": Std_Tax,
            "Higher Tax": Higher_Tax,
            "Total Tax": Total_Tax,
            "Tax Credit": self.__TaxCredit,
            "Net Tax": Net_Tax,
            "PRSI": PRSI,
            "Net Deductions": Net_Deduction,
            "Net Pay": Net_Pay
        }
    # printing the dictionary
        print(dict)

    # returning the dictionary for the computePayment method
        return dict


# creating a class 'testEmployee' for the testing purpose:
class testEmployee(unittest.TestCase):

    # Testing: Net pay cannot exceed gross pay
    def testNetPayCannotExceedGrosspay(self):
        e = Employee(12345,'Green','Joe', 37, 16, 1.5, 550, 710)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])


    # Testing: Overtime pay cannot be negative.
    def testOverTimePayCannotBeNegative(self):
        e = Employee(12345, 'Green', 'Joe', 37, -16, 1.5, 72, 710)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(0, pi["Overtime Pay"])


    # Testing: Regular Hours cannot be greater than the Hours worked
    def testRegHoursNotGreaterThanHoursWorked(self):
        e = Employee(12345, 'Green', 'Joe', 73, 16, 1.5, 72, 710)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(pi["Regular Hours Worked"], pi["Hours Worked"])


    #Testing: Higher Tax cannot be negative.
    def testHigherTaxCannotBeNegative(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 715)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(0,pi["Higher Tax"])


    # Testing: Net Pay cannot be negative
    def testNetPayCannotBeNegative(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(0,pi["Net Pay"])

unittest.main(argv=['ignored'],exit=False)

