import pytest
import pandas as pd
from src.cascade_model import CascadeImbalancePredictor

def test_data_generation():
    predictor = CascadeImbalancePredictor()
    df = predictor.generate_synthetic_market_data(n_samples=100)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert 'is_extreme_imbalance' in df.columns

def test_model_training():
    predictor = CascadeImbalancePredictor()
    df = predictor.generate_synthetic_market_data(n_samples=200)
    model = predictor.fit_cascade_layers(df)
    
    # تست اینکه مدل آموزش دیده و قابلیت پیش‌بینی دارد
    features = ['load_forecast', 'da_price', 'solar_gen', 'wind_gen', 'ida2_auction', 'last_known_imbalance']
    preds = model.predict(df[features])
    
    assert len(preds) == 200
    assert set(preds).issubset({0, 1})
