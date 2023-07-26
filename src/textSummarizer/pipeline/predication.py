from src.textSummarizer.config.configuration import ConfigurationManager 
from transformers import AutoTokenizer
from transformers import pipeline


class PredicationPipeline:
    def __init__(self):
        self.config=ConfigurationManager().get_model_evaluation_config()


    def predict(self,text):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs={"length_penalty":0.8,"num_beans":8,"max_length":128}

        pipe=pipeline("summarization",model=self.config.model,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output=pipe(text,**gen_kwargs)[0]['summary_text']
        print("\nModel Summary:")
        print(output)


        return output