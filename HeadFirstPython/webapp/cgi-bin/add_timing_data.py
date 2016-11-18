import  cgi   #导入cgi库
import  os
import time
import  sys
import  yate

print(yate.start_response('text/plain'))
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
cur_time = time.asctime(time.localtime())

print(host + "," + addr + "," + cur_time +"," + method + ":",end = '',file = sys.stderr)

form = cgi.FieldStorage()       #获取所有的表单数据，并存放到一个字典里
for each_form_item in form.keys():
    print(each_form_item + '->'+form[each_form_item].value,end='',file=sys.stderr)
print(file=sys.stderr)
print('OK.I　got here!')

