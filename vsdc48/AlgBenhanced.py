############
############ ALTHOUGH I GIVE YOU THIS TEMPLATE PROGRAM WITH THE NAME 'skeleton.py', 
############ YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR THE PURPOSES OF 
############ THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT THIS PROGRAM IS STILL 
############ CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES! TO SEE
############ THE STANDARD MODULES, TAKE A LOOK IN 'validate_before_handin.py'.
############
############ DO NOT INCLUDE ANY COMMENTS ON A LINE WHERE YOU IMPORT A MODULE.
############

import os
import sys
import time
import random

############ START OF SECTOR 0 (IGNORE THIS COMMENT)
############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############ BY 'DO NOT TOUCH' I REALLY MEAN THIS. EVEN CHANGING THE SYNTAX, BY
############ ADDING SPACES OR COMMENTS OR LINE RETURNS AND SO ON, COULD MEAN THAT
############ CODES MIGHT NOT RUN WHEN I RUN THEM!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############
############ END OF SECTOR 0 (IGNORE THIS COMMENT)

input_file = "AISearchfile058.txt"

############ START OF SECTOR 1 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

############ END OF SECTOR 1 (IGNORE THIS COMMENT)

############ START OF SECTOR 2 (IGNORE THIS COMMENT)
path_for_city_files = os.path.join("..", "city-files")
############ END OF SECTOR 2 (IGNORE THIS COMMENT)

