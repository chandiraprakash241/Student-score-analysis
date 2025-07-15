from models import Student
from utils import load_students_from_csv, write_report
from visualizer import plot_total_scores, plot_pass_fail_pie
import numpy as np

students = load_students_from_csv('students.csv')
report_lines = []

# Overall Statistics
averages = [s.average for s in students]
report_lines.append(f"Class Average: {np.mean(averages):.2f}")

# Topper
topper = max(students, key=lambda s: s.total)
report_lines.append(f"Topper: {topper.name} with {topper.total} marks")

# Failures
failed = [s for s in students if not s.is_pass()]
report_lines.append(f"Number of failed students: {len(failed)}")
for s in failed:
    report_lines.append(f"{s.name} failed in: {', '.join(s.failed_subjects())}")

# Students scoring above 90 average
distinctions = [s for s in students if s.average >= 90]
report_lines.append(f"Distinction holders (>90 avg): {len(distinctions)}")

# Write report
write_report('report.txt', report_lines)

# Generate Visuals
plot_total_scores(students)
plot_pass_fail_pie(students)

print("Analysis complete. Report and plots generated.")
