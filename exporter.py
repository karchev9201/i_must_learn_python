import csv

def save_to_csv(jobs, file_name):
  if not file_name:
    file = open("jobs.csv", mode="w")
  elif file_name.endswith(".csv"):
    file = open(file_name, mode="w")
  else:
    file = open(f"{file_name}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "compan", "location", "link"])
  for job in jobs:
    writer.writerow(job.values())
  return