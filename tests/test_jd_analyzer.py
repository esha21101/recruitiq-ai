from src.parsers.job_parser import extract_job_description
from src.jd.jd_analyzer import analyze_job_description

jd = extract_job_description(
    "data/raw/job_description.docx"
)

result = analyze_job_description(jd)

print("\nJOB ANALYSIS\n")

for key, value in result.items():

    print(f"{key}:\n{value}\n")