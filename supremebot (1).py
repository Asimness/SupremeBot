from splinter import Browser
from Tkinter import *
import tkFont
import string
import os
import sys
import Tix as tk
import time
#import selenium
#from selenium import webdriver
count = 0
countCheck = 1
    #User input
def getNameInput():
    return name.get()
def getEmailInput():
    return email.get()
def getPhoneInput():
    return phone.get()
def getAddressInput():
    return address.get()
def getZipCodeInput():
    return zipcode.get()
def getCityInput():
    return city.get()
def getStateInput():
    return state.get()
def getSizeOneInput():
    return sizeOne.get()
def getSizeTwoInput():
    return sizeTwo.get()
def getSizeThreeInput():
    return sizeThree.get()
def getCreditCardTypeInput():
    return creditCardType.get()
def getCreditCardNumberInput():
    return creditCardNumber.get()
def getMonthInput():
    return month.get()
def getYearInput():
    return year.get()
def getSecurityNumberInput():
    return securityNumber.get()
def closeUserInfo():
    userInfo.destroy()
def getZipCodeTryTwo():
    return zipcodeTryTwo.get()
def getItemOne():
    #if len(itemOne.get()) >= 1:
        #global count
        #count = count + 1
        #global countCheck
        #countCheck = countCheck + 1
    return itemOne.get()
def getItemTwo():
    #if len(itemTwo.get()) >= 1:
        #global count
        #count = count + 1
        #global countCheck
        #countCheck = countCheck + 1
    return itemTwo.get()
def getItemThree():
    #if len(itemThree.get()) >= 1:
        #global count
        #count = count + 1
        #global countCheck
        #countCheck = countCheck + 1
    return itemThree.get()

userInfo = tk.Tk()
name = StringVar()
email = StringVar()
phone = StringVar()
address = StringVar()
zipcode = StringVar()
city = StringVar()
state = StringVar()
sizeOne = StringVar()
sizeTwo = StringVar()
sizeThree = StringVar()
creditCardType = StringVar()
creditCardNumber = StringVar()
month = StringVar()
year = StringVar()
securityNumber = StringVar()
zipcodeTryTwo = StringVar()
itemOne = StringVar()
itemTwo = StringVar()
itemThree = StringVar()

userInfo.geometry("600x900")
sw= tk.ScrolledWindow(userInfo, scrollbar=tk.Y) # just the vertical scrollbar
sw.pack(fill=tk.BOTH, expand=1)
nameLabel = tk.Label(sw.window, text = "Enter full name").pack()
nameEntry = tk.Entry(sw.window, textvariable = name).pack()

emailLabel = tk.Label(sw.window, text = "Enter Email").pack()
emailEntry = tk.Entry(sw.window, textvariable = email).pack()

phoneLabel = tk.Label(sw.window, text = "Enter phone number").pack()
phoneEntry = tk.Entry(sw.window, textvariable = phone).pack()

addressLabel = tk.Label(sw.window, text = "Enter address").pack()
addressEntry = tk.Entry(sw.window, textvariable = address).pack()

zipcodeLabel = tk.Label(sw.window, text = "Enter 5 digit zipcode").pack()
zipcodeEntry = tk.Entry(sw.window, textvariable = zipcode).pack()

cityLabel = tk.Label(sw.window, text = "Enter City").pack()
cityEntry = tk.Entry(sw.window, textvariable = city).pack()

stateLabel = tk.Label(sw.window, text = "Enter State (TX)").pack()
stateEntry = tk.Entry(sw.window, textvariable = state).pack()

sizeOneLabel = tk.Label(sw.window, text = "Chose a size for item one").pack()
sizeOneRadiobutton = Radiobutton(sw.window, text="S", variable = sizeOne, value="S").pack(anchor=CENTER)
sizeOneRadiobutton = Radiobutton(sw.window, text="M", variable = sizeOne, value="M").pack(anchor=CENTER)
sizeOneRadiobutton = Radiobutton(sw.window, text="L", variable = sizeOne, value="L").pack(anchor=CENTER)
sizeOneRadiobutton = Radiobutton(sw.window, text="X", variable = sizeOne, value="X").pack(anchor=CENTER)

