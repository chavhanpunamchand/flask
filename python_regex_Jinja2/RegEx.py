'''
pages -->
email           -->  def validate_email(val):
                            pass --> logic to check valid email or not
mobile              def validate_indian_mobiles(val) : --> check
usnumbers -->
pincode
address
names
landline

us-numbers
website
urls
pancard
aadharcard
only numbers
only special chars
salary

? -- zero or one -->
'''
value ='''
Sample letter to editor Akshay 98368783784 requesting for an article Ananta submission 69838783784 www.careerride.com 
› view › sample-letter-to-editor-re abc@gmail.com 9838783784
For your 7778783784 reference I have 4838783784 attached the copy of the article. If there avddc@gmail.com is 9838783784 Yogesh anything 
in it you Sumit find unsuitable, Amit please let me know. I will be glad to 2 8387853784 look into it. 
Kindly let me know the process through Jaydeep which I can get xx@yahoo.com it published.
'''
import re

email_pattern = "[\w]+@gmail[.]{1}[\w]{2,}"

ans = re.findall(email_pattern,value)
print(ans)

import sys
sys.exit(0)
