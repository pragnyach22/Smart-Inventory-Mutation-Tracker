# Smart-Inventory-Mutation-Tracker

Overview of Project
In the current project, Python programming language will be used for simulating warehouse inventory. The project gives information about behavior of data during copying and modification through shallow and deep copy. The objective of this project is learning about impact of mutations in data within nested structure.

Problem Definition
The inventory data will be maintained in form of list of dictionaries containing information like price, stock and supplier. There will be generation of shallow and deep copies of the data followed by application of mutation. This process will help in analyzing change behavior.

Implementing Features of Problem Description

Using lists and dictionaries in data
Functionality through functions
Shallow and deep copying of data
Applying mutations like reducing prices and updating stock
Comparing data before and after applying mutations
Usage of loops and conditions
Personalization according to roll number

Functions Defined
create_inventory(): this function generates and returns initial data of inventory
apply_discount(): this function reduces price by ten percent and updates stock according to roll number
compare_data(): this function compares and counts changes in original data and modified data

Personalization Logic

Roll Number = 642
Length of inventory = 2

Index
index= 642 % 2 =0

Therefore, only the element whose index is 0, i.e., laptop, would be chosen for modifying stock.

Logic behind mutation
The price of all items shall be decreased by ten percent.
Only the stock of Laptop will be increased.
Sample Output
Original inventory
Laptop price 50000 stock 10
Phone price 20000 stock 25

After Shallow Copy Mutation
Laptop price 45000 stock 15
Phone price 18000 stock 25
Original data is also affected

After Deep Copy Mutation
Laptop price 45000 stock 15
Phone price 18000 stock 25
Original data not affected

Key Learning Points

Shallow Copy
It creates a copy only of the outer level
Inner references remain same
Changes in the data affect original data

Deep Copy
It makes complete copy including inner references
No common reference
No change in original data

Conclusion

From this project, we learn that there is a difference between shallow and deep copies. This difference needs to be understood to avoid data corruption.

Learning Points

Difference between shallow and deep copy
Concept of nested dictionary
Knowledge about functions and loop and conditions
Knowledge of how mutations occur
