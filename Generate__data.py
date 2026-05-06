import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate mock real estate data
n_samples = 1000

data = {
    'Square_Feet': np.random.randint(800, 5000, n_samples),
    'Bedrooms': np.random.randint(1, 6, n_samples),
    'Bathrooms': np.random.randint(1, 4, n_samples),
    'Age_Years': np.random.randint(0, 50, n_samples),
    'Location_Score': np.random.randint(1, 10, n_samples)
}

df = pd.DataFrame(data)

# Calculate Price based on a formula with some random noise
base_price = 50000
price = (
    base_price + 
    (df['Square_Feet'] * 150) + 
    (df['Bedrooms'] * 25000) + 
    (df['Bathrooms'] * 15000) - 
    (df['Age_Years'] * 1000) + 
    (df['Location_Score'] * 30000) + 
    np.random.normal(0, 20000, n_samples) # Add realistic noise
)

df['Price'] = price.round(2)

# Save to CSV
df.to_csv('real_estate_data.csv', index=False)
print("✅ Successfully generated 'real_estate_data.csv'")
