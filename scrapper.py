import requests
from bs4 import BeautifulSoup

def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"s-pagination"})
  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(link.find("span").string)
  last_page = int(pages[-1])
  return last_page;

def extract_per_job_info(html, url):
  title = html.find("h2").find("a")['title']
  companyAndLocation = html.find("h3").find_all("span")
  company = companyAndLocation[0].get_text(strip=True)
  location = companyAndLocation[1].get_text(strip=True)
  link = f"{url}/{html['data-jobid']}"
  return {'title':title, 'company':company, 'location':location,
  'link':link}

def get_jobs(last_page, url):
  jobs = []
  for page in range(last_page):
    print(f"SO Jobs Data Extract, at Page: {page}")
    result = requests.get(f"{url}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
      job = extract_per_job_info(result, url)
      
      jobs.append(job)
  return jobs

def jobs(question_keyword):
  url = f"https://stackoverflow.com/jobs?q={question_keyword}"
  last_page = get_last_page(url)
  jobs = get_jobs(last_page, url)
  return jobs
