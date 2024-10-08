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

input_file = "AISearchfile535.txt"

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

algorithm_code = "GA"

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

from dataclasses import dataclass
from typing import List, Tuple
from threading import Thread

# Type aliases
Tour = CityList = List[int]
Distribution = List[int]
Solution = Tuple[Tour, int]


@dataclass
class Individual:
    tour: Tour
    length: int


Population = List[Individual]

# Runtime parameters
pop_size = 10000  # 1000
TOURNAMENT_SIZE = int(pop_size / 50)

# Probabilities
PROB_MUTATION = 0.04
TWO_OPT_PROB = 0.001
TWO_OPT_NUM_ITER = 2

# Maximum cities to shuffle in PSM mutation
MAX_PARTIAL_SHUFFLE = 5

# Extinction configuration
EXTINCTION_ITER = 500
EXTINCTION_PROB = 0.005
EXTINCTION_RANGE = (0.2, 0.4)

# Restarting algorithm
MIN_RESTART_ITER = 200  # 5000
MAX_RESTART_ITER = 10000

# Useful variables
SET_ALL_CITIES = set(range(num_cities))
LIST_ALL_CITIES = list(range(num_cities))


def save(tour, tour_length):
    global max_it
    global pop_size
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


def generate_tour(partial_length: int = 2) -> Tour:
    """Generates a tour where the first `partial_length` cities are random and the rest are filled using nearest neighbour

    Args:
        partial_length (int, optional): Length of random portion. Defaults to 2.

    Returns:
        Tour: The generated tour
    """
    partial = random.sample(LIST_ALL_CITIES, partial_length)

    added_cities, _ = nn_complete_tour(partial)

    return partial + added_cities


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
                length_delta = - dist_matrix[tour[i-1]][tour[i]] - dist_matrix[tour[j-1]
                                                                               ][tour[j]] + dist_matrix[tour[i-1]][tour[j-1]] + dist_matrix[tour[i]][tour[j]]

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


def generate_individual() -> Individual:
    """Generates a random individual of the population which is just a random tour

    Returns:
        Individual: The individual
    """
    tour = random.sample(LIST_ALL_CITIES, num_cities)
    return Individual(tour, get_tour_length(tour))


def pick_individual(population: Population) -> Individual:
    """Picks a random individual from the `population` by running a tournament

    Args:
        population (Population): The population

    Returns:
        Individual: Randomly selected individual
    """
    tournament = random.sample(population, TOURNAMENT_SIZE)

    return min(tournament, key=lambda ind: ind.length)


def ox_crossover(ind1: Individual, ind2: Individual, i: int, j: int) -> Tour:
    """Performs ordered crossover on two parent individuals and returns the child tour

    Args:
        ind1 (Individual): First parent individual
        ind2 (Individual): Second parent individual
        i (int): Index 1 of crossover
        j (int): Index 2 of crossover

    Returns:
        Tour: The child tour
    """
    # Get the genetic data from parent 1
    new_tour = ind1.tour[i:j]
    visited = set(new_tour)

    # Get the rest of the tour
    rest_tour = [city for city in ind2.tour if city not in visited]

    # Rearrange these correctly to form the tour
    return rest_tour[num_cities-j:] + new_tour + rest_tour[:num_cities-j]


def scx_crossover(ind1: Individual, ind2: Individual):
    # Start with the first city from the best parent
    child = [ind1.tour[0]] if ind1.length <= ind2.length else [ind2.tour[0]]
    visited = set(child)

    # Store index maps for both parents
    i_map1 = {n: i for i, n in enumerate(ind1.tour)}
    i_map2 = {n: i for i, n in enumerate(ind2.tour)}

    # Fill the child
    while len(child) < num_cities:
        # Get the current city in the child
        curr = child[-1]

        # Find the next cities from each parent
        next_p1 = ind1.tour[(i_map1[curr] + 1) % num_cities]
        next_p2 = ind2.tour[(i_map2[curr] + 1) % num_cities]

        if next_p1 in visited and next_p2 in visited:
            # Both next cities are in child, find the closest city not in child
            unvisited = SET_ALL_CITIES - visited
            next_city = min(unvisited, key=lambda x: dist_matrix[curr][x])
        elif next_p1 in child:
            # If city suggested by parent 1 has already been visited
            next_city = next_p2
        elif next_p2 in child or dist_matrix[curr][next_p1] < dist_matrix[curr][next_p2]:
            # If city suggested by parent 2 has already been visited or city suggested by parent 1 is cheaper to visit
            next_city = next_p1
        else:
            # If city suggested by parent 2 is cheaper to visit
            next_city = next_p2

        # Append city to child and add to visited
        child.append(next_city)
        visited.add(next_city)

    return child


