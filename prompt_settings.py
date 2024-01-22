from lamini import Lamini

llm = Lamini(model_name="mistralai/Mistral-7B-Instruct-v0.2")
print(llm.generate("You are a pirate. Do you like parrots?"))
print(llm.generate("<s>[INST]You are a pirate. Do you like parrots?[/INST]"))

llm_compare = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
print(llm_compare.generate("You are a pirate. Do you like parrots?"))
print(llm_compare.generate("<s>[INST] <<SYS>>\nYou are a pirate.\n<</SYS>>\nDo you like parrots? [/INST]"))