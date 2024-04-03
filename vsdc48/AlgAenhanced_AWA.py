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

input_file = "AISearchfile100.175.txt"

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

algorithm_code = "AS"

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

from typing import List, Tuple, Set, Dict
from heapq import heappush, heappop
from dataclasses import dataclass
from threading import Thread
from line_profiler import profile

# Type aliases
Tour = CityList = Tuple[int, ...]
HeapItem = Tuple[float, Tour]   # f_w(n), tour of the node
Heap = List[HeapItem]
Solution = Tuple[Tour, int]

# Define infinity, and the set of all cities
INFINITY = float('inf')
ALL_CITIES = set(range(num_cities))

@dataclass
class Node:
    id: int         # Unique id of the node
    tour: Tour      # The tour
    unvisited: Set  # Unvisited nodes in the tour
    g: int          # g(n)
    f: int          # f(n) = g(n) + h(n)
    fp: float       # f'(n) = g(n) + h'(n)

# Define data structure for open and closed lists
NodeDict = Dict[Tour, Node]

@profile
def nn_complete_tour(tour: Tour) -> Tuple[CityList, int]:
    """Uses the nearest-neighbour algorithm to complete a partial `tour` and returns the cities and cost of completing the tour

    Args:
        tour (Tour): The partially completed tour

    Returns:
        Tuple[CityList, int]: Returns an tuple containing: an ordered list of the cities used to complete the tour and the cost of doing so
    """
    # Compute the unvisited cities
    unvisited = ALL_CITIES - set(tour)
    
    # Declare vars to store the cities used to complete the tour and the cost of doing so
    last_element, added_cities, added_cost = tour[-1], tuple(), 0
    
    # Keep iterating until
    while unvisited:
        # Find the next shortest edge
        min_city = min(unvisited, key=lambda x: dist_matrix[last_element][x])
        
        # Add the edge to the running total
        added_cities += (min_city,)
        added_cost += dist_matrix[last_element][min_city]
        
        # Mark it as visited and set it as the last element
        unvisited -= {min_city}
        last_element = min_city
    
    # Add the final edge to the cost
    added_cost += dist_matrix[added_cities[-1]][tour[0]]
    
    return added_cities, added_cost

@profile
def compute_MST_cost(unvisited: CityList) -> int:
    """Domain-ptimised implementation of prim's MST algorithm used to calculate the cost of creating a minimum spanning tree using the unvisited cities in the tour

    Args:
        unvisited (CityList): Cities not yet visited in the tour

    Returns:
        int: Cost of creating the Minimum Spanning Tree (MST) (Total weight)
    """
    # Arbitrarily pick the starting city
    start = unvisited[0]
    
    # Min-heap to store cities not yet included in the MST
    heap = [(0, start)]
    
    # Keep track of cities included in MST, and the cost of the MST
    in_mst = [False] * num_cities
    mst_cost = 0
    
    # Keep track of key values i.e. current shortest distance to connect the vertex
    # This is done to reduce the number of potential candidate edges added to the heap
    key_values = [INFINITY] * num_cities
    key_values[start] = 0
    
    # Convert unvisited to a set and store dist_matrix as a local reference for faster computation 
    set_unvisited = set(unvisited)
    d = dist_matrix
    
    while True:
        # Pick the minimum-cost city from the heap
        key, u = heappop(heap)
        
        # Skip if this city is already included in the MST
        if not in_mst[u]:
            # Add the picked vertex to the MST and remove it from unvisited
            mst_cost += key
            in_mst[u] = True
            set_unvisited.remove(u)
            
            # Check if MST has been fully constructed
            if not set_unvisited:
                break
            
            # Add adjacent vertices to the heap if they are cheaper than the current best way to connect the vertex
            for v in set_unvisited:
                if d[u][v] < key_values[v]:
                    key_values[v] = d[u][v]
                    heappush(heap, (d[u][v], v))
                
    return mst_cost

