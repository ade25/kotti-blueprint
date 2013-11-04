# -*- coding: utf-8 -*-
import datetime
from dateutil.tz import tzutc

from colander import deferred
from colander import SchemaNode
from colander import String
from colander import Range
from colander import DateTime
from colander import iso8601
from deform.widget import DateTimeInputWidget
from kotti.views.edit.content import ContentSchema
from kotti.views.edit import DocumentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_blogtool import _
from kotti_blogtool.resources import Blog
from kotti_blogtool.fanstatic import kotti_blogtool


@deferred
def deferred_date_missing(node, kw):
    value = datetime.datetime.now()
    return datetime.datetime(
        value.year, value.month, value.day, value.hour,
        value.minute, value.second, value.microsecond, tzinfo=tzutc())


class BlogSchema(DocumentSchema):
    """ Blog schema derived from basic documents """
    pass


class BlogEntrySchema(DocumentSchema):
    date = SchemaNode(
        DateTime(),
        title=_(u'Date'),
        description=_(u'Choose date of the blog entry. '
                      u'If you leave this empty the creation date is used.'),
        validator=Range(
            min=datetime.datetime(
                2012, 1, 1, 0, 0, tzinfo=iso8601.Utc()),
            min_err=_('${val} is earlier than earliest datetime ${min}')),
        widget=DateTimeInputWidget(),
        missing=deferred_date_missing,
    )


class BlogAddForm(AddFormView):
    schema_factory = BlogSchema
    add = Blog
    item_type = _(u"Blog")


class BlogEditForm(EditFormView):
    schema_factory = BlogSchema


class BlogEntryAddForm(AddFormView):
    schema_factory = BlogEntrySchema
    add = BlogEntry
    item_type = _(u"Blog Entry")


class BlogEntryEditForm(EditFormView):
    schema_factory = BlogEntrySchema


@view_config(name=Blog.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt')
class BlogAddForm(AddFormView):

    schema_factory = BlogSchema
    add = Blog
    item_type = _(u"Blog")


@view_config(name='edit',
             context=Blog,
             permission='edit',
             renderer='kotti:templates/edit/node.pt')
class BlogEditForm(EditFormView):

    schema_factory = BlogSchema


@view_defaults(context=Blog, permission='view')
class BlogView(object):
    """View(s) for Blog"""

    def __init__(self, context, request):

        self.context = context
        self.request = request

    @view_config(name='view',
                 renderer='kotti_blogtool:templates/blog.pt')
    def view(self):

        kotti_blogtool.need()

        return {}

    @view_config(name='alternative-view',
                 renderer='kotti_blogtool:templates/blog-alternative.pt')
    def alternative_view(self):

        return {}
