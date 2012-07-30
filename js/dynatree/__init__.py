from fanstatic import Library, Resource
import js.jquery
import js.jqueryui

library = Library('dynatree', 'resources')

dynatree_css = Resource(library, 'src/skin/ui.dynatree.css')
dynatree = Resource(library, 'src/jquery.dynatree.js',
        minified='src/jquery.dynatree.min.js',
        depends=[dynatree_css, js.jquery.jquery, js.jqueryui.jqueryui])
