import numpy as np
import random as rd
import matplotlib.pyplot as plt
import statistics as sta


# decide what the person will do

def randomEvent(listProb):
    """Takes a list of probabilities and return an index proportional to
    the probability in listProb[index].
    Input: a list of numbers, must add up to 1.0
    Output: a random index between 0 and len( listProb ) - 1 """
    # First check input is correct type
    if len(listProb) == 0 or type(listProb) != list:
        print("Input must be a list longer than 0!")
        raise ValueError
    # Then check that probabilities are consistent
    totProb = 0.0
    for i in listProb:
        totProb += i
    if totProb != 1.0:
        print("Your probabilities do not add up to 1.0!")
        raise ValueError

        # Now pick the event with the right probability (look at the code
    # to see what it does if interested )
    random = np.random.rand()
    total = listProb[0]
    index = 0
    while total < random:
        total += listProb[index + 1]
        index += 1

    return index


# Movement function

def move(pos, NMob):  # pos argument is the position of the person currently
    # NMob is the maximum number of mobility
    if NMob != 0:
        direction = rd.randint(0, 1)  # give the direction. 1 for positive and 0 for negative
        distance = rd.randint(1, NMob)  # give the distance.
        if direction == 1:
            pos += distance
            if pos > n - 1:  # when the person moves across cells from the maximum index to the minimum
                pos = pos - n
        elif direction == 0:
            pos = pos - distance
            if pos < 0:  # when the person moves across cells from the maximum index to the minimum
                pos = n + pos
    return pos


# Model information

N = 1000  # The total number of people
n = 100  # The total number of the cell
sp = 20  # The total number of sick people
hp = N - sp  # The total number of healthy people
vp = 0  # people who take the vaccination
NMob = 1  # Number of mobility for a person

# Sick people info.

p_better = 0.1  # probability to get healthy
p_die_1 = 0.1  # to die
p_travel_1 = 0.2  # to move
p_nothing_1 = 0.6  # to stay still
sickList = [p_better, p_die_1, p_travel_1, p_nothing_1]  # a list for all probability of each
                                                         # event for sick people

# healthy people info.

p_worseB = 0.0  # probability to get sick if no sick people in the same cell
p_worseA = 0.1  # if a healthy person is not vaccinated AND in the same cell with a sick person
p_die_2 = 0.02  # to die
p_travel_1 = 0.1  # to move
p_nothing_2A = 0.78  # with sick person to stay still
p_nothing_2B = 0.88  # no sick person in the same cell to stay still
healListV = [p_worseB, p_die_2, p_travel_1,
             p_nothing_2B]  # a list for all probability of each event for vaccinated people

# open the data txt for data record
myFile = open('D:\VISA\data.txt', 'w+')

# start the simulation

# Number:
liveS = 0  # all of the living people in 20 simulations
deadS = 0
sickS = 0
livelist = []  # for calculating standard deviation
deadlist = []
sicklist = []

# plotting:
plt.figure(20)  # number of graphs we need
x = range(1, 366)  # for the x-axis of the graph
suffix = 1  # suffix for the name of the graphs 'Graph{}.......'


