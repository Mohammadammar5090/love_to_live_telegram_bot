# love_to_live_telegram_bot
A special bot for the "Love to Live" initiative


This program, known as the bot, has been meticulously crafted for the "love to live (LTL)" initiative, an educational endeavor aimed at children battling cancer. It operates as follows:

1. Volunteers are prompted to complete a form every week through the bot, which engages them with thoughtful inquiries.
2. The bot uploads the responses to an Excel file on Google Drive, utilizing the API and the gspread library.
3. It diligently creates backups of the data, ensuring its security and preservation.
4. By appending a concise keyword beside the volunteer's name, the bot swiftly identifies those who have yet to fill out the form.
5. Each volunteer possesses a unique identifier, their phone number, which sets them apart.
6. Moreover, the bot facilitates volunteers in submitting proof of their session contributions. For instance, upon receiving an image, the bot efficiently converts and shares it in a Telegram group named "LTL_data," which boasts ample storage capacity.

7. Additionally, I have incorporated a version of ChatGPT to streamline volunteer tasks, making it effortless for them to retrieve questions or acquire knowledge.

To enhance the initiative supervisors' experience, numerous features have been implemented. These include reminders for volunteers to complete the form, the ability to send group messages and have them persist in the conversation, and the ability to identify individuals who fall short in their obligations, among other valuable capabilities.

Telegram was selected as the preferred application due to its user-friendly interface and an array of impressive features. Notably, it permits the transmission of videos up to 2 gigabytes, offers customizable keyboards that can be effortlessly modified to suit the bot's purpose, and encompasses various other noteworthy functionalities.

I used the replit.com ,flask code and UptimeRobot.com instead of a paid server
