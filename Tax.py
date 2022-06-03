# Tax Project
import openpyxl
from datetime import datetime
import FederalTaxCalculation


def get_TXT_info():
    tax_info = open('Tax_Information.txt', 'r')
    info = tax_info.readline()
    infoDiction = {}
    while info != "":
        index = info.find(":")
        title = info[:index]
        content = info[index + 1:]
        content = content.strip()
        if 'Name' in title:
            infoDiction['Name'] = content
        elif 'SIN' in title:
            infoDiction['SIN'] = content
            if len(content) != 9:
                raise ValueError('Incorrect length of SIN number.')
        elif 'Date of Birth' in title:
            infoDiction['Date of Birth'] = content
            try:
                datetime.strptime(content, "%Y/%m/%d")
            except ValueError:
                raise ValueError("Incorrect date format, should be YYYY/MM/DD.")
        elif 'Province' in title:
            infoDiction['Province'] = content
            if content == 'Alberta' or content == 'AB':
                infoDiction['Province'] = 'AB'
            elif content == 'British Columbia' or content == 'BC':
                infoDiction['Province'] = 'BC'
            elif content == 'Manitoba' or content == 'MB':
                infoDiction['Province'] = 'MB'
            elif content == 'New Brunswick' or content == 'NB':
                infoDiction['Province'] = 'NB'
            elif content == 'Newfoundland' or content == 'NL' or content == 'Newfoundland and Labrador':
                infoDiction['Province'] = 'NL'
            elif content == 'Nova Scotia' or content == 'NS':
                infoDiction['Province'] = 'NS'
            elif content == 'Northwest Territories' or content == 'NT':
                infoDiction['Province'] = 'NT'
            elif content == 'Nunavut' or content == 'NU':
                infoDiction['Province'] = 'NU'
            elif content == 'Ontario' or content == 'ON':
                infoDiction['Province'] = 'ON'
            elif content == 'Prince Edward Island' or content == 'PE':
                infoDiction['Province'] = 'PE'
            elif content == 'Quebec' or content == 'QC':
                print('Sorry, this tax calculator do not work on Quebec Tax.')
                raise ValueError('Please enter a province except Quebec.')
            elif content == 'Saskatchewan' or content == 'SK':
                infoDiction['Province'] = 'SK'
            elif content == 'Yukon' or content == 'YT':
                infoDiction['Province'] = 'YT'
            else:
                raise ValueError('The province value is wrong, please enter a reasonable province.')
        elif 'Mailing Address' in title:
            infoDiction['Mailing Address'] = content
        elif 'Email Address' in title:
            infoDiction['Email Address'] = content
        elif 'Employment Income' in title:
            infoDiction['Employment Income'] = content
        elif 'Income tax deducted' in title:
            infoDiction['Income tax deducted'] = content
        elif 'CPP contributions' in title:
            infoDiction['CPP contributions'] = content
        elif 'Employee EI premiums' in title:
            infoDiction['Employee EI premiums'] = content
        elif 'Registered Pension Plan' in title:
            infoDiction['Registered Pension Plan'] = content
        elif 'Annual union dues' in title:
            infoDiction['Annual union dues'] = content
        elif 'Pension Adjustment' in title:
            infoDiction['Pension Adjustment'] = content
        elif 'Canadian Armed Forces' in title:
            infoDiction['Canadian Armed Forces'] = content
        elif 'Unused federal tuition' in title:
            infoDiction['Unused federal tuition'] = content
        elif '2021 Tuition Fee' in title:
            infoDiction['2021 Tuition Fee'] = content
        elif 'CWB advanced payment' in title:
            infoDiction['CWB advanced payment'] = content
        elif 'Donation to Charities' in title:
            infoDiction['Donation to Charities'] = content
        elif 'Donation to government bodies' in title:
            infoDiction['Donation to government bodies'] = content
        elif 'Donation to universities outside Canada' in title:
            infoDiction['Donation to universities outside Canada'] = content
        elif 'Donation to United Nations' in title:
            infoDiction['Donation to United Nations'] = content
        info = tax_info.readline()
    tax_info.close()
    return infoDiction


