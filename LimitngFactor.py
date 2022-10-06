import streamlit as st
import pandas as pd

# input data from github

inputPath = r'https://raw.githubusercontent.com/DataScienceTempleFirst/EDS/a08881aeae3c63e23232ea475ab74b2a5eb6240f/spring2022/week13_14/data/Periodic_Table_of_Elements.csv'
df = pd.read_csv(inputPath, error_bad_lines=False)
cols = [2]
df = df[df.columns[cols]]
print(df)

# title

st.title('Limiting Factors Example:')

# get name and amount of element

element_num = st.number_input("How many elements are in your equation: ", value=0)

element_names = []
init_elements = []

valid_element = False

for i in range(element_num):
    valid_element = False
    while not valid_element:
        st.text("please input valid element.")
        proposed_name = st.text_input("Element:")

        if proposed_name in df:
            element_names.append(proposed_name)
            valid_element = True
            st.text("valid.")

    init_elements.append(st.number_input("Amount of " + element_names[i] + ": ", value=0))

# get amount needed of each per reaction

st.header("Amount of element needed per reaction")

reaction_elements = []

for i in range(element_num):
   init_elements.append(st.number_input("Amount of " + element_names[i] + " needed per reaction: ", value=0))

# assign starting values to elements

reactions_possible = 0

element_amount = []

for i in range(element_num):
    element_amount.append(init_elements[i])

# perform loop
repeating = True

while repeating:
    for i in range(element_num):
        element_amount - reaction_elements
        if element_amount <= 0:
            repeating = False
    reactions_possible += 1

# check to see if factor is limiting factor
limiting_factors = []

for i in range(element_num):
    if init_elements[i] - (reaction_elements[i] * (reactions_possible + 1)) < 0:
        limiting_factors.append(element_names[i])
    else:
        if element_names[i] in limiting_factors:
            limiting_factors.remove(element_names[i])

st.header("limiting factors:")
st.subheader(limiting_factors)
