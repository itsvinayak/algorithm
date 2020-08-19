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
print("AVERAGE SALARY PER GENDER")
print(mean_output)


def female_salary(row):
    if row["gender"] == "Female":
        return row["cleanup_salary"]


def male_salary(row):
    if row["gender"] == "Male":
        return row["cleanup_salary"]


df["female_salary_avg"] = df.apply(female_salary, axis=1)
df["male_salary_avg"] = df.apply(male_salary, axis=1)


print(
    df.groupby("Job Title")[
        "cleanup_salary", "male_salary_avg", "female_salary_avg"
    ].mean()
)
