import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class CascadeImbalancePredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        
    def generate_synthetic_market_data(self, n_samples=1000):
        np.random.seed(42)
        data = {
            'load_forecast': np.random.normal(12000, 1500, n_samples),
            'da_price': np.random.normal(80, 25, n_samples),
            'solar_gen': np.random.uniform(0, 4000, n_samples),
            'wind_gen': np.random.uniform(1000, 6000, n_samples),
            'ida2_auction': np.random.normal(85, 30, n_samples),
            'last_known_imbalance': np.random.normal(0, 200, n_samples),
        }
        df = pd.DataFrame(data)
        df['is_extreme_imbalance'] = ((df['last_known_imbalance'].abs() > 350) | 
                                      (df['da_price'] > 130)).astype(int)
        return df

    def fit_cascade_layers(self, df):
        features = ['load_forecast', 'da_price', 'solar_gen', 'wind_gen', 'ida2_auction', 'last_known_imbalance']
        X = df[features]
        y = df['is_extreme_imbalance']
        self.model.fit(X, y)
        return self.model
