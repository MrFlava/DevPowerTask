import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
WIKI_URL = (
    "https://en.wikipedia.org/w/index.php?"
    "title=List_of_countries_by_population_(United_Nations)"
    "&oldid=1215058959"
)
