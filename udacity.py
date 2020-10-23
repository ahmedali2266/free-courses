import webbrowser

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
