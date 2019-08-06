# GitHub Contributions Hack

## Allows you to write arbitrary messages in your GitHub contributions area

![screenshot](screenshot.png "Screenshot of program result")

## Usage Instructions

In order for git commits to be counted towards your contributions, they cannot be from a fork, so please follow these instructions to make it work right:

1. Create a new repository
2. Clone your new repository
3. `git clone https://github.com/jeffslofish/contributions-hack.git`
4. `cp contributions-hack/* your-new-repo-name`
5. `cd your-new-repo-name`
6. `python commit.py message yyyy mm dd` (Replace message with your own word. Replace yyyy mm dd with your own year, month, and day for the first date of your first letter. Should be a Sunday. Also, your message will appear more clearly if you choose a date that has no contributions for a period of time after it, depending on how long your message is.)
7. `git push` 
8. Go to your user profile and see your message in the contributions area! (It usually only takes a few seconds for the commit contributions to appear after doing a push.)

## Notes
- Currently the only letters a-z are supported, and the message must be one word. Feel free to add more and submit a pull request!
