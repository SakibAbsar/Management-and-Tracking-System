
import pandas as pd
import matplotlib.pyplot as plt

def generate_risk_dashboard(file_path):
    df = pd.read_excel(file_path)
    risks = df.groupby("Impact")["Likelihood"].count()
    risks.plot(kind="bar")
    plt.title("Risk Dashboard")
    plt.xlabel("Risk Impact Level")
    plt.ylabel("Number of Risks")
    plt.savefig("reports/risk_dashboard.png")
    plt.show()

if __name__ == "__main__":
    generate_risk_dashboard("config/risk_register_template.xlsx")
