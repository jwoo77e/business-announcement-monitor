import os
import csv
import requests
import datetime
from bs4 import BeautifulSoup
from email.message import EmailMessage
import smtplib
from io import StringIO

KEYWORDS = ["AI", "안전보건", "안전", "보건", "스마트", "산업", "건설"]
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/1EzNv1x1ReMixooDTOIFx6TeGjklgi--BYbNixPSeSi4/export?format=csv&gid=749793349"


def fetch_sites():
    resp = requests.get(SHEET_CSV_URL)
    resp.raise_for_status()
    content = resp.content.decode("utf-8")
    reader = csv.reader(StringIO(content))
    urls = []
    for row in reader:
        # URL이 4번째 열(인덱스 3)에 있다고 가정
        if len(row) > 3 and row[3].startswith("http"):
            urls.append(row[3])
    return urls


def scan_site(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        results = []
        for a in soup.find_all("a"):
            text = a.get_text(strip=True)
            link = a.get("href")
            if not link:
                continue
            for kw in KEYWORDS:
                if kw.lower() in text.lower():
                    results.append({
                        "공고명": text,
                        "링크": requests.compat.urljoin(url, link),
                        "내용": "",
                        "게시일": datetime.date.today().isoformat(),
                        "공고 기한": ""
                    })
                    break
        return results
    except Exception as e:
        print(f"Error scanning {url}: {e}")
        return []


def gather_announcements():
    urls = fetch_sites()
    all_results = []
    for u in urls:
        all_results.extend(scan_site(u))
    return all_results


def build_csv(data):
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=["공고명", "링크", "내용", "게시일", "공고 기한"])
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()


def send_email(csv_content):
    user = os.environ["GMAIL_USER"]
    pwd = os.environ["GMAIL_PASS"]

    msg = EmailMessage()
    msg["Subject"] = "[자동] 신규 사업 공고 알림"
    msg["From"] = user
    msg["To"] = "jaewoo.kim@riskzero.kr"
    msg.set_content("첨부된 CSV 파일을 확인해 주세요.")
    msg.add_attachment(csv_content.encode("utf-8"), maintype="text", subtype="csv", filename="announcements.csv")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(user, pwd)
        smtp.send_message(msg)


if __name__ == "__main__":
    data = gather_announcements()
    if data:
        csv_content = build_csv(data)
        send_email(csv_content)
