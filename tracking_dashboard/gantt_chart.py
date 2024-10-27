
import pandas as pd
import matplotlib.pyplot as plt

def generate_gantt_chart(file_path):
    df = pd.read_excel(file_path)
    fig, ax = plt.subplots(figsize=(10, 6))

    for idx, row in df.iterrows():
        ax.barh(row["Task Name"], row["End Date"] - row["Start Date"], left=row["Start Date"])
    
    plt.xlabel("Timeline")
    plt.title("Project Gantt Chart")
    plt.savefig("reports/gantt_chart.png")
    plt.show()

if __name__ == "__main__":
    generate_gantt_chart("config/project_plan_template.xlsx")