def cross_over(ind1: Individual, ind2: Individual) -> Individual:
    """Creates two children from the two individuals and returns the fittest one

    Args:
        ind1 (Individual): First parent individual
        ind2 (Individual): Second parent individual

    Returns:
        Individual: Child Individual
    """
    # Pick a random position in the distribution
    i = random.randint(0, num_cities - 2)
    j = random.randint(i + 1, num_cities - 1)

    # Create child tours using cross-over
    child_tour1 = ox_crossover(ind1, ind2, i, j)
    child_tour2 = ox_crossover(ind2, ind1, i, j)

    # Gets the fitness of both children
    length1 = get_tour_length(child_tour1)
    length2 = get_tour_length(child_tour2)

    # Return the fitter child
    if length1 < length2:
        return Individual(child_tour1, length1)
    else:
        return Individual(child_tour2, length2)


def mutate_rsm(tour: Tour) -> None:
    """Performs Reverse Sequence Mutation (RSM) / Inverse Mutation (IM) on the `tour`

    Args:
        tour (Tour): The input tour
    """
    if num_cities < 4:
        # Too small to perform RSM
        return

    # Pick two random indexes in the tour to perform RSM
    i = random.randint(0, num_cities - 3)
    j = random.randint(i + 2, num_cities - 1)

    # Reverse the partial tour between the two indexes
    rev = reversed(tour[i:j])
    tour[i:j] = rev


def mutate_partial_shuffle(tour: Tour) -> None:
    """Performs Partial Shuffle Mutation (PSM) / Scramble Mutation on the `tour` which takes a subset of the tour and scrambles it

    Args:
        tour (Tour): The input tour
    """
    if num_cities < 4:
        # Too small to shuffle partially
        return

    # Get start idx
    max_i = num_cities - 2
    i = random.randint(0, max_i)

    # Get end idx
    max_j = min(i + MAX_PARTIAL_SHUFFLE, num_cities)
    j = random.randint(i + 2, max_j)

    # Shuffle the portion
    shuffle_portion = tour[i:j]
    random.shuffle(shuffle_portion)

    # Replace the original
    tour[i:j] = shuffle_portion


def mutate_swap(tour: Tour) -> None:
    """Performs Swap Mutation which swaps two random cities in the tour

    Args:
        tour (Tour): The input tour
    """
    # Get two indexes to perform a swap
    i1, i2 = tuple(random.sample(LIST_ALL_CITIES, 2))

    # Perform the swap
    temp = tour[i1]
    tour[i1] = tour[i2]
    tour[i2] = temp


def mutate_throas(tour: Tour) -> None:
    """Performs THROAS mutation on a `tour` which circularly swaps 3 consequtive cities in the tour

    Args:
        tour (Tour): The input tour
    """
    if num_cities < 5:
        # Too small to perform throas
        return

    # Get a random index
    i = random.randint(0, num_cities - 1)

    # Perform the circular swap
    temp = tour[i]
    tour[i] = tour[i-1]
    tour[i-1] = tour[i-2]
    tour[i-2] = temp


def mutate_thrors(tour: Tour) -> None:
    """Performs THRORS mutation on a `tour` which circularly swaps cities at any 3 indexes in the tour

    Args:
        tour (Tour): The input tour
    """
    if num_cities < 3:
        # Too small to perform THRORS
        return

    # Get 3 random indexes
    i, j, k = tuple(random.sample(LIST_ALL_CITIES, 3))

    # Perform the circular 3-swap
    temp = tour[i]
    tour[i] = tour[k]
    tour[k] = tour[j]
    tour[j] = temp


def mutate_full_shuffle(tour: Tour) -> None:
    """Performs a mutation where the tour is randomly shuffled

    Args:
        tour (Tour): The input tour
    """
    tour[0:num_cities] = random.sample(LIST_ALL_CITIES, num_cities)


