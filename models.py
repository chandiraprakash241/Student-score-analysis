class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # dictionary {subject: mark}
        self.total = sum(marks.values())
        self.average = self.total / len(marks)

    def is_pass(self):
        return all(m >= 40 for m in self.marks.values())

    def failed_subjects(self):
        return [sub for sub, m in self.marks.items() if m < 40]
