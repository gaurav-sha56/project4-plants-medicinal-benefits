class ai_response:

    def ai_processing(plant_name):
        from openai import OpenAI

        base_url = "https://api.aimlapi.com/v1"
        api_key = "a597bad60fa34ab28ee2462b1187b6af"
        system_prompt = "You are are herbalist and you are provided with a scientific name of a plants. Tell the all medicinal benefits of the plant and if the name is \"no best match found\" the simply say \"try different image\""
        user_prompt = plant_name

        api = OpenAI(api_key=api_key, base_url=base_url)


        
        completion = api.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
            max_tokens=256,
        )

        response = completion.choices[0].message.content

        print("User:", user_prompt)
        print("AI:", response)
