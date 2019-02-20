
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


# function used to combine html

def replace(template, title, file_name):
    index_content = open(file_name).read()
    finished_index_page = template.replace("{{content}}", index_content)
    finished_index_page = finished_index_page.replace("{{title}}", title)
    return finished_index_page
    
def create_page(template, page):
    file_name = page['filename']
    output = page['output']
    title = page['title']
    
    
    page_html = replace(template, title, file_name)
    open(output, "w+").write(page_html)
    
def main():
    template = open("templates/base.html").read()
    for page in pages:
        create_page(template, page)
    
if __name__ == "__main__":
    main()



	




print ('Finished combining HTML templates with conent')


