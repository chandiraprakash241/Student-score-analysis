import matplotlib.pyplot as plt

def plot_total_scores(students):
    names = [s.name for s in students]
    totals = [s.total for s in students]
    plt.bar(names, totals, color='skyblue')
    plt.title('Total Marks of Students')
    plt.xlabel('Students')
    plt.ylabel('Total Marks')
    plt.savefig('total_scores.png')
    plt.close()

def plot_pass_fail_pie(students):
    pass_count = sum(1 for s in students if s.is_pass())
    fail_count = len(students) - pass_count
    plt.pie([pass_count, fail_count], labels=['Pass', 'Fail'], autopct='%1.1f%%', colors=['green', 'red'])
    plt.title('Pass vs Fail')
    plt.savefig('pass_fail_pie.png')
    plt.close()
