from rules import rules

# assignment 3-3-a scenarios

def wagon():


    print("#####################     WAGON    #################################")

    a1 = 'pull the lever'
    a2 = 'do not pull the lever'

    c1 = '1 person dies'
    c2 = '5 people die'

    actions = (a1, a2)
    consequence = (c1, c2)

    equation = {a1: c1, a2: c2}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 6:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]

                elif i == 7:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be -{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 11:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 12:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 6:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be -{rules[i-1][1]}')
                    u -= rules[i-1][1]

                elif i == 7:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be -{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 11:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be -{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 12:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u

    print('\n actions are : ', actions)
    print('\n consequences are : ', consequence)

    
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')


    if u1 >= u2:
        print('the best action for the wagon scenario is : ' , a1)
        print('\n\n')
        print('the intension for this action is : ' , equation[a1])
        print('\n\n')
    else:
        print('the best action for the wagon scenario is : ' , a2)
        print('\n\n')
        print('the intension for this action is : ' , equation[a2])
        print('\n\n')
       

def boat():

    print("#####################     boat    #################################")

    a1 = 'to push the biggest person into water'
    a2 = 'to not push the biggest person into water'

    c1 = 'the boat drowns'
    c2 = 'the biggest person drowns'
    c3 = 'other 3 people drown'

    actions = (a1, a2)
    consequence = (c1, c2, c3)

    equation = {a2: [c1, c2,c3], a1: c2,}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 6:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 8:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 12:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 6:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 8:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 12:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u
    
    print('\n actions are : ', actions)
    print('\n consequences are : ', consequence)
    
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')


    if u1 >= u2:
        print('the best action for the boat scenario is : ' , a1)
        print('\n\n')
        print('the intension for this action is : ' , equation[a1])
        print('\n\n')
    else:
        print('the best action for the boat scenario is : ' , a2)
        print('\n\n')
        print('the intension for this action is : ' , equation[a2])
        print('\n\n')
    

def lying():


    print("#####################     lying    #################################")

    a1 = 'to lie to the elderly'
    a2 = 'not to lie to the elderly'

    c1 = 'create a false illusion into the mind of the elderly'
    c2 = 'elderly eats healthy food and exercises'
    c3 = 'elderly exercise every day'
    c4 = 'elderly has a healthy body due to eating healthy food and exercising'

    actions = (a1, a2)
    consequence = (c1, c2, c3, c4)

    equation = {a1: [c1,c2,c3,c4]}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 4:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 10:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 4:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 10:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u
    
    
    print('\n actions are : ', actions)
    print('\n consequences are : ', consequence)
    
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')

    if u1 >= u2:
        print('the best action for the lying scenario is : ' , a1)
        print('\n\n')
        print('the intension for this action is : ' , equation[a1])
        print('\n\n')




# assignment 3-3-b scenarios

def mendacity():
    
    print("#####################     lie    #################################")

    a1 = 'to lie'
    a2 = 'not to lie'

    c1 = 'the court is right'
    c2 = 'the court is wrong'


    actions = (a1, a2)
    consequence = (c1, c2)

    equation = {a1: c1, a2: c2}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 4:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 6:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 4:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 6:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u
    
    print('\n actions are : ', actions)
    print('\n consequences are : ', consequence)
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')


    if u1 >= u2:
        print('the best action for the lie scenario is : ' , a1)
        print('\n\n')
        print('the intension for this action is : ' , equation[a1])
        print('\n\n')
    else:
        print('the best action for the lie scenario is : ' , a2)
        print('\n\n')
        print('the intension for this action is : ' , equation[a2])
        print('\n\n')


def libel():
    
    
    print("#####################     libel    #################################")

    a1 = 'right testimony'
    a2 = 'wrong testimony'

    c1 = 'the court is right'
    c2 = 'the court is wrong'


    actions = (a1, a2)
    consequence = (c1, c2)

    equation = {a1: c1, a2: c2}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 4:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 8:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                
                elif i == 11:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 4:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 8:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]
                
                elif i == 11:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u

    print('\n actions are : ', actions)
    print('\n consequences are : ', consequence)
    
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')

    if u1 >= u2:
        print('the best action for the libel scenario is : ' , a1)
        print('\n\n')
        print('the intension for this action is : ' , equation[a1])
        print('\n\n')
    else:
        print('the best action for the libel scenario is : ' , a2)
        print('\n\n')
        print('the intension for this action is : ' , equation[a2])
        print('\n\n')


def false_positive_rumor():

 
    print("#####################     false positive rumor    #################################")

    a1 = 'wrong testimony'
    a2 = 'right testimony'

    c1 = 'the court is wrong'
    c2 = 'the court is right'


    actions = (a1, a2)
    consequence = (c1, c2)

    equation = {a1: c1, a2: c2}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 7:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]

                
                elif i == 11:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]

                elif i == 7:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                
                elif i == 11:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u

    print('\n actions are : ', actions)
    print('\n consequences are : ', consequence)
    
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')


    if u1 >= u2:
        print('the best action for the  false positive rumor scenario is : ' , a1)
        print('\n\n')
        print('the intension for this action is : ' , equation[a1])
        print('\n\n')
    else:
        print('the best action for the  false positive rumor scenario is : ' , a2)
        print('\n\n')
        print('the intension for this action is : ' , equation[a2])
        print('\n\n')


def false_negative_rumor():
 
    print("#####################     false negative rumor    #################################")

    a1 = 'wrong testimony'
    a2 = 'right testimony'

    c1 = 'the court is wrong'
    c2 = 'the court is right'


    actions = (a1, a2)
    consequence = (c1, c2)

    equation = {a1: c1, a2: c2}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 7:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]

                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]

                elif i == 7:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]

                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u
    
    print('\n actions are : ', actions)
    print('\n consequences are : ', consequence)
    
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')


    if u1 >= u2:
        print('the best action for the false negative rumor scenario is : ' , a1)
        print('\n\n')
        print('the intension for this action is : ' , equation[a1])
        print('\n\n')
    else:
        print('the best action for the false negative rumor scenario is : ' , a2)
        print('\n\n')
        print('the intension for this action is : ' , equation[a2])
        print('\n\n')


