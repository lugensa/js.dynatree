from fanstatic import Library, Resource
import js.jquery
import js.jqueryui

library = Library('dynatree', 'resources')

dynatree = Resource(library, 'src/jquery.dynatree.js',
        minified='src/jquery.dynatree.min.js',
        depends=[js.jquery.jquery, js.jqueryui.jqueryui])
