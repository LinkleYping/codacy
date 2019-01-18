# coding:utf-8
import requests
import bs4
from docx import Document

# 把信息写到docx文件里
def writerror(content,numbers,save_name,demoname='demo.docx'):
    if content == '':
        return "nodata"
    doc = Document(demoname)  # get demo
    doc.styles['Normal'].font.size = 130000  # set font
    calc = 0
    for table in doc.tables:
        first_row = table.rows[0]
        first_row.cells[0].text = u"漏洞具体信息-"+str(calc+1)
        flag = 0
        col = 0
        for row in table.rows:
            if flag == 0:
                flag = flag + 1
                continue;
            row.cells[1].text = content[calc][col]
            col = col + 1
        calc = calc + 1
        if numbers <= calc:
            break
    doc.save(save_name)
    return "ok"


# 从网站上爬信息
def get_error_info(url=''):
    content = []
    response = requests.get(url)
    #print response.text
    soup = bs4.BeautifulSoup(response.text,'lxml')
    #print(soup.find_all('',{"class":"file-issue-container infinite-item"})) #{'class_': 'file-issue-container infinite-item'}
    error_file = soup.find_all('',{"class":"file-issue-container infinite-item"})
    if len(error_file)==0:
        return 'nodata'
    for i in range(len(error_file)):
        error_file_name = error_file[i].find_all('',{"class":"file-title"})
        name = error_file_name[0].get_text()  # Got the file name
        error_loc_set = error_file[i].find_all(attrs={"id":"issue_detail_container"})
        # print "Errors number:", len(error_loc_set)  # Got all errors in a same file
        for error_loc in error_loc_set:
            line = str(int(error_loc.find('a').get_text()))
            code = error_loc.find('',{"class":"code-line"}).get_text()
            content.append([name,line,code])
    print len(content)
    return content


raw_url_p1 = "https://app.codacy.com/app/pjinger/vee/issues?bid=9242582&cid=261884399&step="
step = 0
raw_url_p3 = "&filters=W3siaWQiOiJMYW5ndWFnZSIsInZhbHVlcyI6W251bGxdfSx7ImlkIjoiQ2F0ZWdvcnkiLCJ2YWx1ZXMiOltudWxsXX0seyJpZCI6IkxldmVsIiwidmFsdWVzIjpbbnVsbF19LHsiaWQiOiJQYXR0ZXJuIiwidmFsdWVzIjpbMTU5MF19LHsidmFsdWVzIjpbXX1d"
rval = "ok"
content = []
while rval != "nodata":
    raw_url = raw_url_p1+str(step)+raw_url_p3
    step += 20
    rval = get_error_info(raw_url)
    if rval == "nodata":
        print rval
        continue
    content.extend(rval)
# print content
print len(content)
#content = get_error_info('https://app.codacy.com/app/pjinger/vee/issues?bid=9242582&cid=261884399&step=200&filters=W3siaWQiOiJMYW5ndWFnZSIsInZhbHVlcyI6W251bGxdfSx7ImlkIjoiQ2F0ZWdvcnkiLCJ2YWx1ZXMiOltudWxsXX0seyJpZCI6IkxldmVsIiwidmFsdWVzIjpbbnVsbF19LHsiaWQiOiJQYXR0ZXJuIiwidmFsdWVzIjpbMjQwXX0seyJ2YWx1ZXMiOltdfV0=')
writerror(content,len(content),'test.docx')

