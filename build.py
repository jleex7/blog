def apply_template(filename, page_title):
	#opens base template
	base = open('templates/base.html').read()
	#update title in base template page with title from list
	title_content = base.replace('{{title}}', page_title)
	#opens content files [look at loops]
	content = open(filename).read()
	#combine base template + content pages
	combined_content = title_content.replace('{{content}}', content)
	print(combined_content)
	#returns combined_content
	return combined_content

def write_outputpage(outputFilename, combined_page):
	#opens updated content file and write it into docs folder
	open(outputFilename, 'w+').write(combined_page)

def main():

	# creates a list of directories called pages
	pages = [
			{
				'filename': 'content/index.html',
				'output': 'docs/index.html',
				'title': 'About Me',
			},
			{
				'filename': 'content/technews.html',
				'output': 'docs/technews.html',
				'title': 'Tech News',
			},
			{		
				'filename': 'content/portfolio.html',
				'output': 'docs/portfolio.html',
				'title': 'My Portfolio',
			},
			{		
				'filename': 'content/contact.html',
				'output': 'docs/contact.html',
				'title': 'Contact Me',
			},
			]



    # runs for loop for index/tech_news/portfolio/contact in pages and writes the files in doc folder
	for page in pages:
		combined_page = apply_template(page['filename'], page['title'])
		print(combined_page)
		write_outputpage(page['output'], combined_page)

main()