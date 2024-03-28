## Setup Billing Account for Open AI

the steps below will walk you through setting up a billing account and open ai api token key to be used in [main.py](https://github.com/coleman-zachery/open_ai_api/blob/main/main.py) in order to use the open ai paid service to query chat-gpt.

---


---



go to https://platform.openai.com/api-keys and login, click on  "+ Create new secret key", give it a name, and click "Create secret key"

copy the string into your .py script:

OPENAI_API_KEY='aa-aAa0aAa0aAa0aAa0aAa0aAa'

click "Done"

when you're ready to fund your account, click "Settings", "Billing", "Payment Methods", "Add Payment Method"

you can check out the api pricing at https://openai.com/pricing

lastly, you can monitor spending by clicking on "Usage" as well as set auto-billing to fill the account if it drops too low, and limits to stop funding the service if it spends too much in a month
