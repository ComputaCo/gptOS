## Layout protocol

Layout happens during the render(self, size) call, from top to bottom:

1. The child should indicate its preferred_size, max_size, and min_size
2. The parent should call render on each of its children, ideally it passes their preferred_size as the size argument, but it can pass any size between min_size and max_size. Children may raise an exception if the size is outside of their min_size and max_size.
3. The parent should truncate its output before returning the rendered content.