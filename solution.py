import random 
from math import cos, sin, radians, sqrt
import matplotlib.pyplot as plt

################################ Task 1 ##################################
prob_right_left_stay = [0.5,0.5,0.0]
choices = [1,-1, 0]
pos = 0
cordinates = [pos]
steps = 100
expectation = 0
for i in range(steps):#numsteps
   move = random.choices(choices, prob_right_left_stay)
   pos += move[0]
   cordinates.append(pos)
   
   #calculating expectation
   for i in choices:
       expectation += i * prob_right_left_stay[i]
   
   
plt.title("Task 1 - 1D Random Walk")
plt.xlabel("number of steps")
plt.ylabel("Distance")
plt.plot(cordinates)
plt.show()



################################ Task 2 ##################################
prob_right_left_stay = [0.5,0.5,0.0]
choices = [1,-1, 0]
Dist_difference = 4
pos_A = 0
pos_B = 0 + Dist_difference
exp_time = 0
meeting_times = list()
#arrays to store locations of each person
person_A = [pos_A]
person_B = [pos_B]
for x in range(4):
    for i in range(10000):
        
        #new distance PersonA
        move_A = random.choices(choices, prob_right_left_stay)
        pos_A += move_A[0]
        if x == 0:
            person_A.append(pos_A)
        
        #new distance PersonB
        move_B = random.choices(choices, prob_right_left_stay)
        pos_B += move_B[0]
        if x == 0:
            person_B.append(pos_B)
        
        if (pos_A == pos_B): #meeting condition
            meeting_times.append(i)
            break
        else:
            pass
        
    #resetting the value for successive iterations to find expected time  
    pos_A = 0
    pos_B = 4

for t in meeting_times:
    exp_time += i
    
plt.title("Task 2 - 1D Random Walk with 2 people")
plt.xlabel("number of steps")
plt.ylabel("Distance")
plt.plot(person_A)
plt.plot(person_B)
plt.show()
print("Time taken to meet in consecutive iterations = ", meeting_times)
print("Expected Meeting time = ", exp_time)


################################ Task 3 ##################################
n = 10000
posx = 80
posy = 60
cordinates_x = [posx]
cordinates_y = [posy]
angles = [0, 57.2958, 114.592, 171.888, 229.184, 286.479, 343.775]

for i in range(n):
   step = random.choice([0,0.5,1])
   theta = round(radians(random.randrange(360)))
   posx = posx + step * cos(theta)
   posy = posy + step * sin(theta)
   
   if sqrt(posx**2 + posy**2) > 100:
       posx = cordinates_x[-1]
       posy = cordinates_y[-1]
       
       continue

   cordinates_x.append(posx)
   cordinates_y.append(posy)
   
    
plt.title("Task 3 - 2D Random Walk within a circle with re-entry")
plt.plot(cordinates_x,cordinates_y)

plt.xlim(-100,100)
plt.ylim(-100,100)
circle1 = plt.Circle((0, 0), 100, color = "green", alpha=180)
fig = plt.gcf()
ax = fig.gca()
ax.add_artist(circle1)
plt.show()

################################ Task 4 ##################################
n = 1000
pos = 0
prob_right_left_stay = [0.5,0.5,0.0]
choices = [1,-1, 0]
cordinates = [pos]
for i in range(n):
    step = random.uniform(0,1)
    move = random.choices(choices, prob_right_left_stay)
    pos += step * move[0]
    cordinates.append(pos)
    
plt.title("Task 4 - 1D Continious Random Walk with steps between 0 - 1")
plt.xlabel("number of steps")
plt.ylabel("Distance")
plt.plot(cordinates)
plt.show()


################################ Task 5 ##################################

n = 10000
posx = 40
posy = 30
cordinates_x = [posx]
cordinates_y = [posy]

for i in range(n):
   step = random.uniform(0,1)
   theta = round(radians(random.randrange(360)),2)
   posx = posx + step * cos(theta)
   posy = posy + step * sin(theta)
   if sqrt(posx**2 + posy**2) > 100:
       posx = cordinates_x[-1]
       posy = cordinates_y[-1]
       
       continue
    
   cordinates_x.append(posx)
   cordinates_y.append(posy)


