import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_indeed_jobs(query, location, num_pages):
    jobs = []
    for page in range(num_pages):
        url = f"https://www.indeed.com/jobs?q={query}&l={location}&start={page*10}"
        print(f"Scraping URL: {url}")  # Debugging line
        response = requests.get(url)
        
        # Affichez le contenu HTML pour vérifier la structure
        print(response.text)  # Debugging line
        
        soup = BeautifulSoup(response.text, 'html.parser')
        job_elements = soup.find_all('div', class_='job_seen_beacon')
        
        print(f"Found {len(job_elements)} job elements on page {page}")  # Debugging line
        
        for job_elem in job_elements:
            title_elem = job_elem.find('h2', class_='jobTitle')
            company_elem = job_elem.find('span', class_='companyName')
            location_elem = job_elem.find('div', class_='companyLocation')
            date_elem = job_elem.find('span', class_='date')

            title = title_elem.text if title_elem else 'N/A'
            company = company_elem.text if company_elem else 'N/A'
            location = location_elem.text if location_elem else 'N/A'
            date = date_elem.text if date_elem else 'N/A'

            jobs.append({
                'Title': title,
                'Company': company,
                'Location': location,
                'Date': date
            })

    return jobs

if __name__ == "__main__":
    query = 'data'
    location = 'Africa'
    num_pages = 5
    jobs = scrape_indeed_jobs(query, location, num_pages)
    print(f"Total jobs scraped: {len(jobs)}")  # Debugging line
    df = pd.DataFrame(jobs)
    df.to_csv('indeed_jobs.csv', index=False)
    print("Les données ont été extraites et sauvegardées dans 'indeed_jobs.csv'.")
