from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_community.llms.tongyi import Tongyi
from dotenv import load_dotenv

load_dotenv()
#示例的模板
example_prompt = PromptTemplate.from_template("单词:{word}.反义词:{antonym}")

#示例数据,要求是list内部套字典
example_data = [
    {"word":"大","antonym":"小"},
    {"word":"高","antonym":"矮"},
    ]

few_shot_template =  FewShotPromptTemplate(
    example_prompt = example_prompt,        # 示例数据模板
    examples = example_data,                # 示例数据(用来注入动态数据)
    prefix = "输入一个单词，输出它的反义词。",          # 前缀提示词
    suffix = "基于示例，请输出{input_word}的反义词:",  # 中缀提示词
    input_variables = ["input_word"],       # 声明前端或后端中所需要的输入变量(必须)
)

prompt_text = few_shot_template.invoke(input={"input_word":"前"}).to_string()
print(prompt_text)

model = Tongyi(model="qwen-max")
res = model.invoke(input=prompt_text)
print(res)