import streamlit as st;

st.title('Limiting Factors Example:');

init_bread = st.number_input("Amount of bread: ", min_value=None, max_value=None, value=2, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible");
init_ham = st.number_input("Amount of ham: ", min_value=None, max_value=None, value=2, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible");
init_cheese = st.number_input("Amount of cheese: ", min_value=None, max_value=None, value=2, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

st.header("Amount needed per sandwich");

bread_amount_needed = st.number_input("bread: ", min_value=None, max_value=None, value=2, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible");
ham_amount_needed = st.number_input("ham: ", min_value=None, max_value=None, value=2, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible");
cheese_amount_needed = st.number_input("cheese: ", min_value=None, max_value=None, value=2, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

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
    st.title("you can create " + str(possible_sandwiches) + " sandwich.");
else:
    st.title("you can create " + str(possible_sandwiches) + " sandwiches.");

st.header("limiting factors:");
st.aubheader(limiting_factors);