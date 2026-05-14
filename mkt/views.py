from mkt.models import Ad
from mkt.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "myarts/article_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad

class AdCreateView(OwnerCreateView):
    model = Ad
    # List Article model fields to copy to the Article form / template
    fields = ['title', 'text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text']


class AdDeleteView(OwnerDeleteView):
    model = Ad
