import ProvincesTaxRate
import Deduction
import AgeAmount


class NetONTax:
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        self.__province = province
        self.__income = income
        self.__netIncome = netIncome
        self.__taxableIncome = taxableIncome
        self.__age = age
        self.__CPP = CPP
        self.__EI = EI
        self.__Line13 = Line13
        self.__Line14 = Line14
        self.__basicPersonalAmount = 10880
        self.__NRTRate = 0.0505
        self.__Line14Rate = 0.1116

    def calTax(self):
        Tax = 0
        ageAmount = 0
        LIFT = 0
        OHP = 0
        NLLITCredit = 0
        PELICredit = 0
        NSLICredit = 0
        NBLICredit = 0
        CBTaxCredit = 0
        if self.__province == 'ON':
            Tax = ProvincesTaxRate.ONTax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.ONAgeAmount(self.__age, self.__income).determineAmount()
        elif self.__province == 'NL':
            Tax = ProvincesTaxRate.NLTax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.NLAgeAmount(self.__age, self.__income).determineAmount()
        elif self.__province == 'PE':
            Tax = ProvincesTaxRate.PETax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.PEAgeAmount(self.__age, self.__income).determineAmount()
        elif self.__province == 'NS':
            Tax = ProvincesTaxRate.NSTax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.NSAgeAmount(self.__age, self.__income).determineAmount()
        elif self.__province == 'NB':
            Tax = ProvincesTaxRate.NBTax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.NBAgeAmount(self.__age, self.__income).determineAmount()
        elif self.__province == 'MB':
            Tax = ProvincesTaxRate.MBTax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.MBAgeAmount(self.__age, self.__income).determineAmount()
        elif self.__province == 'SK':
            Tax = ProvincesTaxRate.SKTax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.SKAgeAmount(self.__age, self.__income).determineAmount()
        elif self.__province == 'AB':
            Tax = ProvincesTaxRate.ABTax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.ABAgeAmount(self.__age, self.__income).determineAmount()
        elif self.__province == 'BC':
            Tax = ProvincesTaxRate.BCTax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.BCAgeAmount(self.__age, self.__income).determineAmount()
        elif self.__province == 'NT':
            Tax = ProvincesTaxRate.NTTax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.NTAgeAmount(self.__age, self.__income).determineAmount()
        elif self.__province == 'NU':
            Tax = ProvincesTaxRate.NUTax(self.__netIncome).calculate_tax()
            ageAmount = AgeAmount.NUAgeAmount(self.__age, self.__income).determineAmount()
        Line25 = self.__basicPersonalAmount + ageAmount + self.__CPP + self.__EI
        donationAndGift = (self.__Line13 * self.__NRTRate) + (self.__Line14 * self.__Line14Rate)
        NRTaxCredit = Line25 * self.__NRTRate + donationAndGift
        Line55 = Tax - NRTaxCredit
        if self.__province == 'ON':
            LIFT = Deduction.LIFTCredit(self.__income, self.__netIncome).calCredit()
            OHP = Deduction.OntarioHealthPremium(self.__netIncome).calOHP()
        elif self.__province == 'AB':
            NLLITCredit = Deduction.NLLITCredit(self.__netIncome).cal()
        elif self.__province == 'PE':
            PELICredit = Deduction.PELICredit(self.__netIncome, self.__age).cal()
        elif self.__province == 'NS':
            NSLICredit = Deduction.NSLICredit(self.__netIncome).cal()
        elif self.__province == 'NB':
            NBLICredit = Deduction.NBLICredit(self.__netIncome).cal()
        elif self.__province == 'NB':
            CBTaxCredit = Deduction.CBTaxCredit(self.__netIncome).cal()
        Line86 = Line55 - LIFT - NLLITCredit - PELICredit - NSLICredit - NBLICredit - CBTaxCredit
        if Line86 < 0:
            Line86 = 0
        netTax = Line86 + OHP
        return netTax


class NetABTax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 19369
        self.__NRTRate = 0.1
        self.__Line14Rate = 0.21


class NetNLTax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 9536
        self.__NRTRate = 0.087
        self.__Line14Rate = 0.183


class NetPETax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 10500
        self.__NRTRate = 0.098
        self.__Line14Rate = 0.167


class NetNSTax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 11481
        self.__NRTRate = 0.0879
        self.__Line14Rate = 0.21


class NetNBTax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 10564
        self.__NRTRate = 0.094
        self.__Line14Rate = 0.1795


class NetMBTax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 9936
        self.__NRTRate = 0.108
        self.__Line14Rate = 0.174


class NetSKTax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 16225
        self.__NRTRate = 0.105
        self.__Line14Rate = 0.145


class NetBCTax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 11070
        self.__NRTRate = 0.0506
        self.__Line14Rate = 0.168


class NetYTTax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 13808
        self.__NRTRate = 0.064
        self.__Line14Rate = 0.128


class NetNTTax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 15243
        self.__NRTRate = 0.059
        self.__Line14Rate = 0.1405


class NetNUTax(NetONTax):
    def __init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14):
        NetONTax.__init__(self, province, income, netIncome, taxableIncome, age, CPP, EI, Line13, Line14)
        self.__basicPersonalAmount = 16467
        self.__NRTRate = 0.04
        self.__Line14Rate = 0.115
