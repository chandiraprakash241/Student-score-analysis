import pandas as pd
from models import Student

def load_students_from_csv(filename):
    df = pd.read_csv(filename)
    students = []
    for _, row in df.iterrows():
        name = row['name']
        marks = row.drop('name').to_dict()
        students.append(Student(name, marks))
    return students

def write_report(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
