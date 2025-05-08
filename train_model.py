import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv('college_cutoff_data.csv')

# Preprocessing
le_college = LabelEncoder()
df['College_Code'] = le_college.fit_transform(df['College'])

# Features and target
X = df[['Closing Rank']]
y = df['College_Code']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model and label encoder
joblib.dump(model, 'college_model.pkl')
joblib.dump(le_college, 'label_encoder.pkl')
