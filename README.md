# kdd
kdd cup 2015
-----------
username , course_id 要映射成数字
enrollment_clean   保存clean后的数据，分别是 enrollment_id , username ,course_id
-----
log_train_clean，保存clean后的结果，分别是：enrollment_id，time，source，event，object
object，source，event都要映射成数字，time保存的是2000年1月1日0,0,0秒,的偏移值
source：server=1 , browser=2
event：
 - . problem - Working on course assignments.
 - . video - Watching course videos.
 - . access - Accessing other course objects except videos and assignments.
 - . wiki - Accessing the course wiki.
 - . discussion - Accessing the course forum.
 - . navigate - Navigating to other part of the course.
 - . page_close – Closing the web page.
