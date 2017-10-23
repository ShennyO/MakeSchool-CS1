def loadFile():

    money = 0

    with open('sales_data.txt', 'r+') as f:
        sales_data = f.readlines()
        list_sales_data = list(sales_data)
        output = []
        for one_sale in list_sales_data:
            one_sale = one_sale.replace("$", '')
            one_sale = one_sale.replace('\n', '')
            one_sale = one_sale.split('\t')
            output.append(one_sale)

        for index in output:
            money += float(index[3])

        months = []
        moddedMonths = []
        february = []

        for index in output:
            months.append(index[1])

        for x in months:
            x = x.split('/')
            moddedMonths.append(x)

        for number, month in enumerate(moddedMonths):
            if month[0] == '2':
                february.append(output[number])
#First i have to organize to get only the sales made in february, ok I got all the february shits
#Next step: I have to loop through each array, have a word bank of cities, if the first index
#is not in my word bank, create city variable equal to 0, then add the city to my city bank
        city = {}
        for sale in february:
            if sale[0] not in city:

                city[sale[0]] = 0
            else:
                city[sale[0]] += float(sale[3])

        baller = 0

        for loc, value in city.items():
            if value > baller:
                baller = value

        for loc, value in city.items():
            if value == baller:
                print(loc)
        cash = 0
        #next is the total amount of cash, so what do i need? I need to organize everything by cash, then just add up all the numbers
        for x in output:
            if x[2] == 'Cash':
                cash += float(x[3])
        #Now what is the most popular form of payment in march in oakland?
        #Need to organize everything by march and oakland first,

        payments = {}
        for number, indiv in enumerate(output):
            if indiv[0] == 'Oakland' and moddedMonths[number][0] == '3':
                if indiv[2] not in payments:
                    payments[indiv[2]] = 0
                    payments[indiv[2]] += 1

                else:
                    payments[indiv[2]] += 1

        highest = 0
        for form in payments:
            if payments[form] > highest:
                highest = payments[form]

        best_payment = ""
        for best in payments:
            if payments[best] == highest:
                best_payment = best

        #Now we want to see which city had the most sales value on 4/20 and see the total sales amount on 4/20
        #first we have to organize everything by 4/20

        four_twenty = []

        for index, sale in enumerate(output):
            if months[index] == '4/20':
                four_twenty.append(sale)

        print(four_twenty)

        four_twenty_dict = {}
        four_twenty_value = 0

        for sale in four_twenty:
            if sale[0] not in four_twenty_dict:
                four_twenty_dict[sale[0]] = 0
                four_twenty_dict[sale[0]] += float(sale[3])
            else:
                four_twenty_dict[sale[0]] += float(sale[3])

        for sale in four_twenty_dict:
            if four_twenty_dict[sale] > four_twenty_value:
                four_twenty_value = four_twenty_dict[sale]

        for sale in four_twenty_dict:
            if four_twenty_dict[sale] == four_twenty_value:
                print(sale)

        credit_card = []
        baseball_cards = []
        #What is the average sales amount for credit card purchases?
        #Get the total sales amount for credit card and then divide it by the count of sales with credit cards

        for sale in output:
            if sale[2] == 'Credit':
                credit_card.append(sale)
        avg_credit_val = 0

        for index in credit_card:
            avg_credit_val += float(index[3])

        avg_credit_val = avg_credit_val/len(credit_card)

        for sale in output:
            if sale[2] == 'Baseball Cards':
                baseball_cards.append(sale)




    # print(avg_credit_val)


        #How many purchases were made by bartering with baseball cards?



    print(len(baseball_cards))




    # print(len(four_twenty))
    #
    # print(payments)
    # print(four_twenty)




    # print(four_twenty_value)














    # print(money)
    #
    # # print(city)
    # # print(output)
    # print(cash)
    # print(best_payment)
    # print(months)








loadFile()
