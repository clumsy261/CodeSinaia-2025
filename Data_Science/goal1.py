import math
import time
def calculate_p(px,py,pz):    #This function calculates the momentum of a particle given its components.
    return math.pow(px**2 + py**2 + pz**2, 1/3)               #uses the formula for p

def calculate_pT (px, py):    #This function calculates the transverse momentum of a particle given its x and y components.    
    return math.sqrt(px**2 + py**2)

def calculate_pseudorapidity():               #pseudorapidity is the n with a long end
    pass

def calculate_azimuthal_angle():      #solve if you finish early
    pass

def check_type (pdg_code):      #this function checks the type of particle based on the pdg code
    pass

def poisson_distribution(average):
    return math.sqrt(average)

def difference(no_1, no_2):
    return abs(no_1,no_2)

def combined_uncertainty(no_1,no_2):
    return math.sqrt(no_1 + no_2)

def significance(no_1, no_2, comb_uncertainty):
    if no_1 > no_2:
        return (no_1 - no_2) /comb_uncertainty
    else:
        return (no_2- no_1) /comb_uncertainty

def pion(codd):
    cod = int(codd)
    if(cod == 211): return 1
    if(cod == -211): 
        return -1
    if(cod == 111): 
        return 0
    else:
        return 2
#TODO: Open the input file, read the first line to get event_id and num_particles,
#       then read the rest of the lines into lines_list as lists of strings.
data_sample= "outputs_data\output-Set1.txt"
#batch_size = input("How big should batches be ?\n")
start_time = time.time()
event_count = 0
count_atomi = [0,0,0,0]
avg_pozitiv = 0
avg_negativ = 0
#batch_check = 0
parts = []
with open(data_sample, "r", encoding= "UTF-8") as data_file:
    lines = data_file.readlines()
    for line in lines:
        if(len(line.split()) == 2):
            event_count +=1
        else:
                index =pion(line.split()[3])+1
                count_atomi[index] += 1
                
print(f"In {event_count} total events, we had {count_atomi[2]} positive particles, {count_atomi[1]} neutral particles and {count_atomi[0]} negative particles")
print(f"The average of positive pions per event is {float(count_atomi[2]/event_count)}")
print(f"The average of neutral pions per event is {float(count_atomi[1]/event_count)}")
print(f"The average of negative pions per event is {float(count_atomi[0]/event_count)}")
print(f"The poisson distribution for positive, neutral and negative atoms is: \n Positive:{math.sqrt(count_atomi[2])}\n Neutral:{math.sqrt(count_atomi[1])}\n Negative:{math.sqrt(count_atomi[0])}")
if(count_atomi[2]>count_atomi[0]):
    print(f"There are {count_atomi[2]-count_atomi[0]} more positive particles than antiparticles")
elif(count_atomi[0] > count_atomi[2]):
    print(f"There are {count_atomi[0]-count_atomi[2]} more negative particles than normal ones")
end_time = time.time()
print(f"Also, there are {count_atomi[2]} random particles arround here ")
print(f"Run time : {end_time - start_time} seconds")

#print("event id is", event_id, "and there are", num_particles, "particles")       #print to show the events id and no of particles in the event


# TODO: Loop through each particle in lines_list, convert values to float,
#       call the analysis/calculation functions, and print the results as shown.
    
