# vid-summarize
Downloads videos and produces a text summary or keywords

## initial notes
- input url or filename of file containing urls
- use ytdl-org to download a video
- generate text from audio (google api?)
- produce summary and/or keywords (research methods)

## done so far
- did langchain crash course

## todo
- get transcript for given URL using https://pypi.org/project/youtube-transcript-api/ 
- pipe transcript into spacy for statistical frequency analysis for keywords https://www.activestate.com/blog/how-to-do-text-summarization-with-python/
- pipe transcript into openai (directly or with langchain) for short summary 
- convenient output
- allow batch processing for entire playlist or entire channel
