import pandas as pd


df = pd.read_csv("./sample.csv", sep=",", header=0)


def cleanup_salary(row):
    """to clean salary to replace $ sign """
    salary = row["Salary"].replace("$", "")
    salary = float(salary)
    return salary


df["cleanup_salary"] = df.apply(cleanup_salary, axis=1)


# create column called cleanup_salary
# that column is the result of salary column in the original dataframe
# after the cleanup_salary function has applied

mean_output = df.groupby("gender")["cleanup_salary"].mean()
print(mean_output)
