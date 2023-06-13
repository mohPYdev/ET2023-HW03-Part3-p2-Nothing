from scenarios import wagon, boat, lying, mendacity, libel, false_negative_rumor, false_positive_rumor



def main():

    while True:
        print('press e to exit')
        print('1: wagon\n 2: boat \n 3: lying \n 4: mendacity \n 5: libel \n 6: false_negative_rumor \n 7: false_positive_rumor')
        a = input('which scenario do you want?(1,2,3,4,5,6,7)')

        if a == 'e':
            break
        
        a = int(a)

        if a == 1:
            wagon()

        elif a == 2:
            boat()

        elif a == 3:
            lying()
        elif a == 4:

            mendacity()

        elif a == 5:

            libel()

        elif a == 6:

            false_negative_rumor()

        elif a == 7:

            false_positive_rumor()



if __name__ == '__main__':
    main()