sizeTwoLabel = tk.Label(sw.window, text = "Chose a size for item two").pack()
sizeTwoRadiobutton = Radiobutton(sw.window, text="S", variable = sizeTwo, value="S").pack(anchor=CENTER)
sizeTwoRadiobutton = Radiobutton(sw.window, text="M", variable = sizeTwo, value="M").pack(anchor=CENTER)
sizeTwoRadiobutton = Radiobutton(sw.window, text="L", variable = sizeTwo, value="L").pack(anchor=CENTER)
sizeTwoRadiobutton = Radiobutton(sw.window, text="X", variable = sizeTwo, value="XL").pack(anchor=CENTER)

sizeThreeLabel = tk.Label(sw.window, text = "Chose a size for item three").pack()
sizeThreeRadiobutton = Radiobutton(sw.window, text="S", variable = sizeThree, value="S").pack(anchor=CENTER)
sizeThreeRadiobutton = Radiobutton(sw.window, text="M", variable = sizeThree, value="M").pack(anchor=CENTER)
sizeThreeRadiobutton = Radiobutton(sw.window, text="L", variable = sizeThree, value="L").pack(anchor=CENTER)
sizeThreeRadiobutton = Radiobutton(sw.window, text="X", variable = sizeThree, value="XL").pack(anchor=CENTER)

itemOneLabel = tk.Label(sw.window, text = "Enter the number for item one").pack()
itemOneEntry = tk.Entry(sw.window, textvariable = itemOne).pack()

itemTwoLabel = tk.Label(sw.window, text = "Enter the number for item one").pack()
itemTwoEntry = tk.Entry(sw.window, textvariable = itemTwo).pack()

itemThreeLabel = tk.Label(sw.window, text = "Enter the number for item one").pack()
itemThreeEntry = tk.Entry(sw.window, textvariable = itemThree).pack()

creditCardTypeLabel= tk.Label(sw.window, text = "Chose Type of credit card").pack()
sizeOneRadiobutton = Radiobutton(sw.window, text="Visa", variable = creditCardType, value="V").pack(anchor=CENTER)
sizeOneRadiobutton = Radiobutton(sw.window, text="American Express", variable = creditCardType, value="A").pack(anchor=CENTER)
sizeOneRadiobutton = Radiobutton(sw.window, text="Mastercard", variable = creditCardType, value="M").pack(anchor=CENTER)
#creditCardTypeEntry = tk.Entry(userInfo, textvariable = creditCardType).pack()

creditCardNumberLabel = tk.Label(sw.window, text = "Enter credit card number").pack()
creditCardNumberEntry = tk.Entry(sw.window, textvariable = creditCardNumber).pack()

monthLabel = tk.Label(sw.window, text = "Enter Month (2 digit)").pack()
monthEntry = tk.Entry(sw.window, textvariable = month).pack()

yearLabel = tk.Label(sw.window, text = "Enter year (2019)").pack()
yearEntry = tk.Entry(sw.window, textvariable = year).pack()

securityNumberLabel = tk.Label(sw.window, text = "Enter Security Number").pack()
securityNumberEntry = tk.Entry(sw.window, textvariable = securityNumber).pack()

copLabel = tk.Label(sw.window, text = "You're About To Press the Ye Button!").pack()
yeButton = tk.Button(sw.window, text = 'Supreme', command = closeUserInfo, fg = 'red', bg = 'blue').pack()

userInfo.mainloop()

fillName = getNameInput()
#print fillName
fillEmail = getEmailInput()
#print fillEmail
fillPhone = getPhoneInput()
#print fillPhone
fillAddress = getAddressInput()
#print fillAddress
fillZipCode = getZipCodeInput()
#print fillZipCode
fillCity = getCityInput()
#print fillCity
fillState = getStateInput()
#print fillState

#fill sizes
fillSizeOne = getSizeOneInput()
if fillSizeOne == "S":
    fillSizeOne = "Small"
elif fillSizeOne == "M":
    fillSizeOne = "Medium"
elif fillSizeOne == "L":
    fillSizeOne = "Large"
else:
    fillSizeOne = "X-Large"

fillSizeTwo = getSizeTwoInput()
if fillSizeTwo == "S":
    fillSizeTwo = "Small"
elif fillSizeTwo == "M":
    fillSizeTwo = "Medium"
elif fillSizeTwo == "L":
    fillSizeTwo = "Large"
else:
    fillSizeTwo = "X-Large"

fillSizeThree = getSizeThreeInput()
if fillSizeThree == "S":
    fillSizeThree = "Small"