plt.title("Task 5 - Continuous random variable 2D walk between 0 - 1 and 0 - 2pi")  
plt.plot(cordinates_x,cordinates_y)


plt.xlim(-100,100)
plt.ylim(-100,100)
circle1 = plt.Circle((0, 0), 100, color = "green", alpha = 180)
fig = plt.gcf()
ax = fig.gca()
ax.add_artist(circle1)
plt.show()


################################ Task 7 ##################################
n = 10000
posx = 0
posy = 0
cordinates_x = [posx]
cordinates_y = [posy]
for i in range(n):
   step = random.choice([0, 0.5, 1]) #any random size
   theta = round(radians(random.randrange(360)),2)
   posx = posx + step * cos(theta)
   posy = posy + step * sin(theta)
#
   if sqrt(posx**2 + posy**2) > 100:
       posx = cordinates_x[-1]
       posy = cordinates_y[-1]
       
       continue

   cordinates_x.append(posx)
   cordinates_y.append(posy)

plt.title("Task 7 - 2D Random continuous Walk with discrete steps")  
plt.plot(cordinates_x,cordinates_y)

plt.xlim(-100,100)
plt.ylim(-100,100)
circle1 = plt.Circle((0, 0), 100, color = "green", alpha = 180)
fig = plt.gcf()
ax = fig.gca()
ax.add_artist(circle1)
plt.title("Task 7")
plt.show()


################################ Task 8 ##################################

#this task takes some time to execute bcz of the number of iterations
n = 1000000
m = 10
stepcount = []
for x in range(m):
    #generating random starting position for node 1
    rad = random.uniform(0,2)
    rand_r = random.randint(0,100)
    posx = rand_r * cos(rad)
    posy = rand_r * sin(rad)
    
    #generating random starting position for node 2
    rad2 = random.uniform(0,2)
    rand_r2 = random.randint(0,100)
    posx2 = rand_r2 * cos(rad2)
    posy2 = rand_r2 * sin(rad2)
    
    
    count = 0
    cordinates_x1 = [posx]
    cordinates_y1 = [posy]
    cordinates_x2 = [posx2]
    cordinates_y2 = [posy2]
    
    for i in range(n):
       #chechking if distnce between the 2 nodes is less than 1
       dst = sqrt(((posx2 - posx)**2) + ((posy2 - posy)**2))
       if dst <= 1:
           break
        
       #generating new positions
       step1 = random.uniform(0,1)
       theta1 = round(radians(random.randrange(360)),2)
       posx = posx + step1 * cos(theta1)
       posy = posy + step1 * sin(theta1)
        
       #checking if the nodes are exceeding the boundary or not
       if sqrt(posx**2 + posy**2) > 100:
           posx = cordinates_x1[-1]
           posy = cordinates_y1[-1]
       else:
           cordinates_x1.append(posx)
           cordinates_y1.append(posy)
       
       step2 = random.uniform(0,1)
       theta2 = round(radians(random.randrange(360)),2)
       posx2 = posx2 + step2 * cos(theta2)
       posy2 = posy2 + step2 * sin(theta2)

       if sqrt(posx2**2 + posy2**2) > 100:
           posx2 = cordinates_x2[-1]
           posy2 = cordinates_y2[-1]
       else:
           cordinates_x2.append(posx2)
           cordinates_y2.append(posy2)
       
       count+=1
    stepcount.append(count)
    
    if x == 0:
        #plotting only pne simulation
        plt.plot(cordinates_x1,cordinates_y1)
        plt.plot(cordinates_x2,cordinates_y2)


plt.title("Task8 - 2D Random Walk")
print("Consecutive step counts = ", stepcount)
print("Average steps: " + str(int(sum(stepcount)/len(stepcount))))

plt.xlim(-100,100)
plt.ylim(-100,100)
circle1 = plt.Circle((0, 0), 100, color = "green", alpha = 180)
fig = plt.gcf()
ax = fig.gca()
ax.add_artist(circle1)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()




