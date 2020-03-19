from django.shortcuts import render
import logging
# Create your views here.
from django.views.generic import ListView

from news.models import News
logger = logging.getLogger(__name__)

class NewsList(ListView):
    model = News
    template_name = 'news/news_list.html'

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        logger.debug(f"Request to NewsList from user: {self.request.user.id} with params: {self.request.GET}")
        logger.info("NewsList.get_queryset called")
        try:
            news = News.objects.select_related("region").all()
        except Exception as exc:
            logger.error(str(exc))
            raise
        if not news:
            logger.warning("News list is empty")
        import q; q(news); q(news[0])
        return news