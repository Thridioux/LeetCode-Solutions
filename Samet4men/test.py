from solution import LinkedList

if __name__ == "__main__":
    num_resistors = 10
    resistor_values = list(range(1, 101)) 

    linked_list = LinkedList()
    linked_list.generate_random_list(num_resistors, resistor_values)

    sum_10_list, voltage = linked_list.generate_sum_10_list()
    print("List with sum of 10:", sum_10_list)
    print("Randomly selected voltage:", voltage)

    print("Resistor List:", linked_list.get_resistor_list())
    
    
    print("Equivalent Resistance:", linked_list.calculate_equivalent_resistance(sum_10_list, linked_list.get_resistor_list()))
    
    print("anakol akimi:", linked_list.anakol_akimi(voltage, linked_list.calculate_equivalent_resistance(sum_10_list, linked_list.get_resistor_list())))


    currents = linked_list.calculate_currents(voltage, sum_10_list, linked_list.get_resistor_list())
    print("Currents on each resistor:", currents)

    # expected output:

    # List with sum of 10: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 17.55+2.0611448489+34.6887417327




