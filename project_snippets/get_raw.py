def see_raw_data(df):
    while True:
        get_raw = input('Would you like to see raw data\n' ).lower()
        if get_raw != 'yes':
            break
        else:
            see_raw(df)








def all_raw(df):
    while True:
        raw_true = input('Would you like to view raw data? yes/no \n')
        if raw_true != 'yes':
            break
        else:
            select_number = input('How mnay line sets would you like? 10, 30, 50')
            if select_number == 10:
                print(df.head(10))
            if select_number == 30:
                print(df.head(30))
            if select_number == 50:
                print(df.head(50))
            if select_number != 10 or select_number != 30 or select_number != 50:
                print('That is an invalid option, please try again')
                break





def see_raw(df):
    while True:
        select_lines = input('How  many lines would you like to review?:\n 10 \n 20 \n 50 \n')
        if select_lines == '10':
            print('you have selected the first 10 lines \n')
            print(df.head(10))
        if select_lines == '20':
            print('you have selected the first 20 lines \n')
            print(df.head(20))
        if select_lines == '30':
            print('you have selected the first 50 lines \n')
            print(df.head(50))
        if select_lines != '10' or '20' or '50':
            print('That is an invalid option, please try again')

        restart = input("Would you like to see more raw data? yes/no: \n" )
        if restart.lower() != 'yes':
            break