def get_full_shuffle_weight(iter: int) -> int:
    """Given an iteration number `iter`, returns the weight of a full shuffle occurring in the mutation probability distribution

    Args:
        iter (int): Iteration number, or Iterations since last update

    Returns:
        int: Weight of the full shuffle mutation occurring
    """
    # Full shuffle weight profile corresponding to the function:
    # min(8, 1.02 ^ (iter // 10))
    # which is an exponential growing from 1 to 8 across 1000 iterations
    full_shuffle_prob = [0, 333, 528, 667, 774, 862, 936, 1000]

    # Gets the weight corresponding to the iteration
    prob = 0
    while prob != 8 and iter > full_shuffle_prob[prob]:
        prob += 1

    return prob


def mutate(ind: Individual, iter: int) -> None:
    """Performs a mutation by randomly picking a possible mutation and applying it

    Args:
        ind (Individual): The individual to be mutated
        iter (int): Number of iterations since the last update
    """
    # Initialise the available mutations and their weights
    mutations = [mutate_rsm, mutate_partial_shuffle, mutate_swap,
                 mutate_throas, mutate_thrors, mutate_full_shuffle]
    weights = [12, 6, 4, 2, 1, get_full_shuffle_weight(iter)]

    # Pick a random mutation
    mutation = random.choices(population=mutations, weights=weights, k=1)[0]

    # Apply the mutation
    mutation(ind.tour)

    # Recalculate the new tour length
    ind.length = get_tour_length(ind.tour)


class GA_Solver():
    def solve(self) -> None:
        """Starts the solving process
        """
        # Initialise the initial population and find the global best
        population: Population = [generate_individual()
                                  for _ in range(pop_size)]
        self.g_best = min(population, key=lambda i: i.length)

        # Start the iterations
        last_update_iter = -1
        iter = 0
        while True:
            print(self.g_best.length, iter, last_update_iter)
            # Define a new population
            new_population: Population = []

            if iter - last_update_iter > EXTINCTION_ITER and random.random() < EXTINCTION_PROB:
                # Extinction commences
                # Choose number of individuals to kill in the extinction
                min_to_kill = int(EXTINCTION_RANGE[0] * pop_size)
                max_to_kill = int(EXTINCTION_RANGE[1] * pop_size)
                num_to_kill = random.randint(min_to_kill, max_to_kill)
                print("Extinction", num_to_kill)

                # Since the population is randomly ordered, we can just remove from the start of the list
                population = sorted(population, key=lambda ind: ind.length)
                population = population[num_to_kill:]

            if iter > MIN_RESTART_ITER and (iter > 2 * last_update_iter or iter - last_update_iter > MAX_RESTART_ITER):
                # Restart the algorithm if the current iteration number is twice
                # the iteration number when the last incumbent solution was found
                print("RESTART")
                population = [generate_individual() for _ in range(pop_size)]
                last_update_iter = -1
                iter = 0
                continue

            # Generate a new population
            for _ in range(pop_size):
                # Pick two fit individuals
                x = pick_individual(population)
                y = pick_individual(population)

                # Perform cross-over of the two individuals
                z: Individual = cross_over(x, y)

                if random.random() < TWO_OPT_PROB:
                    # Randomly spawn a 'genius' in the population by performing 2opt on the child
                    tour, tour_length = two_opt(z.tour, TWO_OPT_NUM_ITER)
                    z.tour = tour
                    z.length = tour_length
                elif random.random() < PROB_MUTATION:
                    # Randomly mutate the new individual
                    mutate(z, iter - last_update_iter)

                # Check if the new individual is the new global best
                if z.length < self.g_best.length:
                    self.g_best = z
                    last_update_iter = iter
                    if z.length < 1187:
                        save(self.g_best.tour, self.g_best.length)
                    print(f"{iter} - {self.g_best.length}")

                # Add the individual to the new population
                new_population.append(z)

            # Update the existing population
            population = new_population
            iter += 1

    def get_best_tour(self) -> Solution:
        """Returns a tuple containing the solution tour and its length

        Returns:
            Solution: The solution
        """
        return (self.g_best.tour, self.g_best.length)

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


solver = GA_Solver()

solver.run_with_timeout(60 * 60 * 24 * 7)

tour, tour_length = solver.get_best_tour()

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
