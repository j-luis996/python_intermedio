def main():
    my_list = [1,"hello",True,4.5]
    my_dict = {'fistname' : 'luis', 'lastname':'martinez'}

    super_list = [
        {'firstname' : 'luis', 'lastname':'martinez'},
        {'firstname' : 'lizette', 'lastname':'martinez'},
        {'firstname' : 'dalia', 'lastname':'martinez'}
    ]

    for i in super_list:
        for key, values in i.items():
            print(f'{key}: {values}')
        print('##########')

if __name__ == '__main__':
    main()