elif fillSizeThree == "M":
    fillSizeThree = "Medium"
elif fillSizeThree == "L":
    fillSizeThree = "Large"
else:
    fillSizeThree = "X-Large"

#print fillSize
fillCreditCardType = getCreditCardTypeInput()
#print fillCreditCardType
fillCreditCardNumber = getCreditCardNumberInput()
#print fillCreditCardNumber
fillMonth = getMonthInput()
#print fillMonth
fillYear = getYearInput()
#print fillYear
fillSecurityNumber = getSecurityNumberInput()
#print fillSecurityNumber

#zipcode = raw_input()
#if len(zipcode) < 5:
#    print "Type in a real zip code, you moron"
#    print "Here's another try: Zip Code: ",
#    raw_input()

if fillCreditCardType == "V":
    fillCreditCardType = '//*[@id="credit_card_type"]/option[1]'
elif fillCreditCardType == "A":
   fillCreditCardType = '//*[@id="credit_card_type"]/option[2]'
else:
   fillCreditCardType = '//*[@id="credit_card_type"]/option[3]'

fillItemOne = '//*[@id="container"]/article[' + itemOne.get() + ']/div/a/img'
fillItemTwo = '//*[@id="container"]/article[' + itemTwo.get() + ']/div/a/img'
fillItemThree = '//*[@id="container"]/article[' + itemThree.get() + ']/div/a/img'

if len(fillItemOne) > 40:
    count = count + 1
    countCheck += 1
if len(fillItemTwo) > 40:
    count = count + 1
    countCheck += 1
if len(fillItemThree) > 40:
    count = count + 1
    countCheck += 1

#if len.(fillItemOne) > 0:
    #count = count + 1
#if "20" not in year:
#    year = "20" + year
if count == 1:
    fillItemThree = fillItemOne
    fillSizeThree = fillSizeOne
if count == 2:
    fillSizeThree = fillSizeTwo
    fillSizeTwo = fillSizeOne
    fillItemThree = fillItemTwo
    fillItemTwo = fillItemOne
    #Going to website


    #for selenium
#driver = webdriver.Chrome("C:\Users\Asimness\Desktop\chrome_driver\chromedriver.exe")

browser = Browser('chrome')
while count < countCheck:
    #visit URL
    browser.visit('http://www.supremenewyork.com/shop/all/')
    #click item
    #browser.find_by_xpath('//*[@id="container"]/article[8]/div/a').click()
    if(count == 3):
        browser.find_by_xpath(fillItemOne).click()
        if browser.is_text_present(fillSizeOne):
            browser.find_option_by_text(fillSizeOne).first.click()
    if(count == 2):
        browser.find_by_xpath(fillItemTwo).click()
        if browser.is_text_present(fillSizeTwo):
            browser.find_option_by_text(fillSizeTwo).first.click()
        browser.find_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    if (count == 1):
        browser.find_by_xpath(fillItemThree).click()
        if browser.is_text_present(fillSizeThree):
            browser.find_option_by_text(fillSizeThree).first.click()
        count = 20

    browser.find_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    count = count - 1
    #click add to cart
    #browser.find_by_xpath('//*[@id="add-remove-buttons"]/input').click()

    #clicks checkout button
if browser.is_text_present('checkout now', wait_time =1):
    browser.find_by_xpath( '//*[@id="cart"]/a[2]').click()

    #filling out address
browser.fill('order[billing_name]', fillName )
browser.fill('order[email]' , fillEmail )
browser.fill('order[tel]' , fillPhone )
browser.fill('order[billing_address]' , fillAddress)
browser.fill('order[billing_zip]' , fillZipCode)
browser.fill('order[billing_city]' , fillCity )
browser.find_option_by_text( fillState ).click()
browser.find_option_by_text( "USA" ).first.click()

    #filling out credit card
browser.find_by_xpath(fillCreditCardType).click()
browser.fill('credit_card[cnb]' , fillCreditCardNumber)
browser.find_option_by_text(fillMonth).click()
browser.find_option_by_text(fillYear).click()
browser.fill('credit_card[vval]' , fillSecurityNumber)

    #clicks terms and agreement
browser.find_by_xpath ('//*[@id="cart-cc"]/fieldset/p[2]/label').click()

    #clicks process payment
#(Get Rid) browser.find_by_xpath ('//*[@id="pay"]/input').click()
