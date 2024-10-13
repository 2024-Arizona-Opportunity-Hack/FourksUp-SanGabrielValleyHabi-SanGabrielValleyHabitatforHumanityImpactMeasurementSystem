
# FourksUp (Team #4)
- Opportunity Hack: [  Fall 2024](https://www.ohack.dev/hack/2024_fall)
- Non Profit Partner: [San Gabriel Valley Habitat for Humanity](https://sgvhabitat.org/)
- Slack Channel: [     #FourksUp](https://opportunity-hack.slack.com/app_redirect?channel=fourks-up)

## Hackers
- Seth Rojas
- Quinlan Harris 
- Abram Pierce 
- Joshua Bunnell 

## Project Introduction 
[San Gabriel Valley Habitat for Humanity](https://sgvhabitat.org/)  is a low-income housing and community revitalization nonprofit organization that relies on efficient survey automation and intutive data analysis to improve its outreach. Their current system lacks a complete, customizable, user friendly hub that quantifies impact, displays critical feedback, and merges existing data. Utilizing various Google services, we created a web application that will streamline SGVH's future data collection and analysis and allow them to better track metrics and expand their services.

## Project Links
- [Website](https://sites.google.com/view/sgvh-ohack/home?authuser=3)
- [Colab Notebook AI Tool Demo](https://github.com/2024-Arizona-Opportunity-Hack/FourksUp-SanGabrielValleyHabi-SanGabrielValleyHabitatforHumanityImpactMeasurementSystem/blob/main/Extract_Image_Data.ipynb)
- [Slideshow Demo](https://docs.google.com/presentation/d/1F9AuPJ5EkkQhXMyPwh69T-XTsrCUzgFj2Kidv3TpEaM/edit?usp=sharing)
- [Project Demo]()
- [DevPost]()


## Technologies Used
| Technologies   | Usage |
| -------- | ------- |
| Microsoft Azure AI, Python| API, CV Text Extractor  |
| Looker Studio | Data Visualization |
| Google Forms    | User Surveys  |
| Google Sheets   | Database  |
| Google Sites    | Dashboard |

## Service Integration and Architecture
By utilizing Google's robust technologies, we created a secure, integrated system that is scalable and intuitive for SGVH

![Design Flowchart](flowchartohacks.pdf)
## Tech Stack
- Frontend: Looker Studio, Google Sites, Google Forms
- Backend: Google Sites
- Database: Google Sheets
- APIs: Microsoft Azure AI
<!-- Add/modify as needed -->

## Getting Started
1. Website
   1. Click on the website link at the top
2. Scan and upload feature
   1. See Colab Notebook link at the top for a step by step tutorial

## Challenges
1. Our biggest challenge was pivoting from a coding a full-stack web application to utilizing Google's integrated services. After talks with our community partner and project mentors, we targeted their needs by developing an accessible, customizable, and dynamic application that is simple to maintain and understand. This also allowed us to focus on difficult background tools and maximize Google's free services.
2. SGVH has an overflow of existing survey papers and excel files that are unorganized and discombobulated. To combat this, we developed a python script that utilizes computer vision and a LLM to read existing paper surveys and integrate them into a combined database. The two main issues we ran into was identifying circled multiple-choice questions on the survey and retrieving consistent data from our LLM.
3. Due to the nature of free-response forms, it was difficult to consolidate consistent data between our network of platforms. Before creating visuals on Looker Studio, we combined existing paper surveys and new online surveys into one main database while sectioning off the different survey responses. However, between reading multiple data inputs and the limits of the Google services, maintaining multiple databases which funneled into our visual dataset was a challenge.

## Future Enhancements and Plans
1. Our current AI image-text extractor consistently reads the free response questions which is important time-saving mechanism for a busy nonprofit organization (~15-30sec/response & ~7-10 questions/form). The other questions 
2. Pivoting to Google Sites allowed us to focus on designing a well-documented, robust, and maintable dashboard for our customer. We look to expand this platform by creating a coded web application that still maintains the qualities and features of our current hub, but would offer improved site customizability and scalibility. However, creating a new web application would be time-consuming and is less maintainble and secure than utilizing the safe, integrated systems of Google.

## Meeting San Gabriel Valley Habitat for Humanity's Needs
1. Centralized, easy-to-use data dashboard
   1. Integrated Looker Studio visuals on website
   2. Robust data filtering
2. Online survey implementation integrated with dashboard
   1. Completed online Google Forms structured from given paper surveys
   2. Interconnected Architecture: Google Forms (survey) -> Google Sheets (database) -> Looker Studio (data visualization) -> Google Sites (website/dashboard)
3. Data upload functionality and consolidated, simple database
   1. AI PDF text extractor that can automatically inputs information into Google Form, saving crucial time.
   2. Robust database that maintains a master sheet database and separate sheets for each survey
   3. Utilizing the easy-to-use Google Sheets platform SGVH eliminates a  user learning curve; allowing to SGVH to focus on what they do best.
  
## Your next steps
1. ✅ Add everyone on your team to your GitHub repo like [this video posted in our Slack channel](https://opportunity-hack.slack.com/archives/C1Q6YHXQU/p1605657678139600)
2. ✅ Create your DevPost project [like this video](https://youtu.be/vCa7QFFthfU?si=bzMQ91d8j3ZkOD03)
3. ✅ Use the [2024 DevPost](https://opportunity-hack-2024-arizona.devpost.com) to submit your project
4. ✅ Your DevPost final submission demo video should be 4 minutes or less
5. ✅ Review the judging criteria on DevPost

Examples of stellar readmes:
- ✨ [2019 Team 3](https://github.com/2019-Arizona-Opportunity-Hack/Team-3)
- ✨ [2019 Team 6](https://github.com/2019-Arizona-Opportunity-Hack/Team-6)
- ✨ [2020 Team 2](https://github.com/2020-opportunity-hack/Team-02)
- ✨ [2020 Team 4](https://github.com/2020-opportunity-hack/Team-04)
- ✨ [2020 Team 8](https://github.com/2020-opportunity-hack/Team-08)
- ✨ [2020 Team 12](https://github.com/2020-opportunity-hack/Team-12)

