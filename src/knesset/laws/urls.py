#encoding: UTF-8
from django.conf.urls.defaults import *
from django.utils.translation import ugettext
from django.views.generic.simple import redirect_to
from knesset.hashnav.views import ListDetailView
from knesset.hashnav import ListView
from models import *
from views import *

vote_view = VoteListView(queryset = Vote.objects.all(),paginate_by=20, extra_context={'votes':True,'title':ugettext('Votes')})
bill_list_view = BillListView(queryset=Bill.objects.all().filter(law__merged_into=None).order_by('-stage_date'), paginate_by=20,extra_context={'title':ugettext('Bills')})
bill_detail_view = BillDetailView(queryset=Bill.objects.all(), extra_context={'title':ugettext('Bills')})
vote_list_view = VoteListView(queryset = Vote.objects.all(),paginate_by=20, extra_context={'votes':True,'title':ugettext('Votes')})
vote_detail_view = VoteDetailView(queryset = Vote.objects.all(), extra_context={'votes':True})

lawsurlpatterns = patterns ('',
    url(r'^bill/$', bill_list_view, name='bill-list'),
    url(r'^bill/knesset-booklet/(?P<booklet_num>\d+)/$', redirect_to,
        {'url': '/bill/?booklet=%(booklet_num)s', 'premanent': True }),
    url(r'^bill/(?P<object_id>\d+)/$', bill_detail_view, name='bill-detail'),
    url(r'^vote/$', vote_list_view, name='vote-list'),
    url(r'^vote/(?P<object_id>\d+)/$', vote_detail_view, name='vote-detail'),
    url(r'^(?P<object_type>\w+)/(?P<object_id>\d+)/suggest-tag/$', suggest_tag),
    url(r'^(?P<object_type>\w+)/(?P<object_id>\d+)/tag-votes/(?P<tag_id>\d+)/(?P<vote>[+\-\d]+)/$', vote_on_tag),  
    url(r'^votes/tagged/(?P<tag>.*)/$', tagged, name='tagged-votes'),    
)
