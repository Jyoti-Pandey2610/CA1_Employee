import unittest


class Employee:
    def __init__(self,StaffID,LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
        self.__StaffID = StaffID
        self.__LastName = LastName
        self.__FirstName = FirstName
        self.__RegHours = RegHours
        self.__HourlyRate = HourlyRate
        self.__OTMultiple = OTMultiple
        self.__TaxCredit = TaxCredit
        self.__StandardBand = StandardBand


    def computePayment(self, HoursWorked, date):
        # Over time worked calculations:
        if (HoursWorked < 0):
            raise ValueError('Hours Worked cannot be negative!!!')
        else:
            OverTimeWorked = HoursWorked - self.__RegHours


        if (self.__RegHours > HoursWorked):
            raise ValueError("Regular Hours Worked cannot exceed hours worked")

        Over_Time_Rate = self.__HourlyRate * self.__OTMultiple
        # print(Over_Time_Rate)

        Regular_Pay = self.__RegHours * self.__HourlyRate
        # print(Regular_Pay)

        Over_Time_pay = Over_Time_Rate * OverTimeWorked
        # print(Over_Time_pay)

        Gross_Pay = Regular_Pay + Over_Time_pay
        # print(Gross_Pay)

        Higher_Rate_Pay = Gross_Pay - self.__StandardBand
        # print(Higher_Rate_Pay)

        # 20% Standard Tax
        Std_Tax = Gross_Pay * 0.2
        rnd_Std_Tax = round(Std_Tax)
        # print(rnd_Std_Tax)

        # 40% of Higher rate Pay
        # Higher_Tax = Higher_Rate_Pay*0.4
        if (Higher_Rate_Pay < 0):
            raise ValueError("Higher Tax cannot be negative")
        else:
            Higher_Tax = Higher_Rate_Pay * 0.4
        # print(Higher_Tax)

        if (Higher_Tax < 0):
            raise ValueError("Net Pay cannot be negative.")

        Total_Tax = rnd_Std_Tax + Higher_Tax
        # print(Total_Tax)

        Net_Tax = Total_Tax - self.__TaxCredit
        # print(Net_Tax)

        # PRSI (at 4%)
        PRSI = Gross_Pay * 0.04
        # print(PRSI)

        Net_Deduction = Net_Tax + PRSI
        # print(Net_Deduction)

        Net_Pay = Gross_Pay - Net_Deduction
        # print(Net_Pay)

        dict = {
            "name": self.__FirstName + " " + self.__LastName,
            "Date": date,
            "Hours Worked": HoursWorked,
            "Regular Hours Worked": self.__RegHours,
            "Overtime Hours Worked": OverTimeWorked,
            "Regular Rate": self.__HourlyRate,
            "Overtime Rate": OverTimeWorked,
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
        print(dict)

        return dict

# e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
# e.computePayment(-42, '31/10/2021')

class testEmployee(unittest.TestCase):

    # Net pay cannot exceed gross pay
    def testNetPayCannotExceedGrosspay(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])


unittest.main(argv=['ignored'],exit=False)

    