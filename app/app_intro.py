description = """
## Request Format
Following is the data format for the request body:
```
{
  "engine": "model_name",     # see Model List on next chapter
  "temperature": 0.7,         # the randomness of the model's output
  "max_tokens": 200,          # defines the maximum number of tokens
  "top_p": 0.95,              # represents the sampling probability.
  "top_k": 5,                 # specifies the number of top tokens to consider during sampling. 
  "roles": [                  # the chatlog format, contain role and content
    {
      "role": "user",         # must be "system", "user", "assistant"
      "content": "hi"         # conversation content
    }
  ],
  "frequency_penalty": 0,     # controls the penalty for using frequent tokens in the generated output. 
  "repetition_penalty": 1.03, # penalty for repeating the same or similar phrases in the generated output, encouraging diversity.
  "presence_penalty": 0,      # penalizes the presence of certain tokens in the output.
  "stop": "",                 # specifies a stopping criterion for generation, but in this case,
  "past_messages": 10,        # number of past messages considered for context in the conversation.
  "purpose": "dev"            # the purpose of this conversation
}
```

## Model List
```
1. gpt-35-turbo           | From the Azure Machine Learning OpenAI service.
2. gpt-35-turbo-16k       | The following parameters are not available :
3. gpt-35-turbo-instruct  |  1. repetition_penalty
4. gpt-4                  |  2. top_k
5. gpt-4-32k              | 

6. wulab                  | From the WuLab HuggingFace TGI api service.
                          | The following parameters are not available :
                          |  1. frequency_penalty
                          |  2. presence_penalty
                          |  3. stop
                          |  4. past_messages
```
"""