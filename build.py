
# Lists of pages stored in dictionary

pages = [
	{ 
	"filename": "content/index.html",
	"output": "docs/index.html",
	"title": "Meet Steve",
	},
	{ 
	"filename": "content/projects.html",
	"output": "docs/projects.html",
	"title": "My future projects",
	},
	{ 
	"filename": "content/contact.html",
	"output": "docs/contact.html",
	"title": "Contact me",
	}
]


print ('Using functions and loops to combine pages')


# Using function to make template from top and bottom html

def main():
    top_html = open ('templates/top.html').read()
    bottom_html = open ('templates/bottom.html').read()
    base_html = top_html + bottom_html
    open('templates/base.html', 'w+').write(base_html)
    print('Combined top and bottom html to create base.html')

    
# combines base html with index and creates output file in docs

for page in pages:
	top_html = open ('templates/top.html').read()
	bottom_html = open ('templates/bottom.html').read()
	content = open ('content/index.html').read()
	index_html = top_html + content + bottom_html
	open('docs/index.html', 'w+').write(index_html)
	content = open(page['filename']).read()
	combined = top_html + content + bottom_html
	open(page['output'],'w+').write(combined)
	




print ('Finished combining HTML templates with conent')


