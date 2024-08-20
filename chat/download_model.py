from modelscope import snapshot_download, AutoTokenizer, AutoModelForCausalLM
import torch
model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm2_5-7b-chat',cache_dir ="../")
# tokenizer = AutoTokenizer.from_pretrained(model_dir, device_map="auto", trust_remote_code=True,torch_dtype=torch.float16)
# model = AutoModelForCausalLM.from_pretrained(model_dir,device_map="auto",  trust_remote_code=True,torch_dtype=torch.float16)
# model = model.eval()
# response, history = model.chat(tokenizer, "hello", history=[])
# print(response)
# response, history = model.chat(tokenizer, "please provide three suggestions about time management", history=history)
# print(response)