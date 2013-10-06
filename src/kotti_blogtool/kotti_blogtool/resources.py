from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode

from kotti_blogtool import _


class Blog(Content):
    """My content type"""

    id = Column(
        Integer(),
        ForeignKey('contents.id'),
        primary_key=True
    )

    # Add additional columns here
    example_attribute = Column(
        Unicode()
    )

    type_info = Content.type_info.copy(
        name=u'Blog',
        title=_(u'Blog Folder'),
        add_view=u'add_blog',
        addable_to=['Document', ],
        selectable_default_views=[
            ('alternative-view', _(u"Alternative View")),
        ],
    )

    def __init__(self, example_attribute=u"", **kwargs):

        super(Blog, self).__init__(**kwargs)

        self.example_attribute = example_attribute
