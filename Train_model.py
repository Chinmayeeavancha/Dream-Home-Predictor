import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

print("Loading data...")
df = pd.read_csv('real_estate_data.csv')

# Features and Target
X = df[['Square_Feet', 'Bedrooms', 'Bathrooms', 'Age_Years', 'Location_Score']]
y = df['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Random Forest Model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Model Performance:")
print(f"Mean Absolute Error: ${mae:,.2f}")
print(f"R-Squared (Accuracy): {r2:.2f}")

# Save the trained model
joblib.dump(model, 'house_price_model.pkl')
print("✅ Model saved as 'house_price_model.pkl'")
