# AlphaScope Database Schema

## companies

company_id
name
industry
ticker
created_at

---

## reports

report_id
company_id
created_at
executive_summary
risk_score
sentiment_score

---

## agent_outputs

output_id
report_id
agent_name
output_text

---

## news_articles

article_id
company_id
headline
source
url
published_date
sentiment

---

## topics

topic_id
report_id
topic_name

---

## chat_history

chat_id
report_id
question
answer
created_at

---

## similar_companies

id
company_id
similar_company
similarity_score
