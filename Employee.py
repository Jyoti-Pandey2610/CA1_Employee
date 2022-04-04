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
        pass
        


class testEmployee(unittest.TestCase):
    pass

    