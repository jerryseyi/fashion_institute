
class DebsFs:

    """
    Debs Fashion institute
    we nasdf
    program 2.1
    jadsf dasf
    fdsjdsa ubdsf
     sdfdaas eadfgefd
     frdkg rfedgersm
    """

    robot = 'jedidiah'
    choice_of_styles = """
    ***()==()==()==()==()==()==***
       please choose your styles
    ***()==()==()==()==()==()==***
    """
    choice_of_course = """
    ***==()==()==()==()==()==()==()==()==()==***
          please choose your field of study
    ***==()==()==()==()==()==()==()==()==()==***
    """
    account_details = """
    ***()==()==()==()==()==()==***
             Skye Bank
            02322143122
             Gtb Bank
            0231434353
            First Bank
            90234723542
    ***()==()==()==()==()==()==***
    """

    def __init__(self):
        print(
            """
            *********************************************************
            *         WELCOME TO DEBS FASHION INSTITUTE             *
            * Here We Teach You All You Need TO Know About Fashion  *
            *********************************************************
            """
        )

        self.location = "\t\t\t\t\tWe are situated at manor estate, VGC, LAGOS"
        print(self.location)
        print()
        self.styles = """
                        <====> Native attires for men <====>
                        
                            Buba & Soro = #5000
                            Dansiki     = #7500
                            Agbada      = #12000
                            
                        <====> Native attires for women <====>
                        
                            Iro & Buba   = #5000
                            Aso Oke      = #6000
                            Aso Ofi      = #7500
                            
                        <====> English attires for men <====>
                        
                            Shirt & Trouser     = #8000
                            Customised Tshirt   = #5000
                            Blazers             = #15000
                            Suit                = #50000
                            
                        <====> English attires for women <====>
                        
                            Gown                = #8000
                            Skirt & Blouse      = #7500
                            suit                = #35000
                        """
        print(self.styles)

        self.training = """
                         Our Training is segmented into three classes. 
                        We take you from nothingness to being an expert
                        
                                Beginners Class     = #200000
                                Intermediate Class  = #500000
                                Expert Class        = #1000000
        """
        print(self.training)

    def customer(self):
        name = input("Please provide your full name => ")
        print("You are welcome," + name + " i am " + self.robot + " and i am your guide")
        purpose = input("Please state your purpose of visit: Academy/Shopping => ")
        if purpose.lower() == 'shopping':
            self.fashion_sense()
        elif purpose.lower() == 'academy':
            self.academy()

    def academy(self):
        print(self.choice_of_course)
        print(self.training)
        aspired_course = input("Please Enter the Course you would love to do => ")
        if aspired_course.lower() == 'beginners class':
            beginners_class = 200000
            print("You are expected to pay a sum of ", beginners_class, " naira to the following bank::")
            print(self.account_details)
            print("Note: We don't receive part payment, we receive our morning in full")
            print("Bring the teller once you have paid and you will commence the class")
            print("Money is Non Refundable, You lost your teller, You are one on your own")
            print("please be wise")
            print("Don't come and cry, we'll turn a blind eye...")
        elif aspired_course.lower() == 'intermediate class':
            intermediate_class = 500000
            print("You are expected to pay a sum of ", intermediate_class, " naira to the following bank::")
            print(self.account_details)
            print("Note: We don't receive part payment, we receive our morning in full")
            print("Bring the teller once you have paid and you will commence the class")
            print("Money is Non Refundable, You lost your teller, You are one on your own")
            print("please be wise")
            print("Don't come and cry, we'll turn a blind eye...")
        elif aspired_course.lower() == 'expert class':
            expert_class = 1000000
            print("You are expected to pay a sum of ", expert_class, " naira to the following bank::")
            print(self.account_details)
            print("Note: We don't receive part payment, we receive our morning in full")
            print("Bring the teller once you have paid and you will commence the class")
            print("Money is Non Refundable, You lost your teller, You are one on your own")
            print("please be wise")
            print("Don't come and cry, we'll turn a blind eye...")
        else:
            print("<==> You are not eligible <===>")

    def fashion_sense(self):

        print(self.choice_of_styles)

        sex_of_cloth = input("You are welcome, which cloth do you want to buy, Men or Women ? ")
        if sex_of_cloth.lower() == 'men':
            section = input("Which section are you going, English or Native ? ")
            if section.lower() == 'native':
                Buba_Soro = 5000
                Dansiki = 7500
                Agbada = 12000

                print("""
                    Here in this section we have :
                                    Buba and Soro -> #5000
                                    Dansiki -> #7500
                                    Agbada -> #12000
                """)
                select_type = input("Please select the one you would like to buy : ")
                if select_type.lower() == 'buba and soro':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = Buba_Soro * quantity
                    print("\t\t\tThe total cost of the Buba and Soro you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                elif select_type.lower() == 'dansiki':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = Dansiki * quantity
                    print("\t\t\tThe total cost of the Dansiki you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                elif select_type.lower() == 'agbada':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = Agbada * quantity
                    print("\t\t\tThe total cost of the Agbada you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                else:
                    print(" <=> Incorrect Selection <=>")

            elif section.lower() == 'english':
                Shirt_Trouser = 8000
                Customized_Tshirt = 5000
                Blazers = 15000
                Suit = 50000

                print("""
                    Here in this section we have :
                                    Shirt and Trouser -> #8000
                                    Customized Tshirt -> #5000
                                    Blazers -> #15000
                                    Suit -> #50000
                """)
                select_type2 = input("Please select the one you would like to buy : ")
                if select_type2.lower() == 'shirt and trouser':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = Shirt_Trouser * quantity
                    print("\t\t\tThe total cost of the Shirt and Trouser you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                elif select_type2.lower() == 'customized tshirt':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = Customized_Tshirt * quantity
                    print("\t\t\tThe total cost of the Customized Tshirt you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                elif select_type2.lower() == 'blazers':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = Blazers * quantity
                    print("\t\t\tThe total cost of the Blazers you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                elif select_type2.lower() == 'suit':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = Suit * quantity
                    print("\t\t\tThe total cost of the Suit you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                else:
                    print(" <=> Incorrect Selection <=>")
            else:
                print("++++ Sorry we have no wears for the culture you seek +++")

        elif sex_of_cloth.lower() == 'women':
            section = input("Which section are you going, English or Native ? ")
            if section.lower() == 'native':
                iro_buba = 5000
                aso_oke = 6000
                aso_ofi = 75000

                print("""
                                Here in this section we have :
                                                iro and buba -> #5000
                                                aso oke -> #6000
                                                aso ofi -> #75000
                            """)
                select_type = input("Please select the one you would like to buy : ")
                if select_type.lower() == 'iro and buba':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = iro_buba * quantity
                    print("\t\t\tThe total cost of the iro and buba you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                elif select_type.lower() == 'aso oke':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = aso_oke * quantity
                    print("\t\t\tThe total cost of the aso oke you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                elif select_type.lower() == 'aso ofi':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = aso_ofi * quantity
                    print("\t\t\tThe total cost of the aso ofi you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                else:
                    print(" <=> Incorrect Selection <=>")

            if section.lower() == 'english':
                gown = 8000
                skirt_blouse = 7500
                suit = 35000

                print("""
                                Here in this section we have :
                                                Gown -> #8000
                                                Skirt and Blouse -> #7500
                                                Suit -> #35000
                            """)
                select_type = input("Please select the one you would like to buy : ")
                if select_type.lower() == 'gown':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = gown * quantity
                    print("\t\t\tThe total cost of the gown you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                elif select_type.lower() == 'skirt and blouse':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = skirt_blouse * quantity
                    print("\t\t\tThe total cost of the skirt and blouse you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                elif select_type.lower() == 'suit':
                    quantity = int(input("How many would you love to buy ? "))
                    cost = suit * quantity
                    print("\t\t\tThe total cost of the suit you bought is ", cost, " Naira")
                    print("**=.=.=Thank you for shopping with us, we expect you next time =.=.=**")
                else:
                    print(" <=> Incorrect Selection <=>")
            else:
                print("++++ Sorry we have no wears for the culture you seek +++")
        else:
            print("===> we only sell male or female clothes here, No alien clothes ===>")


nc = DebsFs()

nc.customer()



