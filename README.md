## Create Open AI API Key and Setup Billing Account

the steps below will walk you through setting up a billing account and open ai api token key to be used in [main.py](https://github.com/coleman-zachery/open_ai_api/blob/main/main.py) in order to use the open ai paid service to query chat-gpt.

---

1.   login at https://platform.openai.com/api-keys

---

2a.   to create an api key, click on "API keys", then "+ Create new secret key", give it a name, and then click "Create secret key"

![1](https://github.com/coleman-zachery/open_ai_api/assets/42438576/59fadb6d-639a-4d27-9fa6-44e0666020f0)

---

2b.   copy the generated string for your api key into your .py script:

![2](https://github.com/coleman-zachery/open_ai_api/assets/42438576/8880aee2-c692-43a5-bad1-6c1d17d26487)

``` python
OPENAI_API_KEY='aa-aAa0aAa0aAa0aAa0aAa0aAa'
```

---

2c.   click "Done"

![4](https://github.com/coleman-zachery/open_ai_api/assets/42438576/8a57c51c-d38d-40f3-8ad0-a556744b2d0c)

---

3a.   when you're ready to fund your account, click "Settings" > "Billing" > "Payment Methods" > "Add Payment Method"

![image](https://github.com/coleman-zachery/open_ai_api/assets/42438576/b41a3954-535c-4789-99b1-63a852f6cc85)

---

3b.   you can monitor spending by clicking on "Usage" (as well as set auto-billing to fill the account if it drops too low, and limits to stop funding the service if it spends too much in a month)

![5](https://github.com/coleman-zachery/open_ai_api/assets/42438576/222f6c3c-31f0-474d-9db9-0bd1cdec9c11)

---

3c.   lastly, you can check out the api pricing at https://openai.com/pricing

![4](https://github.com/coleman-zachery/open_ai_api/assets/42438576/049a4fe9-1806-4f06-bbea-04dd2b6d919e)
