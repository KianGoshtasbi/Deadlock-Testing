import json
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report



def main():
    df = pd.read_csv('itemAttributes.csv')
    df['win_rate'] = df['wins'] / df['matches']
    df['high_win_rate'] = (df['win_rate'] > df['win_rate'].median()).astype(int)

    X = df[['cost', 'tier', 'matches', 'players']]
    y = df['high_win_rate']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("Feature Importance:")
    for feature, importance in zip(X.columns, model.feature_importances_):
        print(f"{feature}: {importance:.2f}")


    



if __name__ == "__main__":
    main()