# Ralph_Lauren_task

> This is a test case for a job interview.
> The task can be found in task.pdf file in the repository.

- In order to execute the scrapy spider, go to spiders/ dir and type in:
	scrapy crawl ralph_lauren

## Report
### Task 1
- The hardest part was security of Ralph Lauren and their website. First of all, there are no robots.txt or any mention about scraping in Terms of Use whatsoever, so I was left to collect info about what anti-bot protection Ralph Lauren uses bits by bits. Fixing those issues has taken some time, but eventually I got them request headers, set up the manual randomized delay between requests, auto-throttling, disabled cookies and set up a cookie string from my own web browser (replaced in the final commit due to security reasons), which allowed to finally get rid of those 403 bans. Image pipeline also required some time to get used to, but nothing too entertaining.
- It was the first time for me encountering such issues with bot-protection, and while it was really frustrating at first, at the end of the day I found all of the problems very interesting to solve.
