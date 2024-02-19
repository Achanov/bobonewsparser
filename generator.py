import sqlite3
import datetime
from jinja2 import Environment, FileSystemLoader
conn = sqlite3.connect('news.db')
cursor = conn.cursor()
now = datetime.datetime.now()
twenty_four_hours_ago = now - datetime.timedelta(hours=24)
cursor.execute("""
SELECT * FROM news WHERE date >= ? ORDER BY date DESC
""", (twenty_four_hours_ago.strftime('%Y-%m-%d %H:%M'),))
news_items = cursor.fetchall()
conn.close()
env = Environment(loader=FileSystemLoader('.'))
def truncate_text(text, length=170):
    if len(text) > length:
        return text[:length] + '...'
    else:
        return text
env.filters['truncate'] = truncate_text
template = env.get_template('news_template.html')
html_content = template.render(news_items=news_items)
with open('news.html', 'w', encoding='utf-8') as f:
    f.write(html_content)