############ START OF SECTOR 3 (IGNORE THIS COMMENT)
if os.path.isfile(path_for_city_files + "/" + input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string(path_for_city_files + "/" + input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the city-file folder.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME.
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############
############ END OF SECTOR 3 (IGNORE THIS COMMENT)

############ START OF SECTOR 4 (IGNORE THIS COMMENT)
path_for_alg_codes_and_tariffs = os.path.join("..", "alg_codes_and_tariffs.txt")
############ END OF SECTOR 4 (IGNORE THIS COMMENT)

############ START OF SECTOR 5 (IGNORE THIS COMMENT)
code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs(path_for_alg_codes_and_tariffs)

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR
############ USER-NAME, E.G., "abcd12"
############
############ END OF SECTOR 5 (IGNORE THIS COMMENT)

my_user_name = "vsdc48"

############ START OF SECTOR 6 (IGNORE THIS COMMENT)
############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############
############ END OF SECTOR 6 (IGNORE THIS COMMENT)

my_first_name = "Michal"
my_last_name = "Pluta"

############ START OF SECTOR 7 (IGNORE THIS COMMENT)
############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############
############ END OF SECTOR 7 (IGNORE THIS COMMENT)

algorithm_code = "PS"

############ START OF SECTOR 8 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the algorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

start_time = time.time()

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER. NOTE THAT I CALCULATE THE TIME OF
############ A RUN USING THE RESERVED VARIABLE 'start_time' AND INCLUDE THE RUN-TIME IN 'added_note' LATER.
############
############ IN FACT, YOU CAN INCLUDE YOUR ADDED NOTE IMMEDIATELY BELOW OR EVEN INCLUDE YOUR ADDED NOTE
############ AT ANY POINT IN YOUR PROGRAM: JUST DEFINE THE STRING VARIABLE 'added_note' WHEN YOU WISH
############ (BUT DON'T REMOVE THE ASSIGNMENT IMMEDIATELY BELOW).
############
############ END OF SECTOR 8 (IGNORE THIS COMMENT)

added_note = ""

############ START OF SECTOR 9 (IGNORE THIS COMMENT)
############
############ NOW YOUR CODE SHOULD BEGIN BUT FIRST A COMMENT.
############
############ IF YOU ARE IMPLEMENTING GA THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'pop_size' TO DENOTE THE SIZE OF YOUR POPULATION (THIS IS '|P|' IN THE PSEUDOCODE)
############
############ IF YOU ARE IMPLEMENTING AC THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'num_ants' TO DENOTE THE NUMBER OF ANTS (THIS IS 'N' IN THE PSEUDOCODE)
############
############ IF YOU ARE IMPLEMENTING PS THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'num_parts' TO DENOTE THE NUMBER OF PARTICLES (THIS IS 'N' IN THE PSEUDOCODE)
############
############ DOING THIS WILL MEAN THAT THIS INFORMATION IS WRITTEN WITHIN 'added_note' IN ANY TOUR-FILE PRODUCED.
############ OF COURSE, THE VALUES OF THESE VARIABLES NEED TO BE ACCESSIBLE TO THE MAIN BODY OF CODE.
############ IT'S FINE IF YOU DON'T ADOPT THESE VARIABLE NAMES BUT THIS USEFUL INFORMATION WILL THEN NOT BE WRITTEN TO ANY
############ TOUR-FILE PRODUCED BY THIS CODE.
############
############ END OF SECTOR 9 (IGNORE THIS COMMENT)

from typing import List, Tuple
from dataclasses import dataclass
from threading import Thread
from math import floor

#Global constants
MAXINT = sys.maxsize * 2 + 1
num_parts = 1000                 # Number of particles

# Acceleration coefficients
ALPHA = 0.3 / 0.9               # cognitive learning factor
BETA = 1.0 / 0.9                # social learning factor

# Inertia parameters
INERTIA_START = 1
INERTIA_RATIO = 0.9999

# Proximity randomisation
EPSILON_RANGE = (0.8, 1)

# Extinction
EXTINCTION_ITER = 500           # If no changes after this many iterations then extinction

SET_ALL_CITIES = set(range(num_cities))
LIST_ALL_CITIES = list(range(num_cities))

# Dazing setup
DAZE_ITER = EXTINCTION_ITER / 10
DAZE_PROB = 0.0003
DAZE_DURATION = 10

# Type aliases
Tour = CityList = List[int]
Velocity = List[Tuple[int, int]]
Solution = Tuple[Tour, int]

def save(tour, tour_length):
    global max_it
    global num_parts
    added_note = ""
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 1)

    if algorithm_code == "GA":
        try: max_it
        except NameError: max_it = None
        try: pop_size
        except NameError: pop_size = None
        if added_note != "":
            added_note = added_note + "\n"
        added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'pop_size' = " + str(pop_size) + "."

    if algorithm_code == "AC":
        try: max_it
        except NameError: max_it = None
        try: num_ants
        except NameError: num_ants = None
        if added_note != "":
            added_note = added_note + "\n"
        added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'num_ants' = " + str(num_ants) + "."

    if algorithm_code == "PS":
        try: max_it
        except NameError: max_it = None
        try: num_parts
        except NameError: num_parts = None
        if added_note != "":
            added_note = added_note + "\n"
        added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'num_parts' = " + str(num_parts) + "."
        
    added_note = added_note + "\nRUN-TIME = " + str(elapsed_time) + " seconds.\n"

    flag = "good"
    length = len(tour)
    for i in range(0, length):
        if isinstance(tour[i], int) == False:
            flag = "bad"
        else:
            tour[i] = int(tour[i])
    if flag == "bad":
        print("*** error: Your tour contains non-integer values.")
        sys.exit()
    if isinstance(tour_length, int) == False:
        print("*** error: The tour-length is a non-integer value.")
        sys.exit()
    tour_length = int(tour_length)
    if len(tour) != num_cities:
        print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
        sys.exit()
    flag = "good"
    for i in range(0, num_cities):
        if not i in tour:
            flag = "bad"
    if flag == "bad":
        print("*** error: Your tour has illegal or repeated city names.")
        sys.exit()
    check_tour_length = 0
    for i in range(0, num_cities - 1):
        check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
    check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
    if tour_length != check_tour_length:
        flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
        sys.exit()
    print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")
    len_user_name = len(my_user_name)
    user_number = 0
    for i in range(0, len_user_name):
        user_number = user_number + ord(my_user_name[i])
    alg_number = ord(algorithm_code[0]) + ord(algorithm_code[1])
    tour_diff = abs(tour[0] - tour[num_cities - 1])
    for i in range(0, num_cities - 1):
        tour_diff = tour_diff + abs(tour[i + 1] - tour[i])
    certificate = user_number + alg_number + tour_diff
    local_time = time.asctime(time.localtime(time.time()))
    output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
    output_file_time = output_file_time.replace(" ", "0")
    script_name = os.path.basename(sys.argv[0])
    if len(sys.argv) > 2:
        output_file_time = sys.argv[2]
    output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

    f = open(output_file_name,'w')
    f.write("USER = {0} ({1} {2}),\n".format(my_user_name, my_first_name, my_last_name))
    f.write("ALGORITHM CODE = {0}, NAME OF CITY-FILE = {1},\n".format(algorithm_code, input_file))
    f.write("SIZE = {0}, TOUR LENGTH = {1},\n".format(num_cities, tour_length))
    f.write(str(tour[0]))
    for i in range(1,num_cities):
        f.write(",{0}".format(tour[i]))
    f.write(",\nNOTE = {0}".format(added_note))
    f.write("CERTIFICATE = {0}.\n".format(certificate))
    f.close()
    print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")

@dataclass
class Particle:
    p: Tour
    v: Velocity
    p_best: Tuple[Tour, int]
    last_update: int
    dazed: bool
    dazed_until: int

def nn_complete_tour(tour: Tour) -> Tuple[CityList, int]:
    """Uses the nearest-neighbour algorithm to complete a partial `tour` and returns the cities and cost of completing the tour

    Args:
        tour (Tour): The partially completed tour

    Returns:
        Tuple[CityList, int]: Returns an tuple containing: an ordered list of the cities used to complete the tour and the cost of doing so
    """
    # Compute the unvisited cities
    unvisited = SET_ALL_CITIES - set(tour)
    
    # Declare vars to store the cities used to complete the tour and the cost of doing so
    last_element, added_cities, added_cost = tour[-1], [], 0
    
    # Keep iterating until
    while unvisited:
        # Find the next shortest edge
        min_city = min(unvisited, key=lambda x: dist_matrix[last_element][x])
        
        # Add the edge to the running total
        added_cities += [min_city]
        added_cost += dist_matrix[last_element][min_city]
        
        # Mark it as visited and set it as the last element
        unvisited -= {min_city}
        last_element = min_city
    
    # Add the final edge to the cost
    added_cost += dist_matrix[added_cities[-1]][tour[0]]
    
    return added_cities, added_cost

def two_opt(tour: Tour, passes: int = int(1e9)) -> Tuple[Tour, int]:
    """Performs 2-optimisation on a given `tour` to find a local improvement

    Args:
        tour (Tour): The current tour
        passes (int, optional): Number of passes of 2opt to perform. Defaults to int(1e9).

    Returns:
        Tour: The locally optimised tour
        int: The tour's length
    """
    
    # Best tour length after each 2 opt iteration
    tour_length = get_tour_length(tour)

    # Best tour found at any point in time
    best_tour = tour
    best_length = tour_length

    improved = True
    for _ in range(passes):
        if not improved:
            # Exit if no improvement found in previous iteration
            break
        
        # Initially no improvement
        improved = False

        # Iterate through all possible 2-edge swaps
        for i in range(1, num_cities - 2):
            for j in range(i + 2, num_cities):
                # Pre-calculate the length delta
                length_delta = - dist_matrix[tour[i-1]][tour[i]] - dist_matrix[tour[j-1]][tour[j]] + dist_matrix[tour[i-1]][tour[j-1]] + dist_matrix[tour[i]][tour[j]]
                
                # If it doesn't improve the length of the current tour then skip
                if length_delta >= 0:
                    continue
                # Calculate new tour length
                new_tour_length = tour_length + length_delta

                if new_tour_length < best_length:
                    # Perform the 2-opt swap
                    new_tour = tour[:]
                    new_tour[i:j] = tour[j - 1:i - 1:-1]
                    
                    # Update best tour found
                    best_tour = new_tour
                    best_length = new_tour_length

                    # Continue 2-opt
                    improved = True

        # Update best tour and length found in the previous iteration
        tour = best_tour
        tour_length = best_length

    return best_tour, best_length

def get_tour_length(tour: Tour) -> int:
    """Calculates the length of a given `tour`

    Args:
        tour (Tour): The input tour

    Returns:
        int: The length of the tour
    """
    return sum(dist_matrix[tour[i]][tour[i-1]] for i in range(num_cities))

def generate_random_tour() -> Tour:
    """Generates a completely random tour

    Returns:
        Tour: A random tour
    """
    return random.sample(LIST_ALL_CITIES, num_cities)

def generate_nn_tour(partial_length: int = 2) -> Tour:
    """Generates a tour where the first `partial_length` cities are random and the rest are filled using nearest neighbour

    Args:
        partial_length (int, optional): Length of random portion. Defaults to 2.

    Returns:
        Tour: The generated tour
    """
    partial = random.sample(LIST_ALL_CITIES, partial_length)
    
    added_cities, _ = nn_complete_tour(partial)
    
    return partial + added_cities

def generate_velocity(n_swaps: int = 5, n_cities: int = num_cities) -> Velocity:
    """Returns a random velocity containing `n_swaps` number of swaps

    Args:
        n_swaps (int, optional): Number of swaps in the velocity. Defaults to 5.

    Returns:
        Velocity: The random velocity
    """
    return [tuple(random.sample(range(n_cities), 2)) for _ in range(n_swaps)]

def generate_particle() -> Particle:
    """Generates a new particle with a random tour and random velocity

    Returns:
        Particle: A new particle
    """
    tour = generate_nn_tour()
    tour, tour_length = two_opt(tour, 2)
    velocity = generate_velocity()
    
    return Particle(tour, velocity, (tour, tour_length), 0, False, 0)

def generateAllParticles() -> List[Particle]:
    """ Generates `num_parts` number of particles and returns them as a list

    Returns:
        List[Particle]: List of particles generated
    """
    return [generate_particle() for _ in range(num_parts)]

def normalise_v(v: Velocity) -> Velocity:
    """Normalises a given velocity `v` by applying the velocity and then recalculating the equivalent, simplified velocity

    Args:
        v (Velocity): Input velocity

    Returns:
        Velocity: Normalised (simplified) velocity
    """
    original = list(range(num_cities))
    modified = apply_v(original, v)
    return calc_v(original, modified)

def calc_v(tourA: Tour, tourB: Tour) -> Velocity:
    """Calculates the velocity between `tourA` and `tourB` by performing an insertion-style sort

    Args:
        tourA (Tour): The subtrahend in the velocity calculation
        tourB (Tour): The minuend in the velocity calculation
    Returns:
        Velocity: The velocity corresponding to `tourB` - `tourA`
    """
    
    # Copy tourA and create an index map of tourB to speed up index requests
    tourX = tourA[:]
    idx_map = {val: idx for idx, val in enumerate(tourX)}

    # Perform the sort, keeping track of velocity
    v = []
    for i in range(num_cities):
        # The element is already in the correct order then continue
        if tourX[i] == tourB[i]:
            continue
        
        # Find the correct element and where it is currently located
        correct = tourB[i]
        correct_idx = idx_map[correct]

        # Perform the swap
        tourX[i], tourX[correct_idx] = tourX[correct_idx], tourX[i]

        # Update the index_map to reflect the swap.
        idx_map[tourX[correct_idx]] = correct_idx
        idx_map[correct] = i

        # Add swap to velocity
        v.append((i, correct_idx))

    return v

def scale_v(v: Velocity, gamma: float) -> Velocity:
    """Scales a given velocity `v` by a given scalar `gamma`

    Args:
        v (Velocity): The input velocity
        gamma (float): The scalar to scale the velocity using

    Returns:
        Velocity: The scaled velocity
    """
    
    # Negative scalar is just a reversal
    if gamma < 0:
        return reversed(scale_v(v, gamma))

    # Compute fractional portion of the velocity
    if 0 <= gamma <= 1:
        return v[:floor(gamma * len(v))]

    # Compute the whole and fractional portion of the velocity
    if gamma > 1:
        gamma_floor = floor(gamma)
        return v * gamma_floor + scale_v(v, gamma - gamma_floor)

def apply_v(tour: Tour, v: Velocity) -> Tour:
    """Given an existing `tour` and a velocity `v`, sequentially applies the swaps in the velocity and returns a new velocity

    Args:
        tour (Tour): The existing tour
        v (Velocity): The velocity to apply

    Returns:
        Tour: The new tour
    """
    # Copy the existing tour
    new_tour = tour[:]
    
    # Sequentially apply all the swap operations
    for i1, i2 in v:
        new_tour[i1], new_tour[i2] = new_tour[i2], new_tour[i1]

    return new_tour

def calc_cognitive_v(p_a: Tour, p_best: Tour, epsilon1: float) -> Velocity:
    """Calculates the cognitive velocity of a particle

    Args:
        p_a (Tour): Currently position of the particle
        p_best (Tour): Personal best of the particle
        epsilon1 (float): Random proximity factor

    Returns:
        Velocity: The cognitive velocity of the particle
    """
    cognitive_v = calc_v(p_a, p_best)
    return scale_v(cognitive_v, ALPHA * epsilon1)

def calc_social_v(p_a: Tour, g_best: Tour, epsilon2: float) -> Velocity:
    """Calculates the social velocity of a particle

    Args:
        p_a (Tour): Current position of the particle
        g_best (Tour): The current global best position since a star topology is being used
        epsilon2 (float): Random proximity factor

    Returns:
        Velocity: The social velocity of the particle
    """
    social_v = calc_v(p_a, g_best)
    return scale_v(social_v, BETA * epsilon2)

class PSO_Solver:
    def solve(self) -> None:
        """Starts the solving process
        """
        # Generate all the particles
        parts: List[Particle] = generateAllParticles()

        # Calculate global best
        self.g_best = min(parts, key=lambda p: p.p_best[1]).p_best
        
        # Runtime variables
        inertia = INERTIA_START
        iter = 0
        last_global_update = -1

        while True:
            print(iter, sum(part.dazed for part in parts))
            if iter > EXTINCTION_ITER and iter > 2 * last_global_update:
                # Complete extinction - essentially a restart
                print("EXTINCTION")
                parts = generateAllParticles()
                print("PARTICLES GENERATED")
                
                # Check if a new global best is within the new particle swarm
                best = min(parts, key=lambda p: p.p_best[1]).p_best
                if best[1] < self.g_best[1]:
                    self.g_best = best
                    print(self.g_best[1])
                    save(*self.g_best)
                
                # Reset variables
                last_global_update, iter, inertia = 0, 0, INERTIA_START
            
            # Generate values for runtime parameters
            inertia *= INERTIA_RATIO
            e1 = random.uniform(*EPSILON_RANGE)
            e2 = random.uniform(*EPSILON_RANGE)
                
            for a in range(num_parts):
                # Check if the particle should be dazed
                if iter - parts[a].last_update > DAZE_ITER and random.random() < DAZE_PROB:
                    # Daze the particle by giving it a semi-random position and making it so they are blind to their surroundings (i.e. 0 social velocity)
                    parts[a].dazed = True
                    parts[a].dazed_until = iter + DAZE_DURATION
                    
                    # Generate a random tour but make it a bit better by applying 10 iterations of 2-opt
                    parts[a].p = two_opt(generate_random_tour(), 10)[0]
                    parts[a].last_update = iter
                    print("DAZE")
                elif parts[a].dazed and iter >= parts[a].dazed_until:
                    # Free the particle from dazing
                    parts[a].dazed = False
                    parts[a].last_update = iter
                    
                # Calculate the cognitive & social velocities
                cognitive_v = calc_cognitive_v(parts[a].p, parts[a].p_best[0], e1)
                social_v = calc_social_v(parts[a].p, self.g_best[0], e2)
                
                # Move the current particle
                parts[a].p = apply_v(parts[a].p, parts[a].v)

                # Update the velocity
                parts[a].v = scale_v(parts[a].v, inertia) + cognitive_v
                
                # Only add social velocity if the particle isn't dazed
                if not parts[a].dazed:
                    parts[a].v += social_v

                # Normalise if velocity is too large
                if len(parts[a].v) > 2.5 * num_cities:
                    parts[a].v = normalise_v(parts[a].v)

                # Update local best
                length = get_tour_length(parts[a].p)
                if length < parts[a].p_best[1]:
                    # Improve particle's solution using 2opt
                    parts[a].p_best = two_opt(parts[a].p)
                    
                    # Update the last time the particle updated and anything updated
                    parts[a].last_update = iter
                    last_global_update = iter

                    # Update global best
                    if parts[a].p_best[1] < self.g_best[1]:
                        self.g_best = parts[a].p_best
                        save(*self.g_best)
                        print("GBEST - " + str(self.g_best[1]))

            iter += 1

    def get_best_tour(self) -> Solution:
        """Returns a tuple containing the solution tour and its length

        Returns:
            Solution: The solution
        """
        return self.g_best

    def run_with_timeout(self, timeout: int = 59) -> bool:
        """Runs the solver for `timeout` number of seconds and returns whether the solver terminated

        Args:
            timeout (int, optional): Number of seconds to run the solver for. Defaults to 59.

        Returns:
            bool: Whether the solver terminated within the timeout
        """
        solver_thread = Thread(target=self.solve)
        solver_thread.daemon = True
        solver_thread.start()
        solver_thread.join(timeout)

        return solver_thread.is_alive()
    
solver = PSO_Solver()

solver.run_with_timeout(60 * 60 * 24 * 7)

tour, tour_length = solver.get_best_tour()

########### Testing when to normalise

# tour = get_random_tour()

# for c in range(10, 4001, 10):
#     v = get_random_velocity(n_swaps=c)

#     start = time.time()
#     normalise_v(v)
#     end = time.time()

#     normalised = round((end - start) * 1000, 4)

#     start = time.time()
#     apply_v(tour, v)
#     end = time.time()

#     applied = round((end - start) * 1000, 4)

#     print(str(round(float(c) / num_cities, 3)).ljust(7, " "), str(normalised).ljust(7, " "), str(applied).ljust(7, " "))


############ START OF SECTOR 10 (IGNORE THIS COMMENT)
############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1} SO THAT EVERY INTEGER
############ APPEARS EXACTLY ONCE, AND YOU SHOULD ALSO HOLD THE LENGTH OF THIS TOUR IN THE RESERVED
############ INTEGER VARIABLE 'tour_length'.
############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE'S
############ NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATE AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############
############ DO NOT EDIT ANY TOUR FILE! ALL TOUR FILES MUST BE LEFT AS THEY WERE ON OUTPUT.
############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

end_time = time.time()
elapsed_time = round(end_time - start_time, 1)

if algorithm_code == "GA":
    try: max_it
    except NameError: max_it = None
    try: pop_size
    except NameError: pop_size = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'pop_size' = " + str(pop_size) + "."

if algorithm_code == "AC":
    try: max_it
    except NameError: max_it = None
    try: num_ants
    except NameError: num_ants = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'num_ants' = " + str(num_ants) + "."

if algorithm_code == "PS":
    try: max_it
    except NameError: max_it = None
    try: num_parts
    except NameError: num_parts = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'num_parts' = " + str(num_parts) + "."
    
added_note = added_note + "\nRUN-TIME = " + str(elapsed_time) + " seconds.\n"

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")
len_user_name = len(my_user_name)
user_number = 0
for i in range(0, len_user_name):
    user_number = user_number + ord(my_user_name[i])
alg_number = ord(algorithm_code[0]) + ord(algorithm_code[1])
tour_diff = abs(tour[0] - tour[num_cities - 1])
for i in range(0, num_cities - 1):
    tour_diff = tour_diff + abs(tour[i + 1] - tour[i])
certificate = user_number + alg_number + tour_diff
local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = {0} ({1} {2}),\n".format(my_user_name, my_first_name, my_last_name))
f.write("ALGORITHM CODE = {0}, NAME OF CITY-FILE = {1},\n".format(algorithm_code, input_file))
f.write("SIZE = {0}, TOUR LENGTH = {1},\n".format(num_cities, tour_length))
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write(",{0}".format(tour[i]))
f.write(",\nNOTE = {0}".format(added_note))
f.write("CERTIFICATE = {0}.\n".format(certificate))
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")

############ END OF SECTOR 10 (IGNORE THIS COMMENT)
