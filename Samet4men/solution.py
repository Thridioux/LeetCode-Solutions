
#                                                 ---40ohm---
#                                               |            |
#                                ---30ohm---    |            |
#                               |           |   |            |
#               ---20ohm---     |           |   | ---40ohm---| 
#              |           |    |           |   |            |
# |----10ohm---|           | ---|---30ohm---|---|            |-----|
# |            |           |    |           |   |            |     |
# |             ---20ohm---     |           |   | ---40ohm---|     |
# |                             |           |   |            |     |
# |                              ---30ohm---    |            |     |
# |                                             |            |     |
# |                                               ---40ohm---      |       
# |                                                                |
# |                                                                |
# |------------------------------40V-------------------------------|
# esdeger devre direnci? , anakol akimi? , her bir direncin uzerindeki akimi,gerilimi ve gucu bul.
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def add_node(self, data):
        new_node = Node(data)
        if not self.head: 

            self.head = new_node 
        else:
            current = self.head 
            while current.next: 
                current = current.next 
            current.next = new_node 

    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    
    def generate_random_list(self, num_resistors, resistor_values):
        for _ in range(num_resistors):
            random_index = random.randint(0, len(resistor_values) - 1)
            self.add_node(resistor_values[random_index])
        

    
    def generate_sum_10_list(self):
        resistor_values = list(range(1, 101))  
        voltage = random.choice(resistor_values)
        sum_10_list = []
        current_sum = 0
        while current_sum < 10:
            next_value = random.choice(resistor_values)
            if current_sum + next_value <= 10:
                sum_10_list.append(next_value)
                current_sum += next_value
        return sum_10_list, voltage
                    
    def get_resistor_list(self):
        resistor_list = []
        current = self.head
        while current:
            resistor_list.append(current.data)
            current = current.next
        return resistor_list
    
    def calculate_equivalent_resistance(self, connection, generated_resistor_values):
        parallel_resistances = []
        series_resistance = 0
        current_index = 0
        for num_resistors in connection:
            if num_resistors == 1:
                series_resistance += generated_resistor_values[current_index]
            else:
                parallel_resistance = generated_resistor_values[current_index:current_index + num_resistors]
                parallel_resistances.append(1 / sum(1 / resistance for resistance in parallel_resistance))
            current_index += num_resistors

        equivalent_resistance = series_resistance + sum(parallel_resistances)
        return equivalent_resistance


    def anakol_akimi(self, voltage, equivalent_resistance):
        return voltage / equivalent_resistance
    
    

    def calculate_currents(self, voltage, connection, generated_resistor_values):
        currents = []
        total_resistance = 0
    
        for index, num_resistors in enumerate(connection):
            if num_resistors == 1:
            
                current = voltage / generated_resistor_values[index]
                currents.append(current)
                total_resistance += generated_resistor_values[index]
            else:
                
                parallel_resistances = generated_resistor_values[index:index + num_resistors]
                total_parallel_resistance = sum(1 / resistance for resistance in parallel_resistances)
                for resistance in parallel_resistances:
                    current = voltage / (total_parallel_resistance + total_resistance) * resistance
                    currents.append(current)
                total_resistance += 1 / total_parallel_resistance  

        return currents

    
    


        

    

            


        
    


    

        

        
        
    



    





                
        