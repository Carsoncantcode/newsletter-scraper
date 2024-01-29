from fastapi import APIRouter, Query
from typing import List
from .logic import scrapeSingleNewsletter, scrapeNewsletterPosts
from schemas.models import *





router = APIRouter()

@router.get('/scrape_article/{url:path}', response_model=Article)
async def scrapeSingle(url: str):
    article_text = scrapeSingleNewsletter(url)
    return {"url": url, "text": article_text}

@router.get('/scrape_all_articles/{url:path}', response_model=List[Article])
async def scrapeAll(url: str):
    articles_data = scrapeNewsletterPosts(url)
    return articles_data

