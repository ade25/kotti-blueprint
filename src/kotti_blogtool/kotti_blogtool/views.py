# -*- coding: utf-8 -*-

from colander import SchemaNode
from colander import String
from kotti.views.edit.content import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_blogtool import _
from kotti_blogtool.resources import Blog
from kotti_blogtool.fanstatic import kotti_blogtool


class BlogSchema(ContentSchema):
    """Schema for add / edit forms of Blog"""

    example_attribute = SchemaNode(
        String(),
        title=_(u'Example Attribute'),
        missing=u"",
    )


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
