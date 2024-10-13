
# FourksUp (Team #4)
Opportunity Hack Fall 2024

## Hackers
- Seth Rojas
- Quinlan Harris 
- Abram Pierce 
- Joshua Bunnell 

## About San Gabriel Valley Habitat for Humanity
Website: (https://sgvhabitat.org/)

Mission statement: Seeking to put God's love into action, Habitat for Humanity brings people together to build homes, communities, and hope. We build strength and self-reliance through shelter.

## Project Introduction
San Gabriel Valley Habitat for Humanity is a homeless housing nonprofit organization that relies on efficient survey automation and intutive data analysis to improve its outreach. Their current system lacks a complete, customizable, user friendly hub that quantifies impact, displays critical feedback, and merges existing data. Utilizing various Google services, we created a web application that will streamline SGVH's data collection and analysis.

## Technologies Used
| Technologies   | Usage |
| -------- | ------- |
| Microsoft Azure AI, Python| REST API, Computer Vision  |
| Looker Studio | Data Visualization |
| Google Forms    | User Surveys  |
| Google Sheets   | Database  |
| Google Sites    | Dashboard |


## Tech Stack
- Frontend: Looker Studio, Google Sites, Google Forms
- Backend: Google Sheets, Google Sites
- Database: Google Sheets
- APIs: Microsoft Azure API
<!-- Add/modify as needed -->

## Getting Started

```bash
# Example commands
git clone [your-repo-link]
cd [your-repo-name]
npm install
npm start
```

## Challenges
1. Our largest challenge was pivoting from a coding a full-stack web applicaiton to utilizing Google's integrated services. After talks with our community partner and project mentors, we targeted their needs by developing an accesssible, customizable, and dynamic application that is simple to maintain and understand. This also allowed us to focus on difficult background tools and maximize Google's free services.
2. SGVH has an overflow of existing survey paper and excel files that are uncentralized and discombobulated. To combat this, we developed a python script that utilizes computer vision and a LLM to read existing paper surveys and integrate them into a combined database. The two main issues we ran into was identifying circled multiple-choice questions on the survey and retrieving consistent data from our LLM
3. Due to the nature of free-response forms, it was difficult to consolidate consistent data between our network of platforms. Before creating visuals on Looker Studio, we combined existing paper surveys and new online surveys into one main database while sectioning off the different survey responses. However, between reading multiple data inputs and the limits of the Google services, maintaining multiple databases which funneled into our visual dataset was a challenge.

## Future Enhancements and Plans (NOT DONEEE)
1. Fully developing a scan
2. Scraping Google Sites
3. Ideas for tools

4. 
## Your next steps
1. ✅ Add everyone on your team to your GitHub repo like [this video posted in our Slack channel](https://opportunity-hack.slack.com/archives/C1Q6YHXQU/p1605657678139600)
2. ✅ Create your DevPost project [like this video](https://youtu.be/vCa7QFFthfU?si=bzMQ91d8j3ZkOD03)
3. ✅ Use the [2024 DevPost](https://opportunity-hack-2024-arizona.devpost.com) to submit your project
4. ✅ Your DevPost final submission demo video should be 4 minutes or less
5. ✅ Review the judging criteria on DevPost

# What should your final Readme look like?
Your readme should be a one-stop-shop for the judges to understand your project. It should include:
- Team name
- Team members
- Slack channel
- Problem statement
- Tech stack
- Link to your DevPost project
- Link to your final demo video
- Any other information you think is important

You'll use this repo as your resume in the future, so make it shine! 🌟

Examples of stellar readmes:
- ✨ [2019 Team 3](https://github.com/2019-Arizona-Opportunity-Hack/Team-3)
- ✨ [2019 Team 6](https://github.com/2019-Arizona-Opportunity-Hack/Team-6)
- ✨ [2020 Team 2](https://github.com/2020-opportunity-hack/Team-02)
- ✨ [2020 Team 4](https://github.com/2020-opportunity-hack/Team-04)
- ✨ [2020 Team 8](https://github.com/2020-opportunity-hack/Team-08)
- ✨ [2020 Team 12](https://github.com/2020-opportunity-hack/Team-12)

## Quick Links
- [Hackathon Details](https://www.ohack.dev/hack/2024_fall)
- [Team Slack Channel](https://opportunity-hack.slack.com/app_redirect?channel=fourks-up)
- [Nonprofit Partner](https://ohack.dev/nonprofit/FUSQQIaQF70ocwcatH9T)
- [Problem Statement](https://ohack.dev/project/pcDVx7FAHQvZSViHbgS7)

