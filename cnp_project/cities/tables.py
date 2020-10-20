import itertools
import django_tables2 as tables


class CityTable(tables.Table):
    """
    A Table to represent the City model with according columns.
    Automatic row numbering starting at 1.
    """

    row_number = tables.Column(verbose_name='#', empty_values=(),
                               orderable=False)
    name = tables.Column(verbose_name='Город / Агломерация')
    country = tables.Column(verbose_name='Страна', orderable=False)
    population = tables.Column(verbose_name='Население агломерации (т.ч.)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count(1)

    def render_row_number(self):
        return f'{next(self.counter)}.'

    class Meta:
        template_name = 'django_tables2/bootstrap4.html'
