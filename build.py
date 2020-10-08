# Building A Python Script

# Python Script for Index.Html
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
index_html = open('content/index.html').read()
combined_index = top_html + index_html + bottom_html
print(combined_index)
open('docs/index.html', 'w+').write(combined_index)

# Python Script for TechNews.Html
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
technews_html = open('content/technews.html').read()
combined_technews = top_html + technews_html + bottom_html
print(combined_technews)
open('docs/technews.html', 'w+').write(combined_technews)

# Python Script for Portfolio.Html
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
portfolio_html = open('content/portfolio.html').read()
combined_portfolio = top_html + portfolio_html + bottom_html
print(combined_portfolio)
open('docs/portfolio.html', 'w+').write(combined_portfolio)

# Python Script for Contact.Html
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
contact_html = open('content/contact.html').read()
combined_contact = top_html + contact_html + bottom_html
print(combined_contact)
open('docs/contact.html', 'w+').write(combined_contact)