class RW_AS_Solver:
    @profile
    def __init__(self, init_city: int = 0, w: int = 2) -> None:
        """Constructor for the enhanced A* Solver

        Args:
            init_city (int, optional): The initial city where the solver starts from. Defaults to 0.
            w (int, optional): The weight of the heuristic in the evaluation function. Defaults to 2.
        """
        # Define the open and closed lists
        self.O: NodeDict = dict()
        self.C: NodeDict = dict()
        
        # Store init arguments
        self.init_city = init_city
        self.w = w

        # Declare a min-heap for the open-list
        self.F: Heap = []
        
        # Define a dict to store past computations of minimum spanning trees
        self.MST: Dict[CityList, int] = dict()
        
        # Define the current solution node
        self.sol_node: Solution = (None, INFINITY)
        
        # Integral node identifier
        self.new_id: int = 0
        
        # Calculate initial node's values
        tour = (init_city,)
        unvisited = ALL_CITIES - set(tour)
        h = self.heuristic(tour, unvisited)
        
        # Define the initial node
        node = Node(self.new_id, tour, unvisited, 0, h, w * h)
        self.new_id += 1
        
        # Add it to the fringe (open-list)
        self.add_to_fringe(node)

    @profile
    def heuristic(self, tour: Tour, unvisited: Set) -> int:
        """Computes the heuristic of a given tour by computing the cost of building an MST containing the unvisited nodes

        Args:
            tour (Tour): The current (partial) tour
            unvisited (Set): The currently unvisited cities

        Returns:
            int: The cost of building an MST containing the unvisited cities
        """
        # If the there are no other cities to visit
        if not unvisited:
            return dist_matrix[tour[-1]][tour[0]]
        
        # Sort the unvisited cities for hashing and memoisation
        unvisited = tuple(sorted(unvisited))

        # Compute the MST cost if it hasn't been computed before
        if not unvisited in self.MST:
            self.MST[unvisited] = compute_MST_cost(unvisited)

        # Return the cost of the MST
        return self.MST[unvisited]

    @profile
    def add_to_fringe(self, node: Node) -> None:
        """Adds a particular search node to the fringe (and open list)

        Args:
            node (Node): The search node to be added to the fringe
        """
        # Register the node in the open list        
        self.O[node.tour] = node
        
        # Add the node to the fringe (min-heap)
        heappush(self.F, (node.fp, node.tour))

    @profile   
    def pop_from_closed_list(self, tour: Tour) -> Node:
        """Pops a given search node identified by its tour from the closed list

        Args:
            tour (Tour): The tour of the search node

        Returns:
            Node: The search node found in the closed list
        """
        return self.C.pop(tour)

    @profile
    def solve(self) -> None:
        while self.O:
            # Pop item from fringe (min-heap) with minimum evaluation value
            heap_item = heappop(self.F)
            
            # Pop the node from the open list based on the tour found in the heap item
            n: Node = self.O.pop(heap_item[1])
            
            # Only proceed if no solution found yet or if the evaluation function of popped node is better than the current best
            if not self.sol_node[0] or n.f < self.sol_node[1]:
                # Add the search node to the closed list
                self.C[n.tour] = n
                
                # Iterate through all children of the search node
                for c in n.unvisited:
                    # Compute values of the child searchnode
                    tour = n.tour + (c,)
                    unvisited = n.unvisited - {c}
                    cost = dist_matrix[n.tour[-1]][c]
                    g = n.g + cost
                    h = self.heuristic(tour, unvisited)
                    
                    # Define the child search node
                    child = Node(self.new_id, tour, unvisited, g, g + h, g + self.w * h)
                    self.new_id += 1
                    
                    # Proceed if child's evaluation function is better than current best solution
                    if child.f < self.sol_node[1]:
                        if len(child.tour) == num_cities:
                            # Save as solution node if it is a goal node
                            print(child.f)
                            self.sol_node = (child.tour, child.f)
                        # elif (child.tour in self.O or child.tour in self.C) and child.g > n.g + cost:
                        #     if child.tour in self.C:
                        #         self.pop_from_closed_list(child.tour)
                        #         self.add_to_fringe(child)
                        elif child.tour in self.C:
                            print("test")
                            self.pop_from_closed_list(child.tour)
                            self.add_to_fringe(child)
                        else:
                            self.add_to_fringe(child)        

    @profile
    def get_best_tour(self) -> Solution:
        # Return the best solution found by the algorithm
        if self.sol_node[0]:
            return list(self.sol_node[0]), self.sol_node[1]
        else:
            best_tour = [0]
            best_length = 0
            
            # Pop a potential best node from fringe
            min_node = self.F[0]
            if min_node:
                best_tour = min_node[1]
                best_length = self.O[best_tour].g
            
            # Complete the partial tour by using recursive nearest neighbour
            added_cities, added_cost = nn_complete_tour(best_tour)
            
            return list(best_tour + added_cities), best_length + added_cost

    @profile
    def run_with_timeout(self, timeout: int = 59) -> bool:
        # Run the solver for `timeout` number of seconds and return whether the solver timed otu
        solver_thread = Thread(target=self.solve)
        solver_thread.daemon = True
        solver_thread.start()
        solver_thread.join(timeout)

        return solver_thread.is_alive()

solver = RW_AS_Solver(init_city=0, w=2)

solver.run_with_timeout(15)

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