def get_EXCEL_info():
    book = openpyxl.load_workbook('Tax_information.xlsx')
    sheet = book.active
    infoDiction = dict()
    infoDiction['Name'] = sheet['C3'].value
    infoDiction['SIN'] = sheet['C4'].value
    if infoDiction['SIN'] > 999999999 or infoDiction['SIN'] < 100000000:
        raise ValueError('Incorrect length of SIN number.')
    dob = sheet['C5'].value
    infoDiction['Date of Birth'] = str(dob.year)
    infoDiction['Province'] = sheet['C6'].value
    province = sheet['C6'].value
    if province == 'Alberta' or province == 'AB':
        infoDiction['Province'] = 'AB'
    elif province == 'British Columbia' or province == 'BC':
        infoDiction['Province'] = 'BC'
    elif province == 'Manitoba' or province == 'MB':
        infoDiction['Province'] = 'MB'
    elif province == 'New Brunswick' or province == 'NB':
        infoDiction['Province'] = 'NB'
    elif province == 'Newfoundland' or province == 'NL' or province == 'Newfoundland and Labrador':
        infoDiction['Province'] = 'NL'
    elif province == 'Nova Scotia' or province == 'NS':
        infoDiction['Province'] = 'NS'
    elif province == 'Northwest Territories' or province == 'NT':
        infoDiction['Province'] = 'NT'
    elif province == 'Nunavut' or province == 'NU':
        infoDiction['Province'] = 'NU'
    elif province == 'Ontario' or province == 'ON':
        infoDiction['Province'] = 'ON'
    elif province == 'Prince Edward Island' or province == 'PE':
        infoDiction['Province'] = 'PE'
    elif province == 'Quebec' or province == 'QC':
        print('Sorry, this tax calculator do not work on Quebec Tax.')
        raise ValueError('Please enter a province except Quebec.')
    elif province == 'Saskatchewan' or province == 'SK':
        infoDiction['Province'] = 'SK'
    elif province == 'Yukon' or province == 'YT':
        infoDiction['Province'] = 'YT'
    else:
        raise ValueError('The province value is wrong, please enter a reasonable province.')
    infoDiction['Mailing Address'] = sheet['C7'].value
    infoDiction['Email Address'] = sheet['C8'].value
    infoDiction['Employment Income'] = sheet['C10'].value
    infoDiction['Income tax deducted'] = sheet['C11'].value
    infoDiction['CPP contributions'] = sheet['C12'].value
    infoDiction['Employee EI premiums'] = sheet['C13'].value
    infoDiction['Registered Pension Plan'] = sheet['C14'].value
    infoDiction['Annual union dues'] = sheet['C15'].value
    infoDiction['Pension Adjustment'] = sheet['C16'].value
    infoDiction['Canadian Armed Forces'] = sheet['C17'].value
    infoDiction['Unused federal tuition'] = sheet['C19'].value
    infoDiction['2021 Tuition Fee'] = sheet['C20'].value
    infoDiction['CWB advanced payment'] = sheet['C22'].value
    infoDiction['Donation to Charities'] = sheet['C24'].value
    infoDiction['Donation to government bodies'] = sheet['C25'].value
    infoDiction['Donation to universities outside Canada'] = sheet['C26'].value
    infoDiction['Donation to United Nations'] = sheet['C27'].value
    book.close()
    return infoDiction


def main():
    choice = None
    dic = None
    while choice != 'txt' and choice != 'excel':
        choice = input('Please enter the source of Tax information (txt or excel): ')
        choice = choice.lower()
    if choice == 'txt':
        dic = get_TXT_info()
    elif choice == 'excel':
        dic = get_EXCEL_info()
    name = dic['Name']
    refund, balanceOwing = FederalTaxCalculation.FederalTaxCal(dic).calculation()
    if refund > 0:
        print('Hello ' + name + ',\nBase on your information entered, you will have a refund for 2021 tax.\n'
                                'The refund amount is: $' + format(refund, '.2f'))
    elif balanceOwing > 0:
        print('Hello ' + name + ',\nBase on your information entered, you have a balance owing for 2021 tax.\n'
                                'The balance owing is: $' + format(balanceOwing, '.2f'))


main()
