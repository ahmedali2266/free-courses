import webbrowser

class free_courses:
    def __init__(self):
        print('Welcome to the free course program developed by Ahmed Ali')
        print('This program searches for all available free courses for you')
        print('---------------------------------------------------------------')
        self.chooses()


    def chooses(self):
        print ('1-Udemy','\n','2-Udacity')
        print('Please select the platform number')
        while True:
            user_choice=input('Enter your choice ... If you want to exit, enter C : ')
            if user_choice == 'c':
                print('Thanks for trying, I hope you come back again  ( ˘ ³˘)♥')
                break

            try:
                user_choice=int(user_choice)
                if user_choice == 1:
                    self.udemy()
                elif user_choice == 2:
                    self.udacity()
                else:
                    print('please choice 1 or 2')
                    

            except ValueError:
                print('please Enter A valid number')
                
                                    

    def udemy(self):
        print('--------------------------------------------------------')
        print("You have chosen the Udemy platform to search in")
        print('--------------------------------------------------------')
        courses=(
        '1-Development courses'
        ,'2-Business Courses','3-Finance & Accounting'
        ,'4-IT & Software','5-Office Productivity'
        ,'6-Personal Development','7-Design','8-Marketing'
        ,'9-Lifestyle','10-Photography',
        '11-Health & Fitness','12-Music'
        ,'13-Teaching & Academics')

        data_links={1:'https://www.udemy.com/courses/development/?price=price-free&sort=popularity',

        2:'https://www.udemy.com/courses/business/?price=price-free&sort=popularity',

        3:'https://www.udemy.com/courses/finance-and-accounting/?duration=long&price=price-free&sort=popularity',

        4:'https://www.udemy.com/courses/it-and-software/?price=price-free&sort=popularity',

        5:'https://www.udemy.com/courses/office-productivity/?price=price-free&sort=popularity',

        6:'https://www.udemy.com/courses/personal-development/?price=price-free&sort=popularity',

        7:'https://www.udemy.com/courses/design/?price=price-free&sort=popularity',

        8:'https://www.udemy.com/courses/marketing/?price=price-free&sort=popularity',

        9:'https://www.udemy.com/courses/lifestyle/?price=price-free&sort=popularity',

        10:'https://www.udemy.com/courses/photography/?price=price-free&sort=popularity',

        11:'https://www.udemy.com/courses/health-and-fitness/?price=price-free&sort=popularity',

        12:'udemy.com/courses/music/?price=price-free&sort=popularity',

        13:'https://www.udemy.com/courses/teaching-and-academics/?price=price-free&sort=popularity'}
        for item in courses:
            print (item)

        while True:
            user_chose=input( "now choose which course you want,To exit enter <X> :>> ")

            if user_chose == 'x':
                print ('Thanks for trying, I hope you come back again  ( ˘ ³˘)♥')
                break

            try:
                user_chose=int(user_chose)
                if user_chose > 0 and user_chose <= 13:
                    print(webbrowser.open(data_links[user_chose]))
                else:
                    print('please choice between 1 ,13 ')

            except ValueError:
                print('please Enter A valid number')


    


    def udacity(self):
        print('--------------------------------------------------------')
        print('You have chosen the Udemy platform to search in')
        print('--------------------------------------------------------')

        courses_udeasty=('1-Android','2-Artificial Intelligence','3-Data Analysis','4-Machine Learning')

        data_links2={1:'https://www.udacity.com/courses/all?type=free%20courses&skill=Android',2:'https://www.udacity.com/courses/all?type=free%20courses&skill=Artificial%20Intelligence',
        3:'https://www.udacity.com/courses/all?type=free%20courses&skill=Data%20Analysis',4:'https://www.udacity.com/courses/all?type=free%20courses&skill=Machine%20Learning'}
        for item in courses_udeasty:
            print(item)

        while True:
            user_chose2=input( "now choose which course you want,To exit enter <X> :>> ")

            if user_chose2 == 'x':
                print ('Thanks for trying, I hope you come back again  ( ˘ ³˘)♥')
                break

            try:
                user_chose2=int(user_chose2)
                if user_chose2 > 0 and user_chose2 <= 4:
                    print(webbrowser.open(data_links2[user_chose2]))
                else:
                    print('please choice between 1 ,13 ')

            except ValueError:
                print('please Enter A valid number')

        


objectt=free_courses()
