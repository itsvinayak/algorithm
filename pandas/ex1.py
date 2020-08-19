import pandas as pd


df = pd.read_csv("./exercise_course.csv", sep=",", header=0)


print(df.groupby("url")["bytes"].mean())


gender_wise = df.groupby("gender")["bytes"].mean()
print(gender_wise)


def male_used(row):
    if row["gender"] == "Male":
        return row["bytes"]


def female_used(row):
    if row["gender"] == "Female":
        return row["bytes"]


df["male_used"] = df.apply(male_used, axis=1)
df["female_used"] = df.apply(female_used, axis=1)


print(df.groupby("url")["bytes", "male_used", "female_used"].mean())
