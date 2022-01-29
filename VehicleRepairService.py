from math import ceil

class Bills():

    customerCareNumber = '+012 12472 47247'
    standardRepairCost = 2000
    branchManagerNumber = '+91 96789 45887'
    branchPaymentsNumber = '+91 96482 48574'

    def __init__(self):
        print('Welcome to Showroom')
        print('Enter Customer ID and name in consecutive lines')
        self.customerID = input()
        self.customerName = input()
        print('Enter your mobile number here : ')
        self.mobileNumber = input()
        print('Enter your Car model :')
        self.carModel = input()
        print('Enter damage rate(1-100) :')
        self.carDamage = int(input())
        print('Do you want to claim insurance(Y/N) : ')
        self.insuranceClaim = input()
        if(self.insuranceClaim=='Y'):
            print('Enter your Insurance company name : ')
            self.insuranceCompanyName = input()
            print('Please enter insurance claim value here(0-100) : ')
            self.insuranceClaimValue = int(input())
        else:
            self.insuranceClaimValue = 0
        print('You will be redirected to our Service branch ..Please wait...')
        for i in range (100):
            print('...',end="")
        print()
        self.serviceBranch()
        
        print("Thanks for coming. Please visit us again!")
        print('---Session ended---')

    def serviceBranch(self):
        print('Welcome to Service branch')
        print('Please enter your CID here :')
        self.CID = input()
        if(self.CID!=self.customerID):
            print('Sorry Your CID doesnt match with our Order list..Please contact Customer Care')
            self.customerCare()
        else:
            print('This may take a while to fetch your order details...')
            print("Let's check your order details :")
            print('Name :',self.customerName)
            print('Car model : ',self.carModel)
            print('Car damage rate: ',self.carDamage)
            if self.insuranceClaim=='Y':
                print('Insurance company name : ',self.insuranceCompanyName)
                print('Insurance claim value',self.insuranceClaimValue)
            else :
                print('Insurance company name : NA')
                print('Insurance claim value : 0%')
            print('Please check your details once and give an acknowledgement here (Y/N): ')
            self.customerAcknowledgement = input()
            if self.customerAcknowledgement == 'N' :
                self.customerCare()
            else:
                print("Thank you for your acknowledgent!")
                print('Here are your bill details')
                print('Car damage : ',self.carDamage, '              Standard repair cost = 2000 per damage point')
                print('Your damage repair cost = ',self.carDamage*2000)
                print('After applying Tax (22%) : ',int(self.carDamage*2000*1.22))
                print('After applying service Tax (8%) : ',int(self.carDamage*2000*1.3))
                print('Insurance claim points :{}% '.format(self.insuranceClaimValue))
                print('Total amount to be paid :',ceil(self.carDamage*2000*(1.3-(self.insuranceClaimValue/100))))
                print('You are most welcome if you want to clarify something about the bill amount(Y/N) :')
                self.customerBillAcknowledgent = input()
                if self.customerBillAcknowledgent == 'Y':
                    self.branchManager()
                else :
                    print('Thank you for your clarification.. You will be redirected to payments section')
                    self.paymentsSection()
    
    def customerCare(self):
        print('Would you like to call the customer care? (Y/N) :')
        self.CCYN = input() 
        if(self.CCYN=='Y'):
            print('Customer care number : ',Bills.customerCareNumber)
    
    def branchManager(self):
        print('Woud you like to contact the branch manager regarding the bill amount? (Y/N) : ')
        self.branchManagerAcknowledgent = input()
        if self.branchManagerAcknowledgent=='Y' :
            print("Branch manager's contact number : ",Bills.branchManagerNumber)
                    
    def paymentsSection(self):
        print('Welcome to payments section')
        print('////////////////////////////////////////  We are afraid but  ////////////////////////////////////////')
        print('/////////////////////////  the payments section is still under development  /////////////////////////')
        print('You may pay online to this number : ',Bills.branchPaymentsNumber)
        print('\n\n\nCustomer Care Number : ',self.customerCareNumber)
        print('Branch Manager contact number : ',self.branchManagerNumber)


def main():
    bill1 = Bills()
    

main()