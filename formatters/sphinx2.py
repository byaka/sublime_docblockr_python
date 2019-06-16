"""Another format for Sphinx."""
from .base import Base


class Sphinx2Formatter(Base):
    """Documentation Formatter Class."""

    name = 'sphinx2'

    def decorators(self, attributes):
        """Create snippet string for a list of decorators."""
        return ''

    def extends(self, attributes):
        """Create snippet string for a list of extended objects."""
        return ''

    def arguments(self, attributes):
        """Create snippet string for a list of arguments."""
        section = ''
        template = ':param {name} {type}: {description}.\n'

        for attr in attributes['arguments']:
            section += template.format(
                name=self._generate_field('name', attr['name']),
                description=self._generate_field('description'),
                type=self._generate_field('type', attr['type']),
            )

        section += self.keyword_arguments(attributes['keyword_arguments'])

        return section

    def keyword_arguments(self, attributes):
        """Create snippet string for a list of keyword arguments."""
        section = ''
        template = ':param {name} {type}: {description} (defaults to {default}).\n'

        for attr in attributes:
            section += template.format(
                name=self._generate_field('name', attr['name']),
                description=self._generate_field('description'),
                default=self._generate_field('default', attr['default']),
                type=self._generate_field('type', attr['type']),
            )

        return section

    def returns(self, attribute):
        """Create snippet string for a list of return values."""
        section = ''
        template = ':returns {{{type}}: {description}.\n'

        section += template.format(
            description=self._generate_field('description'),
            type=self._generate_field('type', attribute['type']),
        )

        return section

    def yields(self, attribute):
        """Create snippet string for a list of yielded results."""
        section = ''
        template = ':returns {{{type}}}: {description}.\n'

        section += template.format(
            description=self._generate_field('description'),
            type=self._generate_field('type', attribute['type']),
        )

        return section

    def raises(self, attributes):
        """Create snippet string for a list of raiased exceptions."""
        section = ':raises:'
        template = ' {name},'

        for attr in attributes:
            section += template.format(
                name=self._generate_field('name', attr),
            )

        return section[:-1] + '\n'

    def variables(self, attributes):
        """Create snippet string for a list of variables."""
        section = ''
        template = ':param {name} {type}: {description}\n'

        for attr in attributes:
            section += template.format(
                name=self._generate_field('name', attr['name']),
                description=self._generate_field('description'),
                type=self._generate_field('type', attr['type']),
            )

        return section
