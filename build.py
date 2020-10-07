# Building A Python Script

# Python Script for Index.Html
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
index_html = open('content/index.html').read()
index.html = top_html + index_html + bottom_html
print(index.html)

# Python Script for TechNews.Html
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
technews_html = open('content/technews.html').read()
index.html = top_html + technews_html + bottom_html
print(technews.html)

# Python Script for Portfolio.Html
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
portfolio_html = open('content/portfolio.html').read()
index.html = top_html + portfolio_html + bottom_html
print(portfolio.html)

# Python Script for Contact.Html
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
contact_html = open('content/contact.html').read()
index.html = top_html + contact_html + bottom_html
print(content.html)
