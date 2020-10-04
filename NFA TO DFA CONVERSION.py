#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Taking NFA input from User 

nfa = {}                                 
n = int(input("Please Enter No. Of States : "))            
t = int(input("Please Enter No. Of Transitions/Paths : "))       # EX: a,b so input 2 for a,b,c input 3
for i in range(n):  
    state = input("Enter The State Name : ")                     # Ex: A, B, C, q1, q2 ..etc
    nfa[state] = {}                                              # Creating a nested dictionary
    for j in range(t):
        path = input("Enter The Path : ")                        # Ex: a or b in {a,b} 0 or 1 in {0,1}
        print("Enter The End state From State {} Travelling Through Path {} : ".format(state,path))
        reaching_state = [x for x in input().split()]            # Enter all the end states 
        nfa[state][path] = reaching_state                        # Assigning the end states to the paths in dictionary

print("\n NFA :- \n")
print(nfa)                                                       # Printing NFA
print("\n Printing NFA Table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter The Final State of NFA : ")
nfa_final_state = [x for x in input().split()]                   # Final state/states of NFA
              
    
new_states_list = []                                             # Holds all the new states created in dfa
dfa = {}                                                         # Dfa dictionary/table or the output structure we needed
keys_list = list(list(nfa.keys())[0])                            # Conatins all the states in nfa plus the states created in dfa are also appended further
path_list = list(nfa[keys_list[0]].keys())                       # List of all the paths eg: [a,b] or [0,1]



# Computing First Row of DFA Transition Table

dfa[keys_list[0]] = {}                                           # Creating a nested dictionary in dfa 
for y in range(t):
    var = "".join(nfa[keys_list[0]][path_list[y]])               # Creating a single string from all the elements of the list which is a new state
    dfa[keys_list[0]][path_list[y]] = var                        # Assigning the state in DFA table
    if var not in keys_list:                                     # If the state is newly created 
        new_states_list.append(var)                              # Then append it to the new_states_list
        keys_list.append(var)                                    # As well as to the keys_list which contains all the states
        
 
# Computing the other rows of DFA transition table

while len(new_states_list) != 0:                                # Consition is true only if the new_states_list is not empty
    dfa[new_states_list[0]] = {}                                # Taking the first element of the new_states_list and examining it
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []                                           # Creating a temporay list
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]# Taking the union of the states
            s = ""
            s = s.join(temp)                                    # Creating a single string(new state) from all the elements of the list
            if s not in keys_list:                              # If the state is newly created
                new_states_list.append(s)                       # Then append it to the new_states_list
                keys_list.append(s)                             # As well as to the keys_list which contains all the states
            dfa[new_states_list[0]][path_list[i]] = s           # Assigning the new state in the DFA table
        
    new_states_list.remove(new_states_list[0])                  # Removing the first element in the new_states_list

print("\n DFA :-- \n")    
print(dfa)                                                      # Printing the DFA created
print("\n Printing DFA Table :-- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break
        
print("\n Final States Of The DFA Are : ",dfa_final_states)       #Printing Final states of DFA


# In[ ]:




