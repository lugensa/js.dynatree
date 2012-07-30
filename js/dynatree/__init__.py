from fanstatic import Library, Resource

library = Library('jquery', 'resources')

jquery = Resource(library, 'jquery/jquery.js',
        minified='jquery/jquery.min.js')
jquery_ui = Resource(library, 'jquery/jquery-ui.custom.js',
        minified='jquery/jquery-ui.custom.min.js')
dynatree = Resource(library, 'src/jquery.dynatree.js',
        minified='src/jquery.dynatree.min.js')
