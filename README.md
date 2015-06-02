# kdd
kdd cup 2015
1、
  username , course_id 要映射成数字
  enrollment_clean   保存clean后的数据，分别是 enrollment_id , username ,course_id
2、
  log_train_clean，保存clean后的结果，分别是：enrollment_id，time，source，event，object
  object，source，event都要映射成数字，time保存的是2000年1月1日0,0,0秒,的偏移值
  source：server=1 , browser=2
  event：
    1. problem - Working on course assignments.
    2. video - Watching course videos.
    3. access - Accessing other course objects except videos and assignments.
    4. wiki - Accessing the course wiki.
    5. discussion - Accessing the course forum.
    6. navigate - Navigating to other part of the course.
    7. page_close – Closing the web page.
