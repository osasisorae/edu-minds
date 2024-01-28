
## Educational Assistance Bot for Telegram and WhatsApp
### Overview
This open-source project is an Educational Assistance Bot designed to provide accessible and personalized learning support for individuals in third-world countries with limited digital access. The bot leverages popular messaging platforms such as Telegram and WhatsApp to deliver educational content, interactive lessons, and guidance across various user profiles, including children, students, graduates, working-class individuals, and entrepreneurs.

### Features
- User Registration and Learning Profiles: Users can register and create learning profiles specifying their goals, preferred learning styles, and subjects of interest.

- Content Delivery: Educational content is delivered through text, images, and short videos, curated based on users' learning profiles.

- Adaptive Learning Paths: The bot tailors learning paths based on user progress, adjusting difficulty levels to proficiency.

- Real-time Feedback: Immediate feedback on quizzes and assessments with the ability to ask questions through natural language interactions.

- Skill Development and Career Guidance: Modules for skill development, career guidance, and entrepreneurship support are available.

- Community Engagement: A community space within the messaging platforms allows users to connect, share experiences, and support each other.

- Offline Mode: Users can download content for offline access, facilitating learning even in areas with intermittent internet connectivity.

### How to Use
To start using the Educational Assistance Bot, simply register with the bot on Telegram or WhatsApp. Follow the prompts to create your learning profile, and begin your personalized learning journey.

### How to Deploy
To run both the MindsDB server and your bot script in the background on a Linux server, you can use the nohup command along with & to start the processes in the background. Additionally, you may want to use & to run commands in the background and disown to detach the process from the terminal session. Here's how you can do it:

- Run the MindsDB Server in the Background:

First, navigate to the directory where your Python virtual environment is located.
Activate the virtual environment.
Then, use the nohup command to run MindsDB in the background.
```
python3 -m venv .venv
cd /home/username/edu-minds/.venv
source bin/activate
nohup python -m mindsdb > mindsdb.log 2>&1 &
disown
```
- Run the Bot Script in the Background:

Similarly, navigate to the directory where your bot script is located.
Ensure the same virtual environment is activated (if needed for the bot).
Use nohup to run your bot script in the background.
```
cd /home/username/edu-minds
nohup /home/username/edu-minds/.venv/bin/python bot.py > bot.log 2>&1 &
disown
```

The > mindsdb.log 2>&1 & and > bot.log 2>&1 & parts of the commands redirect both the standard output and standard error to log files (mindsdb.log and bot.log, respectively) for later review. The & at the end of the command puts the process in the background, and disown detaches it from the terminal, so it keeps running even if you close the terminal.

Remember to check these log files for any output or errors from your processes. You can view the contents of these logs at any time with commands like cat mindsdb.log or tail -f mindsdb.log for real-time updates.

**For a full Tutorial check out the [blog](https://oblvck.hashnode.dev/creating-personalized-learning-paths-with-a-chatbot-using-mindsdb-and-telebot) on [Hashnode](http://www.hashnode.com)**

### Contribution Guidelines
We welcome contributions from the community to enhance and expand the capabilities of the Educational Assistance Bot. Please refer to our contribution guidelines for details on how to get involved.

### Privacy and Security
Our project prioritizes user privacy and data security. Learn more about our approach in our privacy policy.

### Support
For any issues, questions, or suggestions, feel free to open an issue on GitHub.

Thank you for contributing to accessible education for all!