import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load the training and test datasets
Train = pd.read_csv("SYBIL_MODIFIED.csv")
Test = pd.read_csv("SYBIL_TEST.csv")

# Define features to be encoded and perform one-hot encoding on the categorical features
features_to_encode = ['protocol_type', 'service', 'flag']
encoded = pd.get_dummies(Train[features_to_encode])
numeric_features = ['duration', 'src_bytes', 'dst_bytes', 'count', 'srv_count']

# Combine the encoded features with the numeric features
to_fit = encoded.join(Train[numeric_features])

# Create target variables for classification tasks
binary_y = Train['attack_flag']
multi_y = Train['attack_map']

# Test target variables
test_binary_y = Test['attack_flag']
test_multi_y = Test['attack_map']

# Define the function to train the model and make predictions
def predict(test_data):
    model = RandomForestClassifier()
    model.fit(to_fit, multi_y)
    pred = model.predict(test_data)
    return pred

# Function to encode the test dataset similarly to the training dataset
def encode(dataset):
    features_to_encode = ['protocol_type', 'service', 'flag']
    test_encoded_base = pd.get_dummies(dataset[features_to_encode])
    test_index = np.arange(len(dataset.index))
    column_diffs = list(set(encoded.columns.values) - set(test_encoded_base.columns.values))
    diff_df = pd.DataFrame(0, index=test_index, columns=column_diffs)
    column_order = encoded.columns.to_list()
    test_encoded_temp = test_encoded_base.join(diff_df)
    test_final = test_encoded_temp[column_order].fillna(0)
    return test_final

# Extract unique values for service and flag columns from the training dataset
ser = Train['service'].unique()
fg = Train['flag'].unique()

# Create an empty dataframe for user input
data = {
    'protocol_type': [None],
    'service': [None],
    'flag': [None],
    'duration': [None],
    'src_bytes': [None],
    'dst_bytes': [None],
    'count': [None],
    'srv_count': [None]
}

inp_dataset = pd.DataFrame(data)


# Create a form for user input
with st.form("sybil form"):
    inp_dataset['protocol_type'] = st.selectbox('Please select the protocol type', ('tcp', 'udp', 'icmp'))
    inp_dataset["service"] = st.selectbox('Please select the service type', (ser))
    inp_dataset["flag"] = st.selectbox('Please select the flag type', (fg))
    inp_dataset['duration'] = st.number_input("Enter duration:", min_value=0, max_value=57800)
    inp_dataset['src_bytes'] = st.number_input("Enter source bytes:", min_value=0, max_value=1380000000)
    inp_dataset['dst_bytes'] = st.number_input("Enter destination bytes:", min_value=0, max_value=1310000000)
    inp_dataset['count'] = st.number_input("Enter entity count:", min_value=0, max_value=510)
    inp_dataset['srv_count'] = st.number_input("Enter server entity count:", min_value=0, max_value=510)
    submit_button = st.form_submit_button("Submit")

# Encode the user input and combine with numeric features
data2 = encode(inp_dataset).join(inp_dataset[numeric_features])

# st.write(data2)

# Make predictions based on the user input
prediction2 = predict(data2)
inp_dataset["predicted"] = prediction2

st.write(inp_dataset)

# Display the prediction result
if submit_button:
    st.write("After analyzing the network traffic details the traiffic is: ")
    if prediction2 == 0:
        st.write("normal")
    elif prediction2 == 1:
        st.write("dos_attack")
    elif prediction2 == 2:
        st.write("probe_attack")
    elif prediction2 == 3:
        st.write("U2R attack")
    elif prediction2 == 4:
        st.write("sybil attack")
del inp_dataset