import pandas as pd

def recommend_funds(risk_level):
    # Load recommendation file
    recommendations = pd.read_csv("fund_recommendations.csv")

    risk_level = risk_level.lower()

    print("\n===== Mutual Fund Recommendation =====\n")
    print("Risk Level:", risk_level.capitalize())
    print()

    return recommendations


if __name__ == "__main__":
    level = input("Enter Risk Level (Low / Medium / High): ")

    result = recommend_funds(level)

    print(result)