# Ralph_Lauren_task

> This is a test case for a job interview.
> The task can be found in task.pdf file in the repository.

- In order to execute the scrapy spider, do:
~~~
~/.../Ralph_Lauren/spiders | master
scrapy crawl ralph_lauren
~~~
- In order to use my img_convert and img_process go to the according dirs and do:
~~~
python3 main.py
~~~

## Report
### Task 1
- It was not my first time both crawling and scraping, though I never aimed for the images. I have coded a ralph_lauren.py spider, that crawls every sweatshirt webpage and calls a parse_cloth() method on every one of those. This method yields items to download into my pipeline. I used CSS selectors to navigate around. The hardest part was the security of Ralph Lauren and their website. I had to configure request headers, cookies and delay to evade bans. Image pipeline also required some time to get used to, but nothing too entertaining. 

### Task 2
- Regarding image processing given the mask and the images themselves — I haven't had much issues with any of the quests. I was able to only use the mask given by your pretrained model and it's inverse to preprocess any scraped images using bitwise_and() and add() methods. It also occured to me that a little bit of noise cleaning on the masks would be appropriate to make the result look neat.
> You can change name variable in main.py and provide name.jpg and name_mask.jpg to img_process/name to use my tool with any other image.

> It was the first time for me encountering much of the issues I had to deal with, and while it was really frustrating at first, at the end of the day I found all of the problems very interesting to solve. Thank you!
