from lamini import Lamini

# 
# Mistral 7B
# 

llm = Lamini(model_name="mistralai/Mistral-7B-Instruct-v0.2")

prompts = [
    "Given the fact that I'm drinking green juice, am I healthy?",
    "Respond kindly to the child: i really hate zucchini. why should i eat it?",
    "vscode - how to find code that has been checked in a long time ago, e.g. more than 6 months ago",
    """what does an example jsonl file look like that is loaded with this function? def load_examples(self):
        filename = self.saved_examples_path
        if not os.path.exists(filename):
            return {}

        # load the examples from the jsonl file using the jsonlines library
        with jsonlines.open(filename) as reader:
            examples = {}
            for row in reader:
                class_name = row["class_name"]
                example = row["examples"]
                self.add_class(class_name)
                examples[class_name] = example

        return examples""",
]

for prompt in prompts:
    print(f"=============Prompt: {prompt}=============")
    print(llm.generate(prompt))
    print(f"=============Prompt: <s>[INST] {prompt} [/INST]=============")
    print(llm.generate(f"<s>[INST] {prompt} [/INST]"))
    

# 
# Llama 2
# 
    
llm_compare = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")

prompts = [
    {
        "system": "You are a healths food nut.",
        "user": "I'm drinking green juice",
    },
]

for prompt in prompts:
    concat_prompt = f"{prompt['system']} {prompt['user']}"
    hydrated_prompt = f"<s>[INST] <<SYS>>\n{prompt['system']}\n<</SYS>>\n{prompt['user']} [/INST]"
    print(f"=============Prompt: {concat_prompt}=============")
    print(llm_compare.generate(concat_prompt))
    print(f"=============Prompt: {hydrated_prompt}=============")
    print(llm_compare.generate(hydrated_prompt))

