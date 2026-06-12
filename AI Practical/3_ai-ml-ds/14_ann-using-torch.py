# Import pandas for reading and handling dataset
import pandas as pd

# Import function to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Import scaler to normalize feature values
from sklearn.preprocessing import StandardScaler

# Import PyTorch and Neural Network module
import torch, torch.nn as nn


# Load CSV dataset into dataframe
df = pd.read_csv(r'D:\CS_6th\AI Practical\3_ai-ml-ds\data.csv')

# Display original dataset
print(f'At Start: \n{df}')


# Convert categorical labels into numeric values
# Fail -> 0
# Pass -> 1
df['result'] = df['result'].map({'Fail':0, 'Pass':1})

# Display dataset after label conversion
print(f'After Result Map: \n{df}')


# Extract input features (independent variables)
X = df[['study', 'attendance', 'assignments']].values

# Extract target/output column (dependent variable)
y = df['result'].values

# Display feature values
print(f'X values: {X}')

# Display target values
print(f'y values: {y}')


# Split data into training (80%) and testing (20%)
X_train, X_test = train_test_split(
    X,
    test_size=0.2,
    random_state=42
)
# Split data into training (80%) and testing (20%)
y_train, y_test = train_test_split(
    y,
    test_size=0.2,
    random_state=42
)


# Create scaler object
sc = StandardScaler()

# Learn scaling parameters from training data and normalize it
X_train = sc.fit_transform(X_train)

# Apply same scaling to testing data
X_test = sc.transform(X_test)


# Convert training features from numpy array to PyTorch tensor
X_train = torch.tensor(X_train, dtype=torch.float32)

# Convert testing features from numpy array to PyTorch tensor
X_test = torch.tensor(X_test, dtype=torch.float32)


# Convert training labels to tensor and reshape into column vector
y_train = torch.tensor(y_train, dtype=torch.float32).view(-1,1)

# Convert testing labels to tensor and reshape into column vector
y_test = torch.tensor(y_test, dtype=torch.float32).view(-1,1)


# Display shape of training feature matrix
print(X_train.shape)

# Display shape of training labels
print(y_train.shape)


# Create ANN model
# Linear Layer:
# 3 input neurons (study, attendance, assignments)
# 1 output neuron (Pass/Fail)
# Sigmoid converts output into probability between 0 and 1
nn_model = nn.Sequential(
    nn.Linear(3,1),
    nn.Sigmoid()
)


# Binary Cross Entropy loss function for binary classification
nn_loss = nn.BCELoss()

# Stochastic Gradient Descent optimizer with learning rate 0.01
nn_optmzr = torch.optim.SGD(
    nn_model.parameters(),
    lr=0.01
)


# Train model for 15 epochs
for epoch in range(15):

    # Forward pass: generate predictions
    y_pred = nn_model(X_train)

    # Calculate prediction error
    loss = nn_loss(y_pred, y_train)

    # Clear previously stored gradients
    nn_optmzr.zero_grad()

    # Perform backpropagation to calculate gradients
    loss.backward()

    # Update model weights and biases
    nn_optmzr.step()

    # Display loss after each epoch
    print(loss.item())


# Disable gradient calculation during testing
with torch.no_grad():

    # Predict outputs for testing data
    test_pred = nn_model(X_test)

    # Convert probabilities into classes
    # >= 0.5 => Pass (1)
    # < 0.5 => Fail (0)
    predtd = (test_pred >= 0.5).float()

    # Calculate prediction accuracy
    acc = (predtd == y_test).float().mean()

    # Display accuracy
    print(f'Accuracy: {acc.item()}')