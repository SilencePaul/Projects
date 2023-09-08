import FederalTax
import NetProvinceTax
import Deduction
import AgeAmount


class FederalTaxCal:
    def __init__(self, diction):
        self.__diction = diction

    def calculation(self):
        refund = 0
        balanceOwing = 0
        netProvinceTax = 0
        # Basic Information
        bod = self.__diction['Date of Birth']
        age = 2021 - float(bod[:4])
        # Line 10100
        income = float(self.__diction['Employment Income'])
        incomeTaxDeducted = float(self.__diction['Income tax deducted'])
        CPPContribution = float(self.__diction['CPP contributions'])
        employeeEI = float(self.__diction['Employee EI premiums'])
        RPPDeduction = float(self.__diction['Registered Pension Plan'])
        annualUnionDue = float(self.__diction['Annual union dues'])
        pensionAdjustment = float(self.__diction['Pension Adjustment'])
        canadianArmedForce = float(self.__diction['Canadian Armed Forces'])
        unusedFTuition = float(self.__diction['Unused federal tuition'])
        tuitionFee2021 = float(self.__diction['2021 Tuition Fee'])
        CWBAdvanced = float(self.__diction['CWB advanced payment'])
        province = self.__diction['Province']
        D2Charities = float(self.__diction['Donation to Charities'])
        D2Government = float(self.__diction['Donation to government bodies'])
        D2University = float(self.__diction['Donation to universities outside Canada'])
        D2UnitedNation = float(self.__diction['Donation to United Nations'])
        # Calculate CPP
        cppCal = Deduction.CPPContribution(income, CPPContribution)
        Line30800, Line58420, Line22215, Line44800 = cppCal.calCPP()
        # Line 23600
        netIncome = income - pensionAdjustment - annualUnionDue - Line22215 - RPPDeduction
        # Line 26000
        taxableIncome = netIncome - canadianArmedForce
        # Line 73
        federalTax = FederalTax.FederalIncomeTax(taxableIncome).calculate_tax()
        federalBasicAmount = Deduction.FederalBasicPersonalAmount(netIncome).determineAmount()
        ageAmount = AgeAmount.FederalAgeAmount(age, netIncome).determineAmount()
        EIAmount = Deduction.EmployeeInsurance(employeeEI, province).defineMaxAmount()
        canadaEmploymentAmount = 1257
        if income < canadaEmploymentAmount:
            canadaEmploymentAmount = income
        Line99 = federalBasicAmount + ageAmount + Line30800 + EIAmount + canadaEmploymentAmount
        tuitionAmount = Deduction.FederalTuitionCredit(unusedFTuition, tuitionFee2021, federalTax, Line99).calTuition()
        Line111 = tuitionAmount + Line99
        donationAndGift, S9Line13, S9Line14 = Deduction.DonationsAndGifts(netIncome, D2Charities, D2Government,
                                                                          D2University, D2UnitedNation
                                                                          ).calDonationAndGift()
        # Line 35000
        totalFNRTaxCredit = Line111 * 0.15 + donationAndGift
        # Line 42000
        basicFederalTax = federalTax - totalFNRTaxCredit
        if basicFederalTax <= 0:
            basicFederalTax = 0
        netFederalTax = basicFederalTax + CWBAdvanced
        if province == 'ON':
            netProvinceTax = NetProvinceTax.NetONTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'NL':
            netProvinceTax = NetProvinceTax.NetNLTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'PE':
            netProvinceTax = NetProvinceTax.NetPETax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'NS':
            netProvinceTax = NetProvinceTax.NetNSTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'NB':
            netProvinceTax = NetProvinceTax.NetNBTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'MB':
            netProvinceTax = NetProvinceTax.NetMBTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'SK':
            netProvinceTax = NetProvinceTax.NetSKTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'AB':
            netProvinceTax = NetProvinceTax.NetABTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'BC':
            netProvinceTax = NetProvinceTax.NetBCTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'YT':
            netProvinceTax = NetProvinceTax.NetYTTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'NT':
            netProvinceTax = NetProvinceTax.NetNTTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        elif province == 'NU':
            netProvinceTax = NetProvinceTax.NetNUTax(province, income, netIncome, taxableIncome, age,
                                                     Line30800, EIAmount, S9Line13, S9Line14).calTax()
        totalPayable = netFederalTax + netProvinceTax
        if province == 'AB' or province == 'NU':
            CWB = 0
        else:
            CWB = Deduction.CWB(income, netIncome).calCWB()
        totalCredit = incomeTaxDeducted + Line44800 + CWB
        refundORBalance = totalPayable - totalCredit
        if refundORBalance > 0:
            balanceOwing = refundORBalance
        else:
            refund = abs(refundORBalance)
        return refund, balanceOwing
