import streamlit as st;

st.title('Limiting Factors Example:');

init_bread = st.number_input("Amount of bread: ", min_value=None, max_value=None, value=2, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
init_ham = int(input("Amount of ham: "));
init_cheese = int(input("Amount of cheese: "));

bread_amount_needed = int(input("Amount of bread needed per sandwich: "));
ham_amount_needed = int(input("Amount of ham needed per sandwich: "));
cheese_amount_needed = int(input("Amount of cheese needed per sandwich: "));

possible_sandwiches = 0;

bread = init_bread;
ham = init_bread;
cheese = init_cheese;

while ((bread - bread_amount_needed) >= 0) and ((ham - ham_amount_needed) >= 0) and ((cheese - cheese_amount_needed) >= 0):
    possible_sandwiches += 1;
    bread -= bread_amount_needed;
    ham -= ham_amount_needed;
    cheese -= cheese_amount_needed;

limiting_factors = [];
if (init_bread - (bread_amount_needed * (possible_sandwiches + 1)) < 0):
    limiting_factors.insert(0, "bread");

if (init_ham - (ham_amount_needed * (possible_sandwiches + 1)) < 0):
    limiting_factors.insert(0, "ham");

if (init_cheese - (cheese_amount_needed * (possible_sandwiches + 1)) < 0):
    limiting_factors.insert(0, "cheese");

if (possible_sandwiches == 1):
    print("you can create " + str(possible_sandwiches) + " sandwich.");
else:
    print("you can create " + str(possible_sandwiches) + " sandwiches.");

print("limiting factors:");
print(limiting_factors);