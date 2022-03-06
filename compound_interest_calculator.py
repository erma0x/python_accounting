import time
i0=1000  # initial investment
percent=0.025 # percentage of daily earnings
imensile=i0 # * percent + i0
day=1

print('\n Program that calculates profits with the expected percentage of profit over time \n')
	
def profit():
    initial_cap=int(input('enter the starting capital'))
    percent=float(input("the former percentage (8, for 8%) of earnings for each unit of time"))
    days=int(input("number of time units "))
    day=1
    percent=percent/100 #inserisco cosi' la percentuale espressa in %
    print('_'*30)
    visual=input("you want to display unit by unit ? y/n ")
    if str(visual)=='y' or str(visual)=='Y':
        print(" capital  |      unit  |")
    else:
        pass
    while day<days:
        cap += cap *percent
        day+=1
        if visual=='y' or visual=='Y':
            print(int(cap) ,' | ', day)

    print('_'*30)
    print('gross capital of  ' + str(int(round(cap))))
    print('percentage profit of ' + str(int(round(cap/initial_cap*100-100,2))) +' %')
    print('net profit of  ' + str(int(round(cap-initial_cap,0))) +" $ US Dollars")
    time.sleep(1)

while True:
    profit()
    do_you_exit=input('continue? y  /  n   ')
    print('_'*60)
    if do_you_exit=='n':
        break
