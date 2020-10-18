def main():

    # creates a list of directories called pages
	pages = [
            {
                'filename': 'content/index.html',
                'output': 'docs/index.html',
                'title': 'Index',
            },
            {
                'filename': 'content/technews.html',
                'output': 'docs/technews.html',
                'title': 'Tech_News',
            },
            {		
                'filename': 'content/portfolio.html',
                'output': 'docs/portfolio.html',
                'title': 'Portfolio',
            },
            {		
                'filename': 'content/contact.html',
                'output': 'docs/contact.html',
                'title': 'Contact',
            },
            ]

    
	def joinpage(filename):
		#read the top template
		top = open('templates/top.html').read()
		#read content file
		content = open(filename).read()
		#read bottom template
		bottom = open('templates/bottom.html').read()
		#combine top + content + file
		combined_content = top + content + bottom
		print(combined_content)
		#returns combined_content to value
		return combined_content

	def write_outputpage(outputFilename, combined_page):
        # opens updated content file and write it into docs folder
		open(outputFilename, 'w+').write(combined_page)

    # runs for loop for index/tech_news/portfolio/contact in pages and writes the files in doc folder
	for page in pages:
		page_title = page['title']
		print(page_title)
		combined_page = joinpage(page['filename'])
		print(combined_page)
		write_outputpage(page['output'], combined_page)
               
main()