for i in range(20):  # for 20 simulations
    #  Set initial info. for each people
    peopleList = []  # a list contains all of the people in the world.
    # It should include N dictionaries that each contain info. for a person
    i = 0
    while i < N:
        Pi = rd.randint(0, n - 1)  # give the person an initial position
        if i < vp:
            peopleList.append({'Hlt': 'healthy',
                               'Vac': 'yes',
                               'pos': Pi,
                               'worse': p_worseB,
                               'die': p_die_2,
                               'travel': p_travel_1,
                               'nothing': p_nothing_2B})
            # give the person healthy(1) and vaccination(1), probability of other four events
            # For a vaccinated person, he/she will only do nothing or die
            # or move, which does not influence others
        elif i < hp:
            peopleList.append({'Hlt': 'healthy',
                               'Vac': 'no',
                               'pos': Pi,
                               'worse': p_worseB,
                               # Before we start simulating, assume they have 0 probability to get sick
                               'die': p_die_2,
                               'travel': p_travel_1,
                               'nothing': p_nothing_2B})
            # give the person healthy(1) and no vaccination(0), probability of other four events
        else:
            peopleList.append({'Hlt': 'sick',
                               'Vac': 'no',
                               'pos': Pi,
                               'worse': p_better,
                               'die': p_die_1,
                               'travel': p_travel_1,
                               'nothing': p_nothing_1})
            # give the person sick(0) and no vaccination(0), probability of other four events
        i += 1

    # Other perimeters we need
    day = 0  # date
    i = 0
    peopD = 0  # number of people dead in one simulation
    peopS = sp  # number of people sick and initial value is equal to sp
    deadN = []  # a list to record the number of people dead per day and start from the first day
    sickN = []  # for sick people
    liveN = []  # for total number of people alive

    # start the game
    while day < 365:
        # check whether the cell contains sick people
        sickCell = set()  # a set for areas where sick people stay
        for i in range(vp,
                       N):  # unvaccinated people all have probabilities to get
                            # sick, so the loop should cover all of them
            info = peopleList[i]  # extract each person's info. from the peopleList
            if info['Hlt'] == 'sick':  # if the person is sick
                sickCell.add(info['pos'])  # add the indexes of sick cells into the sickCell set
        for i in range(vp, N):  # people who take no vaccination
            info = peopleList[i]
            cell = info.get('pos')  # where the no vaccination people live
            if (cell in sickCell) and (info['Hlt'] == 'healthy'):  # if healthy
                                                                   # people live with the sick people
                info['worse'] = p_worseA  # reset their probabilities for two events
                info['nothing'] = p_nothing_2A

                # consider vaccinated people
        i = 0
        if vp != 0:  # if all dying, just skip this section
            for i in range(vp):
                info = peopleList[i]  # extract info
                if info['Hlt'] != 'dead':
                    index = randomEvent(healListV)  # know what he/she will do
                    if index == 2:  # if he/she will move
                        info['pos'] = move(info.get('pos'), NMob)  # give the person new position
                    elif index == 1:  # if unfortunately dying
                        info['Hlt'] = 'dead'
                        peopD += 1

        # consider no vaccinated people
        i = 0
        for i in range(vp, N):
            info = peopleList[i]
            if info['Hlt'] == 'healthy':  # consider healthy people
                healListNV = [info['worse'], info['die'], info['travel'],
                              info['nothing']]  # extract everyone's event probability
                index = randomEvent(healListNV)
                if index == 0:  # if getting sick
                    info['Hlt'] = p_better
                    info['die'] = p_die_1
                    info['nothing'] = p_nothing_1
                    info['Hlt'] = 'sick'
                    peopS += 1
                elif index == 1:  # if dying
                    info['Hlt'] = 'dead'
                    peopD += 1
                elif index == 2:  # move
                    info['pos'] = move(info['pos'], NMob)
            elif info['Hlt'] == 'sick':
                index = randomEvent(sickList)
                if index == 0:  # get better
                    info['die'] = p_die_2
                    info['worse'] = p_worseB
                    info['nothing'] = p_nothing_2B
                    info['Hlt'] = 'healthy'
                    peopS = peopS - 1
                elif index == 1:  # die
                    info['Hlt'] = 'dead'
                    peopD += 1
                elif index == 2:  # move
                    info['pos'] = move(info['pos'], NMob)

        # add the number into different lists for plotting graphs (per day)
        deadN.append(peopD)
        sickN.append(peopS)
        peopL = N - peopD
        liveN.append(peopL)
        day += 1

    # plot the graph between the day and number of people
    plt.plot(suffix - 1)  # plot on different graphs
    plt.plot(x, liveN, 'ro-', label='Total alive people')  # plot for living people
    plt.plot(x, deadN, 'go-', label='Total dead people')
    plt.plot(x, sickN, 'bo-', label='Total sick people')
    plt.legend()
    plt.xlabel('Time(day)')  # add labels for the axises
    plt.ylabel('Number')
    plt.title('Diease effect on number of people')  # add title
    i = 0
    while i in range(365):  # plot threshold for number 1000
        # plot dashed line
        if i % 10 == 0:
            plt.text(i, 1000, '-')
        else:
            plt.text(i, 1000, '')
        i += 1
    plt.savefig('Graph{}.jpeg'.format(suffix), dpi=500)
    plt.close()

    # record the data in the data text
    myFile.write('Dead people: ' + str(peopD) + '\n')  # number of total people dead
    myFile.write('Living people: ' + str(peopL) + '\n')
    myFile.write('Sick people: ' + str(peopS) + '\n')
    myFile.write('------------------It is the No. ' + str(suffix) + ' simulation------------------\n')
    suffix += 1

    # record total people dead/alive/sick during all simulations
    liveS += peopL  # sum of the living people
    deadS += peopD
    sickS += peopS
    livelist.append(peopL)
    deadlist.append(peopD)
    sicklist.append(peopS)

# calculate the mean and standard deviation
meanL = liveS / 20.0
meanD = deadS / 20.0
meanS = sickS / 20.0
stdL = sta.stdev(livelist)
stdD = sta.stdev(deadlist)
stdS = sta.stdev(sicklist)

# record the results
myFile.write(
    'The mean of the living people is {0:.3f}, dead people,'
    ' {1:.3f} and sick people {2:.3f}.'.format(meanL, meanD, meanS) + '\n')
myFile.write(
    'The standard deviation of the living people is {0:.3f},'
    'dead people {1:.3f} and sick people {2:.3f}.'.format(stdL, stdD, stdS))
