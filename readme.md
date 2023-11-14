# Missing Person in Hong Kong

## What did I use
1. Selenium, for retrieving page sources and navigating websites
2. Python, for making this thing to work

## Why did I build this project
One day I knew that my friend used the transportation fare opendata from data.gov.hk, so I surfed the website and found the opendata for missing person in Hong Kong. That is why I built this project. I used story as the medium since it is self destructing in 24 hours, so it will not spam in followers' pages, and I used facebook as the platform, because the graph api from META does not provide an api to post story, while this can only be achieved by using chrome driver. 
The whole basic flow of the automation is as follow: Update chrome driver -> Get opendata -> Create story content with opendata by opencv -> Post story with chrome driver -> Repeat until all stories are posted -> Delete all stories created in local folder with batch file
To automate the job flow, I also created a batch file and it will be triggered daily by windows task schedular  

## Some reminder
1. You may get banned by meta due to bot usage
2. Always respect the robots.txt
3. The chrome driver should always be up to date, this is done by driverautoupdate.py