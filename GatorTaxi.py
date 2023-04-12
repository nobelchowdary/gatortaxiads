import sys

# Class to represent a min heap data structure
class MinHeap:
    def __init__(self):
        # Initialize heap list with a dummy element at index 0
        self.heap_list = [0]
        # Initialize current size of heap to 0
        self.curr_size = 0

    # Method to insert a node into the min heap
    def insert_element(self, node):
        # Add a new node to the end of the heap list
        self.heap_list += [node]
        # Increment the current size of the heap
        self.curr_size += 1
        # Fix the heap property by moving the new node up the tree as needed
        self.heapifyup(self.curr_size)

    # Method to fix the heap property by moving a node up the tree
    def heapifyup(self, n):
        # Continue swapping a node with its parent until the heap property is satisfied
        while n > 1 and self.heap_list[n].ride.less_than(self.heap_list[n // 2].ride):
            self.swapnodes(n, (n // 2))
            n //= 2

    # Method to swap two nodes in the heap
    def swapnodes(self, node1, node2):
        temp = self.heap_list[node1]
        self.heap_list[node1] = self.heap_list[node2]
        self.heap_list[node2] = temp
        self.heap_list[node1].min_heap_index = node1
        self.heap_list[node2].min_heap_index = node2

    # Method to fix the heap property by moving a node down the tree
    def heapifydown(self, n):
        # Continue swapping a node with its smaller child until the heap property is satisfied
        while (n * 2) <= self.curr_size:
            left_child = n * 2
            right_child = left_child + 1
            if right_child > self.curr_size:
                ind=left_child
            elif self.heap_list[left_child].ride.less_than(self.heap_list[right_child].ride):
                ind=left_child
            else:
                ind=right_child

            if not self.heap_list[n].ride.less_than(self.heap_list[ind].ride):
                self.swapnodes(n, ind)
            n = ind

    # Method to update the value of a node and fix the heap property accordingly
    def eleupdate(self, n, alt):
        node = self.heap_list[n]
        node.ride.tripDuration = alt
        if n == 1:
            self.heapifydown(n)
        elif self.heap_list[n // 2].ride.less_than(self.heap_list[n].ride):
            self.heapifydown(n)
        else:
            self.heapifyup(n)

    # Method to delete a node from the heap and fix the heap property accordingly
    def delete_element(self, n):

        self.swapnodes(n, self.curr_size)
        # self.heap_list[1] = self.heap_list[self.curr_size]
        self.curr_size -= 1
        *self.heap_list, _ = self.heap_list

        self.heapifydown(n)

    # Method to remove the root node from the heap and return its value
    def remove_node(self):
        # Check if heap is empty
        if len(self.heap_list) == 1:
            return 'No Rides Available'

        # Store the root node to be returned later
        root = self.heap_list[1]

        # Swap the root node with the last node in the heap and remove it
        self.swapnodes(1, self.curr_size)
        # self.heap_list[1] = self.heap_list[self.curr_size]
        self.curr_size -= 1
        *self.heap_list, _ = self.heap_list

        # Fix the heap property by moving the new root node down the tree as needed
        self.heapifydown(1)

        # Return the value of the original root node
        return root


# Class to represent a node in the min heap data structure
class MinHeapNode:
    def __init__(self, ride, rbt, min_heap_index):
        # Initialize with a reference to the ride object and its corresponding RB tree node
        self.ride = ride
        self.rbTree = rbt
        # Keep track of the index of this node in the heap list
        self.min_heap_index = min_heap_index


##################################################################################################################

# Defining a class for Red Black Tree Node
class RedBlackTree_Node:
    def __init__(self, ride, min_heap_node):
        # Initializing values for node
        self.ride = ride
        self.parent = None  # parent node
        self.left = None  # left child node
        self.right = None  # right child node
        self.color = 1  # 1=red , 0 = black
        self.min_heap_node = min_heap_node

# Defining a class for Red Black Tree
class RB_Tree:
    def __init__(self):
        # Initializing null node with default values
        self.null_node = RedBlackTree_Node(None, None)
        self.null_node.left = None
        self.null_node.right = None
        self.null_node.color = 0
        # Initializing root as null node
        self.root = self.null_node

    # To retrieve the ride with the rideNumber equal to the key
    def get_ride(self, ridenum):
        temp = self.root

        # Iterating through the tree to find the node with rideNumber equal to the key
        while temp != self.null_node:
            if temp.ride.rideNumber == ridenum:
                return temp
            # If rideNumber is greater than the current node's rideNumber, search in right subtree
            if temp.ride.rideNumber < ridenum:
                temp = temp.right
            # If rideNumber is less than the current node's rideNumber, search in left subtree
            else:
                temp = temp.left

        # If rideNumber is not found, return None
        return None

    def treebalance_afternodedelete(self, leaf):
        #
        while leaf != self.root and leaf.color == 0:
            if leaf == leaf.parent.right:
                parent_sibling = leaf.parent.left
                if parent_sibling.color != 0:
                    leaf.parent.color = 1
                    parent_sibling.color = 0
                    self.right_rotate(leaf.parent)
                    parent_sibling = leaf.parent.left

                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    leaf = leaf.parent
                else:
                    if parent_sibling.left.color != 1:
                        parent_sibling.right.color = 0
                        parent_sibling.color = 1
                        self.left_rotate(parent_sibling)
                        parent_sibling = leaf.parent.left

                    parent_sibling.color = leaf.parent.color
                    leaf.parent.color = 0
                    parent_sibling.left.color = 0
                    self.right_rotate(leaf.parent)
                    leaf = self.root
            else:
                parent_sibling = leaf.parent.right
                if parent_sibling.color != 0:
                    leaf.parent.color = 1
                    parent_sibling.color = 0
                    self.left_rotate(leaf.parent)
                    parent_sibling = leaf.parent.right

                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    leaf = leaf.parent
                else:
                    if parent_sibling.right.color != 1:
                        parent_sibling.left.color = 0
                        parent_sibling.color = 1
                        self.right_rotate(parent_sibling)
                        parent_sibling = leaf.parent.right

                    parent_sibling.color = leaf.parent.color
                    leaf.parent.color = 0
                    parent_sibling.right.color = 0
                    self.left_rotate(leaf.parent)
                    leaf = self.root

        leaf.color = 0

    def __RBT_Change(self, leaf, childleaf):
        if leaf.parent is None:
            self.root = childleaf
        elif leaf == leaf.parent.right:
            leaf.parent.right = childleaf
        else:
            leaf.parent.left = childleaf
        childleaf.parent = leaf.parent


    def removehelpernode(self, leaf, alt):
        delete_node = self.null_node
        while leaf != self.null_node:
            if leaf.ride.rideNumber == alt:
                delete_node = leaf
            if leaf.ride.rideNumber >= alt:
                leaf = leaf.left
            else:
                leaf = leaf.right

        if delete_node == self.null_node:
            return
        heap_node = delete_node.min_heap_node
        y = delete_node
        y_original_color = y.color
        if delete_node.left == self.null_node:
            x = delete_node.right
            self.__RBT_Change(delete_node, delete_node.right)
        elif (delete_node.right == self.null_node):
            x = delete_node.left
            self.__RBT_Change(delete_node, delete_node.left)
        else:
            y = self.find_minimum_node(delete_node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == delete_node:
                x.parent = y
            else:
                self.__RBT_Change(y, y.right)
                y.right = delete_node.right
                y.right.parent = y

            self.__RBT_Change(delete_node, y)
            y.left = delete_node.left
            y.left.parent = y
            y.color = delete_node.color
        if y_original_color == 0:
            self.treebalance_afternodedelete(x)

        return heap_node

    def treebalance_afterinsert(self, present_node):
        while present_node.parent.color == 1:
            if present_node.parent == present_node.parent.parent.left:
                parent_sibling = present_node.parent.parent.right

                if parent_sibling.color == 0:
                    if present_node == present_node.parent.right:
                        present_node = present_node.parent
                        self.left_rotate(present_node)
                    present_node.parent.color = 0
                    present_node.parent.parent.color = 1
                    self.right_rotate(present_node.parent.parent)
                else:
                    parent_sibling.color = 0
                    present_node.parent.color = 0
                    present_node.parent.parent.color = 1
                    present_node = present_node.parent.parent

            else:
                parent_sibling = present_node.parent.parent.left
                if parent_sibling.color == 0:
                    if present_node == present_node.parent.left:
                        present_node = present_node.parent
                        self.right_rotate(present_node)
                    present_node.parent.color = 0
                    present_node.parent.parent.color = 1
                    self.left_rotate(present_node.parent.parent)
                else:
                    parent_sibling.color = 0
                    present_node.parent.color = 0
                    present_node.parent.parent.color = 1
                    present_node = present_node.parent.parent

            if present_node == self.root:
                break
        self.root.color = 0

    def identifyrides_inrange(self, leaf, min, max, alt):
        if leaf == self.null_node:
            return

        if min < leaf.ride.rideNumber:
            self.identifyrides_inrange(leaf.left, min, max, alt)
        if min <= leaf.ride.rideNumber <= max:
            alt.append(leaf.ride)
        self.identifyrides_inrange(leaf.right, min, max, alt)

    def inrange_rides(self, low_ride_num, high_ride_num):
        res = []
        self.identifyrides_inrange(self.root, low_ride_num, high_ride_num, res)
        return res

    def find_minimum_node(self, leaf):
        while leaf.left != self.null_node:
            leaf = leaf.left
        return leaf

    def left_rotate(self, leaf):
        y = leaf.right
        leaf.right = y.left
        if y.left != self.null_node:
            y.left.parent = leaf

        y.parent = leaf.parent
        if leaf.parent == None:
            self.root = y
        elif leaf == leaf.parent.left:
            leaf.parent.left = y
        else:
            leaf.parent.right = y
        y.left = leaf
        leaf.parent = y

    def right_rotate(self, leaf):
        y = leaf.left
        leaf.left = y.right
        if y.right != self.null_node:
            y.right.parent = leaf

        y.parent = leaf.parent
        if leaf.parent == None:
            self.root = y
        elif leaf == leaf.parent.right:
            leaf.parent.right = y
        else:
            leaf.parent.left = y
        y.right = leaf
        leaf.parent = y

    def leaf_insert(self, ride, min_heap):
        node = RedBlackTree_Node(ride, min_heap)
        node.parent = None
        node.left = self.null_node
        node.right = self.null_node
        node.color = 1

        insertion_node = None
        temp_node = self.root

        while temp_node != self.null_node:
            insertion_node = temp_node
            if node.ride.rideNumber < temp_node.ride.rideNumber:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        node.parent = insertion_node
        if insertion_node is None:
            self.root = node
        elif node.ride.rideNumber > insertion_node.ride.rideNumber:
            insertion_node.right = node
        else:
            insertion_node.left = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.treebalance_afterinsert(node)

    def delete_node(self, rideNumber):
        return self.removehelpernode(self.root, rideNumber)
#################################################################################################################

class Ride:
    def __init__(self, ride_number, ride_cost, trip_duration):
        self.rideNumber = ride_number
        self.rideCost = ride_cost
        self.tripDuration = trip_duration

    def less_than(self, other_ride):
        if self.rideCost == other_ride.rideCost:
            return self.tripDuration <= other_ride.tripDuration
        return self.rideCost < other_ride.rideCost
    
    
def ride_insert(ride, heap, rbt):
    ride_exists = rbt.get_ride(ride.rideNumber) is not None
    if ride_exists:
        print_output(None, "Duplicate RideNumber", False)
        sys.exit(0)
    else:
        rbt_node = RedBlackTree_Node(None, None)
        min_heap_node = MinHeapNode(ride, rbt_node, heap.curr_size + 1)
        heap.insert_element(min_heap_node)
        rbt.leaf_insert(ride, min_heap_node)



def print_output(ride, data, holder):
    file = open("output.txt", "a")
    if ride is None:
        file.write(data + "\n")
    else:
        data = ""
        if not holder:
            data += ("(" + str(ride.rideNumber) + "," + str(ride.rideCost) + "," + str(ride.tripDuration) + ")\n")
        else:
            if len(ride) == 0:
                data += "(0,0,0)\n"
            for i in range(len(ride)):
                if i != len(ride) - 1:
                    data = data + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                        ride[i].tripDuration) + "),")
                else:
                    data = data + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                        ride[i].tripDuration) + ")\n")
        file.write(data)
    file.close()


def getride(rideNumber, rbt):
    ride = rbt.get_ride(rideNumber)
    if ride:
        print_output(ride.ride, "", False)
    else:
        default_ride = Ride(0, 0, 0)
        print_output(default_ride, "", False)



def getrides(min, max, rbt):
    list = rbt.inrange_rides(min, max)
    print_output(list, "", True)


def nextride(heap, rbt):
    if heap.curr_size == 0:
        print_output(None, "No active ride requests", False)
        return
    popped_node = heap.remove_node()
    rbt.delete_node(popped_node.ride.rideNumber)
    print_output(popped_node.ride, "", False)



def ridecancel(ridenum, heap, rbt):
    heap_node = rbt.delete_node(ridenum)
    if heap_node is not None:
        heap.delete_element(heap_node.min_heap_index)


def update_ride(ride_number, new_duration, heap_obj, rbt_obj):
    # Retrieve the ride from the red-black tree using the given ride number
    node = rbt_obj.get_ride(ride_number)
    # Check if the ride exists in the red-black tree
    if not node:
        print('')
        return
    # Update the ride duration based on the given conditionals.
    current_duration = node.ride.tripDuration
    if new_duration <= current_duration:
        heap_obj.eleupdate(node.min_heap_node.min_heap_index, new_duration)
    elif current_duration < new_duration <= current_duration * 2:
        ridecancel(node.ride.rideNumber, heap_obj, rbt_obj)
        updated_cost = node.ride.rideCost + 10
        updated_ride = Ride(node.ride.rideNumber, updated_cost, new_duration)
        ride_insert(updated_ride, heap_obj, rbt_obj)
    else:
        ridecancel(node.ride.rideNumber, heap_obj, rbt_obj)


import sys
if __name__ == "__main__":
    heap = MinHeap()
    rbt = RB_Tree()
    file = open("output.txt", "w")
    file.close()
    inputfile=sys.argv[1]
    file = open(inputfile, "r")
    for s in file.readlines():
        n = []
        for num in s[s.index("(") + 1:s.index(")")].split(","):
            if num != '':
                n.append(int(num))
        if "Insert" in s:
            ride_insert(Ride(n[0], n[1], n[2]), heap, rbt)
        elif "Print" in s:
            if len(n) == 1:
                getride(n[0], rbt)
            elif len(n) == 2:
                getrides(n[0], n[1], rbt)
        elif "UpdateTrip" in s:
            update_ride(n[0], n[1], heap, rbt)
        elif "GetNextRide" in s:
            nextride(heap, rbt)
        elif "CancelRide" in s:
            ridecancel(n[0], heap, rbt)

