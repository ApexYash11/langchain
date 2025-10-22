from typing import TypedDict , Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

#schema 

class review(BaseModel):

  key_themes: list[str] = Field(description="A list of key themes mentioned in the review in a list")

  summary: str = Field(description="A brief summary of the product review")
  sentiment: str = Field(description="The sentiment of the review, either positive, negative, or neutral")
  key_themes: list[str] = Field(description="A list of key themes mentioned in the review in a list")
  pros: list[str] = Field(description="A list of positive aspects of the product mentioned in the review in a list")
  cons: list[str] = Field(description="A list of negative aspects of the product mentioned in the review in a list")
  name: str = Field(description="The name of the product being reviewed")

structed_model=model.with_structured_output(review)

result=model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Review by Yash
""")

print(result.name)

